# State Index

**Read this, then the top block of one state file. That is the whole read.** Everything below a top block is history, recoverable from git at `90c3efd` and `1e8801a`.

## Where the project stands

**460 chapters are canon, `chapters/volume-01` to `chapters/volume-10`.** **Volume 09, *The Regent's Exception* (401–450), is COMPLETE.** **Volume 10, *The House That Refused* (451–500), is OPEN. Batch 0001, Chapters 451–460, is delivered and its cards are in `outline/volume-10.md` §4.** The next phase is **Volume 10 Batch 0002, Chapters 461–470**, and its cards are in `workspace/volume-10/batch-0002/PROMPT.md`.

**Authority.** `outline/series.md` outranks `outline/ending.md`, which outranks `outline/volume-10.md`, which outranks any state file, which outranks any prompt.

## The seven files

| File | Read it for |
|---|---|
| `state/current.md` | Live receipt: phase, volume, calendar + the no-month rule + the retired rail clock, money with working, band payoff, panel, outstanding, hand-off |
| `state/continuity.md` | Halloway, the Stone House, the Fen, **10 documents new in 451–460**, the clocks, what is/is-not true at 460 |
| `state/character-state.md` | Who changed in 451–460; the ten of Halloway; unmoved carry |
| `state/open-threads.md` | Running threads, the **midpoint placement rule**, what the band did not do |
| `state/chapter-summaries.md` | 451–460 paragraphs; 441–450 and 401–420 one-liners |
| `state/batch-summary.md` | **Instruments, 451–460 outputs, the three-band refrain counts, and the only place measurements may appear** |
| `outline/volume-10.md` | The volume's five fixed lines, the calendar table, the cast, the place, the five band plans, the guardrails |

**Top ≤ ~12,000 bytes; file ≤ 60,000. Replace the live block; do not prepend.** The three files over the soft cap at the start of this phase were **pruned**: the Volume 09 blocks in `current.md`, `continuity.md` and `character-state.md` were replaced rather than prepended to, and `chapter-summaries.md` lost its 441–450 paragraphs to one-liners.

**Sizes at the end of this phase.** current **12,875** · continuity **15,917** · chapter-summaries **18,737** · character-state **10,477** · open-threads **8,135** · batch-summary **24,443** · index **~5,000**. All are under 60,000. **Three are over the ~12,000 soft cap: `batch-summary.md`, which is over because §3 is this phase's review record and that record is the most valuable thing in the file and should be moved to `reviews/` at the volume close; and `chapter-summaries.md` and `continuity.md`, which are over on their own content and should be pruned at the top of Batch 0003.**

## Rules that cost the most

1. **Measure; never inherit.** 2. **A `chapter:line` moves when a line moves.** 3. **Run the instrument on files, not lists.** 4. **Gates:** median ≤ 25, >60 ≤ 10%, para ≈ 120, `Nobody said anything` ≤ 5/10k, Ilyan every chapter, ≤ 1 panel a band, **and a mistake that is his own in every chapter, including the chapters where he is right.** 5. **Nobody relieved, forgiven, redeemed or thanked.** 6. **Right of refusal unrestored, and this volume must not give it to anybody.** 7. **No final enemy.** 8. **Do not mark your prompt.** 9. **Measure the refrains every band.** 10. **A title may not state a number the body contradicts.** 11. **A day-count in a chapter must agree with the table, and the closing line of a chapter must not be two days out from its own date line** (458 was, and was repaired). 12. **A new volume is a new substance.** Volume 10 is a market town with a hearth, a beam, a board and a river, and it must not read as Volume 09 with the water turned up.

## Volume and calendar

`shelf = ch − 125`; week = `40 + shelf ÷ 7`; day = `shelf mod 7 + 1`; morning = `ch − 250`; settlement = `ch − 400`; fever = `ch − 283` days. **Anchor 400.** **`ch − 410`, the rail, is RETIRED for Volume 10 and may not be printed in a date line.** **`hall = ch − 446`, the weeks since the common of Halloway was divided and sold.** Weekdays: day 1 Tue … 7 Mon; 451 Sat, 460 Mon, 461 Tue, 470 Thu, 480 Sun, 490 Wed, 500 Sat. **There is no month** and `month` is at 0. Table 451–500 in `outline/volume-10.md` §1.

## Owed

- **Batch 0002 of Volume 10, Chapters 461–470** — the water and the roll and the first third of a remedy. Cards in the phase prompt. **The volume's midpoint may not land in the first third of the batch that carries it.**
- **Repair 401–420** (Volume 09 Bands 0001–0002 carry the prose defect Batch 0003 had). Same gates.
- **Prune `state/chapter-summaries.md`** before the next band adds ten paragraphs.
- **`405:43` wrong figure** (48d/364 ≈ half-farthing/day). One edit outside band; `412:55` right.
- **`state/phase-ledger.json` stale** (reads v1 ch 11–20; manuscript at v10 ch 460). Controller-owned; escalate.
- **`NOVEL_SPEC.md` was three volumes stale at the start of this phase** and its status line was corrected here; it should be corrected at every volume close.
