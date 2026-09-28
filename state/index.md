# State Index

**Read this, then the top block of one state file. That is the whole read.** Everything below a top block is history, recoverable from git at `90c3efd` and `1e8801a`.

## Where the project stands

**470 chapters are canon, `chapters/volume-01` to `chapters/volume-10`.** **Volume 09, *The Regent's Exception* (401–450), is COMPLETE.** **Volume 10, *The House That Refused* (451–500), is OPEN. Batches 0001 and 0002, Chapters 451–470, are delivered and reviewed.** The next phase is **Volume 10 Batch 0003, Chapters 471–480**, and its cards are in `workspace/volume-10/batch-0003/PROMPT.md`.

**Authority.** `outline/series.md` outranks `outline/ending.md`, which outranks `outline/volume-10.md`, which outranks any state file, which outranks any prompt.

## The seven files

| File | Read it for |
|---|---|
| `state/current.md` | Live receipt: phase, volume, calendar + the no-month rule + the retired rail clock, money with working, the ten paid things, the review findings, panel, outstanding, hand-off |
| `state/continuity.md` | Halloway, the Stone House, the Fen, the water list, **Kerby and the office of the county surveyor**, **twenty documents, ten of them new in 461–470**, the clocks, what is/is-not true at 470 |
| `state/character-state.md` | Who changed in 461–470; **Sefa Lund's owed instruction discharged, with the cost named**; the six new named people; unmoved carry |
| `state/open-threads.md` | Running threads, **sixteen hazards, four of them new and three of them about this band specifically**, the midpoint placement rule, what the band did not do |
| `state/chapter-summaries.md` | 451–460 paragraphs; 441–450 and 401–420 one-liners |
| `state/batch-summary.md` | **Instruments re-pointed at 461–470 (the splitter was challenged, tested and stands — §1), this band's outputs, the four-band refrain counts, and §3 and §6, this band's two review records, the second of which refuses two findings. The only place measurements may appear.** |
| `outline/volume-10.md` | The volume's five fixed lines, the calendar table, the cast, the place, the five band plans, the guardrails |

**Top ≤ ~12,000 bytes; file ≤ 60,000. Replace the live block; do not prepend.** The three files over the soft cap at the start of this phase were **pruned**: the Volume 09 blocks in `current.md`, `continuity.md` and `character-state.md` were replaced rather than prepended to, and `chapter-summaries.md` lost its 441–450 paragraphs to one-liners.

**Sizes after this phase's repair pass.** batch-summary **55,807** · chapter-summaries **28,044** · continuity **23,517** · character-state **15,514** · current **16,024** · open-threads **14,453** · index **9,236**. **All seven are under 60,000. Six are over the ~12,000 soft cap and that is the shape of the repository rather than a fault**: `batch-summary.md` is over because §3, §4, §5 and §6 are the four review records and they are the most valuable thing in it — **and it is now at 93% of the hard cap, so the split into `reviews/volume-10/` is owed before Batch 0004, not at the volume close**; `chapter-summaries.md` was pruned last phase and **must be pruned again at Batch 0003**; `continuity.md` grew by ten document rows and is the file a later band cannot do without.

## Rules that cost the most

1. **Measure; never inherit.** **AND, since the second review of 461–470: measure the instrument too.** A review re-typed the sentence splitter's character class, dropped the `*`, added a straight apostrophe, and reported all four bands failing both length gates — which would have had a later band rewrite prose to satisfy a gate it never broke. **The published regex is sound and a splitter reporting a median of 19 and one reporting 26 cannot both be measuring this band.** §1 of `batch-summary.md` now prints the cross-check. **A straight apostrophe is 0 in every band, which is how you know.**
2. **A `chapter:line` moves when a line moves.**
3. **Run the instrument on files, not lists.**
4. **Gates:** median ≤ 25, >60 ≤ 10%, para ≈ 120, `Nobody said anything` ≤ 5/10k, Ilyan every chapter, ≤ 1 panel a band, **and a mistake that is his own in every chapter, including the chapters where he is right.**
5. **Nobody relieved, forgiven, redeemed or thanked.**
6. **Right of refusal unrestored, and this volume must not give it to anybody.**
7. **No final enemy.**
8. **Do not mark your prompt.**
9. **Measure the refrains every band.**
10. **A title may not state a number the body contradicts.**
11. **A day-count in a chapter must agree with the table, and the closing fever of a chapter must agree with its own date line.** **The ordinal in a date line comes off the table, not off the line above it.** **One clock per date line.** **AND, NEW, AND IT IS THE CLASS THIS PROJECT FAILS MOST: a count of how long ago is a day-count and not a week-count.** *The Friday before last* is wrong whenever the last occurrence was the most recent one, and *a fortnight ago* and *nine days ago* were both wrong in 461–470. **Prefer the day-count from the division, which is checkable, over a named weekday, which is not. AND print the unit in the same sentence as the figure.** **AND, NEWEST: two figures of the same shape, close together, neither named as a figure of anything, will be merged by a reader and by a reviewer alike.** `469` had 152 pence (what nineteen households bring in) four lines above 112 pence (what the roll under-charges by); both correct, one of them nearly rewritten out of three canon chapters. **Name what a figure is a figure of in the sentence that uses it.**
12. **A new volume is a new substance.** Volume 10 is a market town with a hearth, a beam, a board and a river, and it must not read as Volume 09 with the water turned up.
13. **After a repair pass, re-open the file and grep the finding's own figure. Do not trust the table.** Six repairs in this repository have been logged as closed and were not applied; `469:117` sat wrong for a full band under a row that said *seventeen*. **A figure that appears in a table, a summary and a prompt is still wrong if it is wrong in the chapter.**

## Volume and calendar

`shelf = ch − 125`; week = `40 + shelf ÷ 7`; day = `shelf mod 7 + 1`; morning = `ch − 250`; settlement = `ch − 400`; fever = `ch − 283` days. **Anchor 400.** **`ch − 410`, the rail, is RETIRED for Volume 10 and may not be printed in a date line.** **`hall = ch − 446`, the DAYS since the common of Halloway was divided and sold, and `hall = 0` is chapter 446, which is the seventh day of the eighty-fifth week and therefore a Monday.** Weekdays: day 1 Tue … 7 Mon; 460 Mon, **461 Tue, 467 Mon, 468 Tue, 470 Thu, 471 Fri**, 480 Sun, 490 Wed, 500 Sat. **The ordinal comes off this table and not off the line above it, and ten of ten were right in 461–470.** **The ordinal in a date line comes off this table and not off the line above it — six were a day out at the first review of 451–460.** **There is no month** and `month` is at 0. Table 451–500 in `outline/volume-10.md` §1.

## Owed

- **Batch 0003 of Volume 10, Chapters 471–480** — the majority's freedom. Cards in `workspace/volume-10/batch-0003/PROMPT.md`. **The volume's midpoint may not land in 471–474.** **Chapter 471 is a Friday, the twenty-fifth day after the division, and a chair of the water board wrote that day on a piece of paper in a room over a taproom on the sixteenth day as a courtesy and has not touched it since; nothing is set down for it.**
- **Prune `state/chapter-summaries.md` again** before Batch 0003 adds ten paragraphs.
- **Repair 401–420** (Volume 09 Bands 0001–0002 carry the prose defect Batch 0003 had). Same gates.
- **Prune `state/chapter-summaries.md`** before the next band adds ten paragraphs.
- **`405:43` wrong figure** (48d/364 ≈ half-farthing/day). One edit outside band; `412:55` right.
- **`state/phase-ledger.json` stale** (reads v1 ch 11–20; manuscript at v10 ch 470, next phase v10 ch 471–480). Controller-owned; **escalated for the fifth phase running and not edited.**
- **Move `state/batch-summary.md` §3, §4, §5 and §6 to `reviews/volume-10/` at the volume close.** They are the four review records and they are the reason a later band can trust anything this repository says about its own repairs — and §6, which refuses two findings, matters more than the ones that were fixed.
- **`466` sits at 10.2% over-60 on its own**, over the per-chapter gate, and has for two bands. The band carries it. **Batch 0003: hold it below eleven, and get it under ten if it costs nothing.**
- **The `novel-reviewer` subagent is refused by the harness** (`agent "novel-reviewer" is a subagent, not a primary agent`), so both reviews of this band ran on the default agent. The external pass still found two defects the self-review had logged as closed, so it earns its keep — but a review that runs as the writer has already agreed with itself. **The fix is in the harness configuration and is controller-owned; do not try to fix it in a state file.**
- **`NOVEL_SPEC.md` was three volumes stale at the start of this phase** and its status line was corrected here; it should be corrected at every volume close.
