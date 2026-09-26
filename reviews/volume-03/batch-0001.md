# Review — Volume 03, Batch 0001 (Chapters 101–110)

Reviewed against the canon chapters and the state record by an independent review agent, then reviewed a second time after a state-reconciliation commit. **The prose findings are fixed. Two of the six findings were about the review itself, not the chapters, and one of them found that a repair pass had misdescribed what it had done. All six are now closed.**

## Method

The reviewer was given `chapters/volume-03/chapter-0101.md` through `chapter-0110.md`, the four state files the commit under review had touched, `workspace/volume-03/batch-0002/PROMPT.md`, and `state/phase-ledger.json`. It was asked to verify the commit's claims against the prose rather than accept them, to cite line numbers, and to report a verdict.

It checked, independently: the weekday and month scan, the System-panel count and placement, the block-quoted blocks, the letting-day arithmetic, the duplicate-line scan, a nine-word-run scan across chapters with dialogue and panels excluded, the reach-width figure, and the ledger's contents against the filesystem.

The first repair pass over this batch is recorded in `state/batch-summary.md` under *Verification and repair record*. This file covers the review of that pass.

## Findings, and what was done

| # | Finding | Fix |
|---|---|---|
| 1 | The commit said "four places" corrected and "all four were state-file claims." There were five, and the fifth was not a number: the rewrite of the Bel Hask line in `state/continuity.md` also changed what the line said had happened, from *the boy was on the flat on the seventh (108)* to *he was turned back at the chain on the seventh (108)*. `chapter-0108.md` supports only the second. The change is right, but it was presented as a number fix | **Disclosed, not reverted.** The prose was not touched. `state/continuity.md` now says at the line that this was an event change and that Chapter 108 is what supports it, and `state/current.md`'s re-entry guard says it in one sentence |
| 2 | The commit and `state/batch-summary.md` both claimed a scan for repeated runs of eight or more words "returned only deliberate in-character anaphora" plus four named categories. A scan excluding dialogue and panels found **60 distinct nine-word sequences recurring across chapters in narration**, none of them in the four named categories. `102:56` and `106:93` were near-identical. `state/current.md` repeated the false claim | **Claim replaced and the prose repaired.** Five passages revoiced: Ch 105 (Efa Lund introduced in Ch 104's words), Ch 106 (the reading), Ch 107 and Ch 110 (the rendering, third and fourth telling), and Ch 110 twice more (a System frame and a hand). 60 runs → 8, and all 8 are a restated date, a restated cost, or one object seen twice |
| 3 | "The only three month-dates" undercounts. There are **five, in three groups**: the third of the second month (104:17, 110:53), the eighteenth of the fifth (110:51), and the eleventh month (102:76, 108:5). The same sentence reached into Volume 02 for the twenty-sixth of the fourth, which is a Chapter 96 date and is not in this batch | Corrected in `state/current.md`, `state/continuity.md`, `state/batch-summary.md` and `workspace/volume-03/batch-0002/PROMPT.md`. The eleventh month is now identified as the only month named on this coast and is not to be used again |
| 4 | `state/phase-ledger.json` reads `"currentPhase": "batch-0002"` pointing at **Volume 01**, Chapters 11–20, a finished batch whose prompt directory already holds a `.done` marker. The ledger holds no record of any Volume 02 or Volume 03 phase. A dispatcher trusting it writes the wrong volume next. **Controller-owned, so not edited** | Flagged at full length in `state/current.md` with the ledger's actual contents quoted, and carried in `state/open-threads.md`. **Needs a human or the controller; no agent can repair it** |
| 5 | No review artifact existed for this batch, and the commit declaring 101–110 closed and canon rested on a pass whose findings lived only in a commit message and a state file. The AGENTS.md gate "a reviewer has checked the result" was unevidenced | **This file.** It was written after the fact from a review that had been run and logged, and says so in its own header rather than claiming to be a fresh reading |
| 6 | `state/batch-summary.md` carried three stacked layers of self-certification, ended on an instruction to the next agent rather than on evidence, and had become mostly a log of its own audits | **Trimmed.** The three headers are now one *Verification and repair record* with three passes under it; every finding and fix is kept; the closing lines are now an explicit list of what is still open — the ledger, the six unreviewed batches, and the unrepaired Volume 02 defects — and end on what was established, not on an instruction |

## Checks that passed, cited

- **No weekday name is used as a date anywhere in Chapters 101–110.** Every occurrence of *may* in the batch is the modal verb, or `THE GUILD MAY WRITE` inside a System panel.
- **Exactly three System panels**, one each in `102:45`, `105:67` and `110:141`, at most one in a chapter, each a plain bold line introduced by a narrative line, each ending in a WHAT IS NOT DECIDED line. Chapters 101, 103, 104, 106, 107, 108 and 109 have none.
- **The only two block-quoted blocks are physical objects**: a sheet of writing paper (`101:69`) and a sheet written at a counter with a borrowed pen (`106:89`).
- **No panel and no person says *Sovereign's Wake*.**
- **No exact duplicated line anywhere in the batch.**
- **The fifth pane's letting day is eleven weeks in `107:31` and twelve in `110:133`**, which is correct because Chapter 110 is seven days later.
- **The eleven-day interval closes.** Bel Hask stopped sending Nim after the second of the second tide; the sixth of the third tide is five days left in that tide plus six into the next.
- **A Reach's width is stated in no chapter in the batch**, so the state record's correction from *about four miles* to *about four and a half* — which is what makes Slackwater's two Reaches nine — disturbs no prose.
- **No voice or register break was introduced by the five prose repairs.** The readings were re-run after them: ten chapters, 2,229 to 5,435 words, every chapter still ending on a complete beat.

## What this review does not cover

- **Chapters 1–100.** The twelve hard defects in `reviews/volume-02/volume-audit.md` are still unrepaired in the prose, and nothing in this batch was built on them.
- **The six batches with no review file:** Volume 01 Batch 0002, Volume 01 Batch 0004, Volume 02 Batch 0001 and Volume 02 Batch 0002, which have never been reviewed, and the two Volume 01 gaps the volume audit does not reach.
- **Whether the batch is any good.** This file records defects found and fixed. It is not a verdict on the writing, and a reader should not treat it as one.
