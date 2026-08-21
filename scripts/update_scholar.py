#!/usr/bin/env python3
"""Sincroniza os números de citação do README com o Google Scholar.

O Scholar não tem API oficial e bloqueia IP de datacenter, então isto roda
localmente (IP residencial), não em CI.

Princípio de projeto: falhar alto. Número de citação errado num perfil público
custa mais do que rotina que quebra barulhento. Se o Scholar bloquear, devolver
lixo ou variar de forma implausível, o script sai com erro e NÃO escreve nada.

Uso:
    update_scholar.py                 # confere e relata (exit 1 se houver drift)
    update_scholar.py --write         # aplica no README
    update_scholar.py --write --commit --push
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

SCHOLAR_ID = "ln9mhjcAAAAJ"
REPO = Path(__file__).resolve().parent.parent
README = REPO / "README.md"
LOG = REPO / "scripts" / "last-run.log"

# marcador -> trecho do título da publicação (None = métrica do autor)
FIELDS = {
    "total": None,
    "airline": "Airline delays",
    "grains": "post-harvest losses",
}

# Guarda anti-lixo: o Scholar às vezes devolve 0 ou valores absurdos quando
# limita a taxa. Recusamos escrever fora desta faixa relativa ao valor atual.
MIN_RATIO, MAX_RATIO = 0.8, 2.0


class Abort(RuntimeError):
    """Erro que impede a escrita."""


def log(msg: str) -> None:
    stamp = dt.datetime.now().isoformat(timespec="seconds")
    line = f"{stamp}  {msg}"
    print(line)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def marker_re(name: str) -> re.Pattern[str]:
    return re.compile(rf"(<!--scholar:{name}-->)(\d+)(<!--/scholar-->)")


def read_current(text: str) -> dict[str, int]:
    out = {}
    for name in FIELDS:
        m = marker_re(name).search(text)
        if not m:
            raise Abort(f"marcador <!--scholar:{name}--> ausente do README")
        out[name] = int(m.group(2))
    return out


def fetch() -> dict[str, int]:
    try:
        from scholarly import scholarly
    except ImportError as exc:  # pragma: no cover
        raise Abort("scholarly não instalado: pip install -r scripts/requirements.txt") from exc

    author = scholarly.fill(
        scholarly.search_author_id(SCHOLAR_ID),
        sections=["basics", "indices", "publications"],
    )
    total = author.get("citedby")
    if not isinstance(total, int) or total <= 0:
        raise Abort(f"Scholar devolveu citedby inválido: {total!r} (provável bloqueio)")

    found = {"total": total}
    for name, needle in FIELDS.items():
        if needle is None:
            continue
        hits = [
            p for p in author.get("publications", [])
            if needle.lower() in p.get("bib", {}).get("title", "").lower()
        ]
        if len(hits) != 1:
            raise Abort(f"{name!r}: esperava 1 publicação casando {needle!r}, achei {len(hits)}")
        found[name] = int(hits[0].get("num_citations", 0))
    return found


def guard(current: dict[str, int], fresh: dict[str, int]) -> None:
    for name, old in current.items():
        new = fresh[name]
        if old and not (MIN_RATIO * old <= new <= MAX_RATIO * old):
            raise Abort(
                f"{name}: {old} -> {new} está fora da faixa plausível "
                f"({MIN_RATIO:g}x-{MAX_RATIO:g}x). Nada foi escrito; confira o Scholar à mão."
            )
        if new < old:
            log(f"AVISO  {name} caiu de {old} para {new} — o Scholar às vezes revisa para baixo")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="aplica os números no README")
    ap.add_argument("--commit", action="store_true", help="commita se houver mudança (exige --write)")
    ap.add_argument("--push", action="store_true", help="dá push depois do commit")
    args = ap.parse_args()

    try:
        text = README.read_text(encoding="utf-8")
        current = read_current(text)
        fresh = fetch()
        guard(current, fresh)
    except Abort as exc:
        log(f"ERRO   {exc}")
        return 2

    drift = {k: (current[k], fresh[k]) for k in FIELDS if current[k] != fresh[k]}
    if not drift:
        log(f"OK     em dia (total={fresh['total']})")
        return 0

    log("DRIFT  " + " · ".join(f"{k}: {o} -> {n}" for k, (o, n) in drift.items()))
    if not args.write:
        log("       rode com --write para aplicar")
        return 1

    for name, value in fresh.items():
        text = marker_re(name).sub(rf"\g<1>{value}\g<3>", text)
    README.write_text(text, encoding="utf-8")
    log(f"ESCRITO {README.relative_to(REPO)}")

    if args.commit:
        body = ", ".join(f"{k} {o}->{n}" for k, (o, n) in drift.items())
        subprocess.run(["git", "-C", str(REPO), "add", "README.md"], check=True)
        subprocess.run(
            ["git", "-C", str(REPO), "commit", "-m",
             f"chore: atualiza citações do Scholar ({body})"],
            check=True,
        )
        log("COMMIT  feito")
        if args.push:
            subprocess.run(["git", "-C", str(REPO), "push"], check=True)
            log("PUSH    feito")
    return 0


if __name__ == "__main__":
    sys.exit(main())
