# Batch 0001 Review Fixes — Volume 11 (Chapters 501–510)

> **THIS FILE WAS WRITTEN BY THE REPAIR AND NOT BY THE REVIEWER, and it says so at the top because
> `state/batch-summary.md` §2b set that rule and this repository has already broken it twice: *a
> receipt written by the repair is not a record of the review.* The review ran, produced
> `logs/batch-0001.review.log`, and committed nothing; its findings are transcribed below and every
> one of its nine verified-sound items is kept beside them so that a later reader can see what it
> examined and not only what it changed. **WHAT IS TRANSCRIBED IS THE REVIEW'S VERDICT AND ITS
> FINDINGS, IN ITS OWN CLASSIFICATION AND ITS OWN ORDER. WHAT IS NOT IN IT IS THE REPAIR'S REASONING,
> WHICH LIVES IN `state/current.md` §0.12.**

**Source of findings:** `logs/batch-0001.review.log`, produced by the review phase over commit
`e11f038` (*novel: save writer work batch-0001*), which was the **second** repair pass over
501–510. The reviewer re-ran the published instrument itself rather than trusting the state files,
checked the money, the day-counts, the titles and the line citations by hand, and refused to touch
one file on ownership grounds.

**Scope of this file:** what the review found, what the repair did about each, what was deliberately
not changed, and what the next phase must not inherit. **The prose is the canon.** The narrative of
the review and the repair is §0.12 of `state/current.md`, which is the authority; this file is the
receipt, and it is the first artifact to exist for Volume 11.

**Verdict, in the reviewer's words:** *the underlying chapter repairs are mostly sound and
verifiable — I independently confirmed the money fix, the day-count fix, the ninety→forty tree fix,
the 300/2,400 arithmetic, and the `507`/`509` orchard contradiction repair. The certification layer
is where this phase fails, and it fails in exactly the class §0.11 names against itself: "a
certifying line is certified by whatever it was pointed at."*

## 0. What the review found, in its order and its severity

| # | Finding | Severity | Where it was |
|---|---|---|---|
| **R1** | **`state/batch-summary.md` was not updated — it now certifies figures that are false.** The second repair swept `current.md`, `continuity.md`, `character-state.md`, `chapter-summaries.md` and the next-phase prompt and **skipped the batch summary**, which `AGENTS.md` explicitly requires. Band words 26,581 against an instrument print of **26,606**; sentences 1,210 against **1,208**; eight of ten per-chapter rows wrong; `“*` 135.8 against **135.7**; range 2,301–3,483 against **2,300–3,488**. `batch-summary.md:11` still asserted *"The row sums to 26,581 and the band total is 26,581, and the instrument prints both and they must be equal."* | **High** | `state/batch-summary.md` |
| **R2** | **`state/current.md:124` — corpus size exceeds the corpus.** §0.11 certified the real-world place-names *"at 0 across **511** chapters."* `find chapters -name 'chapter-*.md' \| wc -l` returns **510**. *"A zero-count certificate cannot be issued over a larger corpus than exists."* (The zero held; the claim over the corpus did not.) | **High** | `state/current.md` |
| **R3** | **`chapters/volume-11/chapter-0510.md:89` — the repair replaced one false count with another, and the prose now contradicts itself on the same line.** *"Four sentences, in a different ink, and the longest of them is about thirty words. They say that…"* — that second sentence is **115 words**, against §0.11's claim of *"the longest of them 36 words and so about thirty,"* false by roughly **3×**. Called *"a title-against-body-class defect — the exact class item 4 was written to eliminate. Any reader can count it."* **Secondary, same line:** `510:87` already ends *"in a different ink,"* so the phrase now stands in consecutive paragraphs. | **High** | `chapter-0510.md` |
| **R4** | **The `**` → `*` repair in `504` rests on a fabricated instrument mechanism.** `reviews/volume-10/instrument.py:182-183` prints, per file, `open(f).read().count("**")` — a raw substring count. *"There is no panel tally and no subtraction anywhere in the file."* §0.11's *"the instrument's paragraph rule subtracts as a System panel"* is invented, and `-0504=2**` only ever meant *this file contains `**` twice*. *"The instrument prints no panel count at all, so 'ONE panel' is asserted, never measured."* **The edit itself is still defensible under the one-panel-per-chapter rule.** | Medium | `state/current.md:120` |
| **R5** | **`state/phase-ledger.json` points the fleet at the wrong phase.** `currentPhase: "batch-0002"` carries `volume: 1, startChapter: 11, endChapter: 20` and a note directing to `workspace/volume-01/batch-0002/PROMPT.md`. The real next phase is Volume 11, chapters 511–520. *"Worse, the ledger's target already exists: `chapters/volume-01/` contains `chapter-0001` … and the volume-01 prompt opens 'Write Chapters 11–20… do not restart or replace them' — a self-contradicting instruction."* **The reviewer did not touch it: "This file is controller-owned, so I have not touched it, but it needs a controller-side correction before the next dispatch or it will send the writer to overwrite finished chapters."** | Medium | `state/phase-ledger.json` — **not owned by this phase** |
| **R6** | **No `reviews/volume-11/` directory exists.** *"Volume 11 has ten canon chapters and two repair passes, and no review artifact in its own volume directory."* `AGENTS.md`'s quality gate requires *"A reviewer has checked the result."* | Medium | `reviews/volume-11/` |

## 1. What the review verified sound, and therefore what must not be touched

These are the reviewer's own conclusions and they are the reason this repair was nine edits and not a
rewrite. **Every one of them was re-checked before this file was written, because a certificate about
a repair is the same class of thing as a certificate about a band.**

- **Money repair correct** — 140 acres × 4s = 560s = £28 = 6,720d. `503:5` and `506:7` agree with `506:37`; swept clean through `continuity.md` and `character-state.md`.
- **`502:81` day-count correct** — 81 days = 11 weeks 4 days (the old *"ten weeks and three days"* = 73).
- **`510:23` correct** — 190 + 110 = 300, now stated as *"about three hundred … in a town of about two thousand four hundred."*
- **`509` tree/frost figures** now consistent at forty trees and four weeks across the title, `509:13` and `509:139`; `509:11`'s *"a fortnight later"* is a lateness measurement and not a contradiction.
- **All §0.11 line citations spot-check correctly** — `503:5`, `506:7`, `506:37`, `507:11`, `507:95`, `509:13`, `509:139`, `510:23`, `502:81`, `505:7`.
- **`505` clock repair coherent** — Abel Tarn at 11:30, Barnaby Rill at the twelfth hour, matching `505:7`'s *"swept it again at noon on the Thursday."*
- **`507`/`509` orchard contradiction genuinely resolved**; `England` eliminated; no residual *"ninety half-size"* in prose.

## 2. What this repair did, one line each

| Finding | Action | Files |
|---|---|---|
| **R3** | The semicolon list is now **four separate sentences of 28, 18, 27 and 23 words**, so *four sentences* and *about thirty words* are both checkable with a pencil. The duplicated *"in a different ink"* is out of the second sentence; `510:87` carries it. **Nothing else in any of the ten chapters was touched.** | `chapters/volume-11/chapter-0510.md:89` |
| **R1** | Re-measured with the published instrument and **every figure in §0 replaced**, with the superseded set left visible above it because *"deleting it is how a figure goes stale twice."* Two further unsupported claims in the same block were corrected — the `505` dialogue-line history and the twelve-`**` panel arithmetic — and a meta-narration leak of the kind §0.11 was written about was swept out of the protagonist paragraph. | `state/batch-summary.md` |
| **R2** | **510 chapters**, which is every chapter file that exists, and the sweep result is stated as a result rather than as a size. | `state/current.md:124` |
| **R4** | The reason rewritten against the instrument's actual lines 90 and 182, the false clause named as false, and **`ONE panel` now marked as counted by hand** rather than presented as a machine measurement. The `504` edit itself is kept and its merits restated. | `state/current.md` §0.11 item 7, and `state/batch-summary.md` §0 PANELS |
| **R5** | **Not fixed, and cannot be.** The file is controller-owned and no phase may edit it. **Escalated** in `state/current.md` §0.12, which records that this is the **twelfth** phase to escalate it and the twelfth time to be right to escalate and wrong to have had to, and states the concrete risk: *"it will send the writer to overwrite finished chapters."* | — |
| **R6** | This directory and this file. **It is written by the repair and says so in the first line**, which is the rule `state/batch-summary.md` §2b set. | `reviews/volume-11/batch-0001.md` |

## 3. The measurements this repair stands on

Run, not re-typed, with the corpus named in the command:
`python3 -c "import sys;sys.path.insert(0,'reviews/volume-10');import instrument as I;I.run(501,510,vol='volume-11')"`

**26,598 words · 1,211 sentences · median 18 · over-60 2.89% · max paragraph 120 · max sentence 113**, with a per-chapter row for all ten; `“*Say` 11 (4.1/10k), `“*Go on` 0, `say the rest` 0, `“*` 361 (135.7/10k) and 287 at line start; silence 5 across fifteen wordings with the chorus subset at 0; straight ASCII apostrophes 0; `thanked` 7 and all seven negations; **one panel, counted by hand, and the ten `**` at `508` are that panel and not two measurements.**

**The band moved for this repair and only for this repair: 26,606 → 26,598 words and 1,208 → 1,211 sentences, both from `510:89`.** The previous two certifications, at 26,581 and 26,606, are superseded and are left in place rather than deleted. **Three certifications of one band is not a failing of the instrument. It is the instrument working, and the first two certificates being wrong.**

## 4. What a later band must take from this

1. **A repair that lists the files it swept is enumerating its memory.** §0.11 wrote *all four are swept* and five files needed it and four got it — the one left behind was the batch summary, the file a checker opens first. **Run the sweep as a command.**
2. **A sentence about a chapter is not measured by reading the chapter's row.** Two claims in one state block about `505`'s dialogue lines and about the band's bold marks were supported by no run and contradicted the rows in their own block.
3. **Two repairs in succession on one sentence is a sign the first one was not read.** `510:89` was repaired twice and each pass replaced a false count with a false count. **Make the page true rather than making the claim cheaper.**
4. **A reason you cannot point at a line of the instrument for is probably not a reason.** And a number printed beside a machine measurement is still yours to check by hand.
5. **A zero-count certificate cannot be issued over a corpus larger than the corpus.**
6. **A review that runs, finds blocking defects in a canon band, and commits nothing leaves the next reader with a log and not a record.** This file exists because of that, and it should have been written by the reviewer.
