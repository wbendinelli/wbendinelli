# Research

Three lines of work, one question: **how much is a number about a person allowed to mean?**

Two of them have been in the literature long enough to be measured. So I measured them — not by
counting citations, but by reading them. In September 2026 I retrieved every paper that cites my
two published articles, read the ones I could obtain, and coded what each citation actually does
with the work. The method, the data and the code are public in
[citation-audit](https://github.com/wbendinelli/citation-audit).

**How to read this page.** Live citation counts are written by a script that refuses to publish a
value it cannot verify. Audit figures are a frozen snapshot dated 2026-09-04 and every one of them
is printed by a committed script in the audit repository. Where a number would flatter me and the
evidence does not support it, the unflattering number is the one on the page.

---

## Airline delays, congestion internalization and non-price spillover effects of low cost carrier entry

*Transportation Research Part A: Policy and Practice*, 2016 · [10.1016/j.tra.2016.01.001](https://doi.org/10.1016/j.tra.2016.01.001)

**The question.** Does airline concentration make flights later or earlier? The literature had two
answers that never met. One held that an airline dominant at an airport internalizes the congestion
it causes, so concentration reduces delays. The other held that concentration on a route removes the
competitive pressure to be punctual, so it increases them.

**What the paper established.** Both, and they are not in conflict. Measured on a panel of 209
Brazilian routes, concentration at the endpoint city reduces delays while concentration on the route
increases them, estimated in a single econometric model with instruments for both. The two
literatures were describing different levels of the same market.

**What the field did with it.** The share of papers citing both literatures together rose from 5.3%
before 2016 to 8.5% after, and the jump does not reproduce at placebo cut-offs in 2011 or 2020.
Among papers that cite both, 29.2% cite this one; among papers that cite only one side, 3.5% do —
an odds ratio of 11.4. Two independent citing papers describe the mechanism in their own words: one
in *Transportation Research Part A* writes that the article conciliates the two strands by
separating market from airport concentration. The reconciling framework, not the spillover result
in the title, is what the field adopted: the airport-level finding carries 18 citations, the
framework 8, the title result 4.

**Where to check.** [Report, §6](https://github.com/wbendinelli/citation-audit) · co-citation data in
`data/cocit/`

---

## What are the main factors that determine post-harvest losses of grains?

*Sustainable Production and Consumption*, 2020 · [10.1016/j.spc.2019.09.002](https://doi.org/10.1016/j.spc.2019.09.002)

**The question.** Post-harvest loss is discussed case by case, crop by crop, country by country.
What determines it across countries, at the level where agricultural policy is actually set?

**What the paper established.** On a cross-country panel for rice, maize, soy and wheat, income per
capita is the strongest determinant of loss, and the gaps between income groups persist after
controls. The policy consequence is the paper's own synthesis: raising output without post-harvest
infrastructure raises loss, so production programmes that stop at the farm gate produce surplus and
spoilage together.

**What the field did with it.** This is a reference paper. It is cited to establish the premise, not
to build on: 85% of its in-text citations are passing mentions, and none are foundational. The
citation that matters is the exception. The supply-versus-loss trade-off is cited 11 times, 10 of
them faithfully, and the policy recommendation 7 times, 6 faithfully — the highest fidelity of any
claim across both papers. The field took the result and repeated it correctly.

**One honest caveat.** Being the accessible synthesis has a cost. Figures the paper relays from the
FAO literature are credited to it by later authors: of the 6 citations that use relayed material, 5
attribute it to us. That is a documented pattern in citation behaviour, not a defect of the paper,
but anyone citing it for the 20–35% loss range should cite Gustavsson and colleagues instead.

**Where to check.** [Report, §5 and §7](https://github.com/wbendinelli/citation-audit) · claim
register in `data/claims/`

---

## Dynamic Leadership Vitality Theory

Working paper · [SSRN preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6455001) ·
code: [`dlvt`](https://github.com/wbendinelli/dlvt)

A two-state formal model of how enacted leadership scope, coordination load and vitality coevolve.
The central result is the counterintuitive one: narrowing a leader's scope changes what the system
can carry and how long adjustment takes, but leaves long-run vitality where it started. Relief lands
in the transient, not in the equilibrium. The manuscript is complete; the SSRN preprint is an earlier
version under a title the current one abandons. No reception to report yet, and this page will not
pretend otherwise.

---

## Who cites the work

Citation counts say how often; the venue says by whom. Of the citing records whose journal could be
matched to a Scimago quartile, this is where they land. The denominator is every matched citation,
not only the ones I could read, so the figure does not depend on which publishers granted me access.

| | Q1 | Q2 | Q3 | Q4 | Matched | Q1 share |
|---|---|---|---|---|---|---|
| Airline (2016) | 43 | 4 | 1 | 2 | 50 | 86% |
| Grains (2020) | 26 | 12 | 7 | 3 | 48 | 54% |
| Both | 69 | 16 | 8 | 5 | 98 | 70% |

Seven in ten citations come from first-quartile journals, and for the aviation paper it is close to
nine in ten. The journals that cite most often are the field's own: *Journal of Air Transport
Management*, *Transport Policy*, *Transportation Research* Parts A and E, *Journal of Stored
Products Research*, all Q1.

The remaining records — 35 outside Scimago and 43 with no quartile assigned — are conference
proceedings, book chapters, preprint repositories, theses and journals too recent or too regional
for Scopus. They are counted in the inventory and excluded from this table, because a quartile they
never had cannot be averaged in.

---

## The numbers, and the ruler each one uses

A citation count means nothing without the database that produced it and the population it is
compared against. All three rows below are true at the same time.

| | Airline (2016) | Grains (2020) |
|---|---|---|
| Google Scholar | <!--scholar:airline-->95<!--/scholar--> | <!--scholar:grains-->76<!--/scholar--> |
| OpenAlex | <!--openalex:airline-->53<!--/openalex--> | <!--openalex:grains-->60<!--/openalex--> |
| Field-normalized citation impact | <!--fwci:airline-->13.2<!--/fwci--> | <!--fwci:grains-->5.3<!--/fwci--> |
| Percentile among all works of its year | 96–99 | 95–99 |
| Rank within the same journal and year | 74th of 206 | 39th of 92 |

The first three rows say the papers are cited far above what their field and year would predict, in
the top decile of their cohort worldwide. The last row says that among the articles their own
journals published that year, they sit just above the middle. Both are correct. *Transportation
Research Part A* published 206 research articles in 2016 with a median of 26 citations, well above
the world median for that year: publishing in a high-citation venue raises the bar around you. The
journal ranking uses OpenCitations for the target and the whole cohort, so the comparison is
internally consistent even though its counts are lower than Scholar's.

---

## The audit

Between the citation count and the claim "this work mattered" there is a step almost nobody takes:
reading the citations. I took it.

I assembled the citing literature from four bibliographic databases plus Google Scholar, obtained the
full text wherever access allowed, and read every one I could. Each citation was coded on independent
axes — where the work appears, how deeply it is used, what stance the citing author takes, and
whether the claim attributed to the paper is one the paper makes. The coding was then repeated blind
by two other coders with the labels removed, and disagreements were settled by a documented panel.

| | |
|---|---|
| Citing records assembled | 176 |
| Read and coded | 104 |
| Cited in the body of the text | 92 |
| Present only in the reference list | 12 |
| Accurate | 57 |
| Imprecise | 19 |
| Attributing a claim the paper does not make | 16 |

Sixteen in ninety-two is 17%, which sits inside the 13–25% range published for quotation accuracy in
the medical literature. It is a fact about how citation works, not an accusation. The single most
useful result of the whole exercise is methodological: without a written register of what each paper
actually claims, the original coder could not detect misattribution at all. Agreement on accuracy ran
at κ 0.14 before the register existed and κ 0.60 between two independent coders who had it.

Everything above is reproducible: [github.com/wbendinelli/citation-audit](https://github.com/wbendinelli/citation-audit)

---

## Cite

Bendinelli, W. E., Bettini, H. F. A. J., & Oliveira, A. V. M. (2016). Airline delays, congestion
internalization and non-price spillover effects of low cost carrier entry. *Transportation Research
Part A: Policy and Practice*, 85, 39–52.

Bendinelli, W. E., Su, C. T., Péra, T. G., & Caixeta Filho, J. V. (2020). What are the main factors
that determine post-harvest losses of grains? *Sustainable Production and Consumption*, 21, 228–238.

[Scholar](https://scholar.google.com/citations?user=ln9mhjcAAAAJ) ·
[ORCID](https://orcid.org/0000-0001-8312-1825) ·
[Back to profile](README.md)
