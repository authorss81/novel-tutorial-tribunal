# State Index

**Read this, then the top block of one state file. That is the whole read.** Everything below a top block is history, not memory, and it is recoverable from git at `1e8801a`.

## Where the project stands

**430 chapters are canon, in nine directories, `chapters/volume-01` to `chapters/volume-09`.** Volume 09, *The Regent's Exception*, is open: batches 0001 to 0003 are delivered, chapters 401 to 430, and **the next phase is `workspace/volume-09/batch-0004/`, chapters 431 to 440, on disk and unmarked.**

**Authority order.** `outline/series.md` outranks `outline/ending.md`, which outranks `outline/volume-09.md`, which outranks any state file, which outranks any prompt.

## The six files and what each one is for

| File | About | Read it for |
|---|---|---|
| `state/current.md` | The live receipt: what this phase did, the volume's shape, the calendar, the money with its working, what the band paid, the panel register, what is outstanding, the hand-off | Almost everything, if you are about to write |
| `state/continuity.md` | The fact base: the ground, the road, the twelve documents in play, the four clocks, what is and is not true at the end of 430 | Any figure, any document, any date |
| `state/character-state.md` | Every living person this volume has moved, with what they said and what it cost | Who is who, and who owes what |
| `state/open-threads.md` | What is running, what was opened, what the band did not do | What you may resolve, and what you may not |
| `state/chapter-summaries.md` | One paragraph per chapter for 421 to 430, one line each for 401 to 420 | The last band, in order |
| `state/batch-summary.md` | The instruments and their outputs, with the instruments printed | How to check your own band, and against what |

**A top block stays under about 12,000 bytes and a file under 60,000. The record was 5.9 MB at the batch-0003 review and is now 65 KB across the six. Do not prepend; replace the live block.**

## The rules that have cost this project the most

1. **Measure; never inherit a figure.** A number that was not produced by an instrument you can re-run is not a number, whatever block it is printed in.
2. **A `chapter:line` pointer moves when a line moves.** Read it against the file.
3. **Run the instrument against the chapter files, not against a list.** Three lists were each found short once, and one was short by ten.
4. **A prose gate is a measurement, not an adjective.** Median sentence ≤ 25 words, ≤ 10% over 60 words, paragraph ≈ 120 words, `Nobody said anything` ≤ 5 per band, the protagonist named in every chapter, ≤ 1 System panel per band. The batch-0003 review rejected a band of run-on dialogue on exactly these numbers.
5. **Nobody is relieved, forgiven, redeemed or thanked.** Including the office, which is right about the roads.
6. **The right of refusal is unrestored and no batch may restore it by accident.**
7. **Do not introduce a final enemy.** The First Witness is the ending's problem, not a volume's villain, and nothing in this world answers, replies or renders.
8. **Do not mark your own prompt.** The controller marks it.

## The volume and the calendar

`shelf = chapter − 125`; week = `40 + shelf ÷ 7`; day = `shelf mod 7 + 1`; morning = `chapter − 250`; days since the settlement = `chapter − 400`; days since the rail = `chapter − 410`; fever age = `chapter − 283` days. **The anchor is chapter 400. `chapter − 351` is retired.** The table for 431 to 450 is in `outline/volume-09.md` §1, and a band takes its dates from that table rather than working them out.

## Owed and not yet done

- **A repair phase for chapters 401 to 420.** They have the prose defect the 421 to 430 band had — median 23 and 22% of sentences over 60 words, and Ilyan named in two chapters of ten. The same instrument and the same gates apply. Nothing else needs saying about it.
- **`state/phase-ledger.json` is stale for the fifth phase in a row** and reads volume 1, chapters 11 to 20, while the manuscript is at chapter 430 of volume 9. It is controller-owned, this project has flagged it every phase and correctly not touched it, and **it should be escalated to whoever owns the controller.** If phase selection reads that file, the pipeline is dispatching against volume-1 chapter numbers.
- **`405:43` carries a wrong figure** — forty-eight pence over 364 days is a shade over half a farthing a day. One edit, in a chapter outside the band that found it. `412:55` has it right.
- **Five of nine volumes have no volume audit**, and the audits are separate phases with their own prompts.
