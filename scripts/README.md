# scripts

## `update_scholar.py` — sincroniza as citações com o Google Scholar

O README traz três números que envelhecem sozinhos: total de citações e as
contagens dos dois papers principais. Este script vai ao Google Scholar, compara
e atualiza.

### Por que roda local e não no GitHub Actions

O Google Scholar não tem API oficial e bloqueia IP de datacenter. Um workflow
do Actions falharia — ou, pior, passaria a devolver lixo em silêncio. A rotina
roda na sua máquina, de IP residencial, onde a leitura funciona.

### Como os números ficam presos no texto

Cada número vive entre marcadores HTML, invisíveis no README renderizado:

```markdown
**<!--scholar:total-->191<!--/scholar--> citations**
```

O script só troca os dígitos entre marcadores. Não reescreve prosa.

### Uso

```bash
scripts/.venv/bin/python scripts/update_scholar.py                      # confere
scripts/.venv/bin/python scripts/update_scholar.py --write              # aplica
scripts/.venv/bin/python scripts/update_scholar.py --write --commit --push
```

Códigos de saída: `0` em dia ou aplicado · `1` há defasagem e nada foi escrito ·
`2` erro que impediu a escrita.

### Falha alto, de propósito

Número de citação errado num perfil público custa mais caro que rotina que
quebra barulhento. O script se recusa a escrever e sai com `2` quando:

- o Scholar devolve `citedby` ausente, zero ou não-inteiro (sinal de bloqueio);
- o título de um paper casa com nenhuma ou mais de uma publicação;
- um marcador sumiu do README;
- o valor novo sai da faixa de 0,8× a 2× do atual — a variação implausível que
  caracteriza resposta corrompida por rate limit.

Queda pequena não bloqueia, mas é registrada como `AVISO`: o Scholar às vezes
revisa contagens para baixo, e isso é legítimo.

### Agendar (launchd, semanal)

```bash
cp scripts/com.wbendinelli.scholar-update.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.wbendinelli.scholar-update.plist
```

Roda segunda, 9h — se o Mac estiver dormindo, roda ao acordar. Para revisar
antes de publicar, tire `--push` do plist: o commit fica local esperando você.

Rodar uma vez agora, sem esperar a segunda:

```bash
launchctl start com.wbendinelli.scholar-update
```

Desativar:

```bash
launchctl unload ~/Library/LaunchAgents/com.wbendinelli.scholar-update.plist
```

Histórico em `scripts/last-run.log` (fora do git). Se ele parar de crescer, a
rotina morreu — é o sinal para olhar `launchd.err.log`.
