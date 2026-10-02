# VOLUME 19 CLOSE — REVIEW REPAIR `0V19L`

This is the repair receipt for `reviews/volume-19/batch-0006-close-0V19J.md`. It records a review of the volume 19 close, six findings, a decision on each, and the state of the disk afterwards.

**Nothing in `chapters/` was touched. Zero files changed under `chapters/`. No planned plot was altered. No controller file was edited.**

---

## 0V19L.1 WHAT WAS REVIEWED, AND WHAT WAS VERIFIED AGAINST THE DISK

Commit `47e4111 novel: save writer work close-0006` — the close receipt, six state pointers, and the volume 20 planning prompt. The reviewer's line references were sampled and reproduce. The close's central factual claim holds: `chapters/volume-19/` holds forty files, `921`–`930` are absent, and volumes 01 through 18 hold fifty each.

**The reviewer's arithmetic, character, and structural findings are all confirmed.** Nothing below disputes them.

## 0V19L.2 FINDING 1 — THE DISPATCHER WOULD RE-RUN FINISHED WORK. REPAIRED. AND IT WAS TWO PHASES.

**This was the finding that would have caused damage on the next unattended run.**

`scripts/novel_runner.sh` selects the first prompt in sorted order carrying no `.done`, `.blocked` or `.retired`, whose `.retry-after` has passed. Replaying that loop over the state at `47e4111` selected `workspace/volume-19/batch-0004/PROMPT.md` — the `931`–`940` band, ten finished chapters.

**The work had landed. Only the marker had not.**

| what | where | landed in |
|---|---|---|
| ten chapters, `931`–`940` | `chapters/volume-19/` | `7774ffe` |
| seven state blocks | `reviews/volume-19/batch-0004-*.md` | `7774ffe` |
| the pointer to band 5 | `workspace/volume-19/batch-0005/PROMPT.md` | `7774ffe` |
| **the `.done` marker** | — | **never** |

The controller then deferred the phase twice and set `.wip-conflict` on it. Its `.retry-after` of `1790980211` had expired. The retire regex does not match its first line, so the phase would never have been retired either.

**The reviewer named a second instance of the same defect only as supporting evidence, and it was a live hazard of the same kind. `workspace/volume-19/plan-0001/` created `outline/volume-19.md` — four hundred lines, a hundred and forty-six thousand bytes, a finished volume plan with all five bands and all the guardrails — in commit `651111c`, which is the commit whose subject line is `novel: defer plan-0001`.** That phase was going to be dispatched to re-plan a volume that already had its plan.

**Both were closed the way the controller itself closes a phase, using the exact file set at `scripts/novel_runner.sh:266`:**

- `workspace/volume-19/batch-0004/` — `.done` written; `.deferred`, `.attempts`, `.retry-after`, `.wip-conflict` removed.
- `workspace/volume-19/plan-0001/` — `.done` written; `.deferred`, `.attempts`, `.retry-after` removed.

**Nothing was deleted, nothing was retired, and no prose was touched.**

### The reviewer's hesitation, answered rather than overruled

The reviewer declined to write the marker because doing so would "silently ratify a ten-chapter gap." That was the right instinct and the wrong category.

**`batch-0004` is `931`–`940`.** The gap is `921`–`930`, and no directory was ever created for it — the on-disk slot sequence is `0002`, `0003`, `0004`, `0005` and it skips no number, because the missing band never entered the sequence. The marker records forty chapters that exist. It asserts nothing about ten that do not.

**Writing that marker does not ratify the gap. It records forty chapters and is silent about the other ten, and the gap is repaired separately at `0V19L.3`.**

## 0V19L.3 FINDING 2 — THE MISSING BAND WAS UNWRITABLE. REPAIRED.

**Chapters `921`–`930` were owed work that no dispatched phase could perform.** Three things blocked them at once:

1. No phase directory existed for them. `batch-0002` is `901`–`910`, `batch-0003` is `911`–`920`, `batch-0004` is `931`–`940`, `batch-0005` is `941`–`950`.
2. `workspace/volume-20/plan-0001/PROMPT.md` forbade writing them four times over.
3. The volume 19 close recorded them as owed by nobody.

**They now have a named owner: `workspace/volume-19/batch-0003-gap/`.**

The directory name carries the band, not a slot. It sorts before `close-0006` and before `plan-0001` inside `workspace/volume-19/`, and `volume-19` sorts before `volume-20`, so **the missing band is dispatched before anything that would plan or write past it.**

### What the new phase is, and what it is not

It writes ten chapters and nothing else. It does not restart, reopen, re-outline or edit `901`–`920` or `931`–`950`. It changes no plan: band 3 of `outline/volume-19.md` §7 is the authority, and where the prompt and the plan disagree the plan wins and the disagreement is reported.

It carries, from §7 item 3, all four unspent obligations:

- two people each asked once, and that this is not a corroboration, and there is no third person to ask, and the two accounts are each true and the truth is not the thing;
- `930` as an off-morning and a week's first day, written once and in one shape;
- a title at `930` that names a weekday names **a Tuesday**;
- no chapter prints the number of people who were in a room — house figure zero, and this is the band where a reader will ask for it.

### The ladder was checked three ways before it was handed over

| check | result |
|---|---|
| the six figures a morning, run forward from `920` on the page | agrees with the plan's §4 table row for row |
| the water, run from its own head at `682` on a period of eight | agrees with the same ten rows |
| the closing edge, `930` into `931` on the page | fever `92w 3d` into `92w 4d`, morning `680` into `681`, week `155 / 1` into `155 / 2` — no seam |

The off-mornings at `922` and `930` are a Monday and a Tuesday, the anchor at `927` is ninety-two weeks old, and the seven standing counters were each confirmed against the prose of `920` and `931` before their formulas were written down.

**The prompt tells the writer to derive every counter from its formula and to check the ladder a third time against `920` and `931`, because a row of a formula is not a row of a chapter.**

## 0V19L.4 THE VOLUME 20 POINTER WAS CARRYING THE BAND AS OWED IN VOLUME 20. CORRECTED.

`workspace/volume-20/plan-0001/PROMPT.md` carried two claims that were true when the close wrote them and are now false.

A correction block was inserted after its first page. It states that the ten chapters are owed to `workspace/volume-19/batch-0003-gap/`; that the close's "owed by nobody" table is superseded by that dispatch and not by anything invented; and that the two off-morning sentences at `922` and `930` are owed in volume 19, band 3, and not in volume 20.

**The fourfold prohibition on writing, planning, inventing or summarising `921`–`930` was deliberately left standing whole.** That prohibition binds the volume 20 planner, not this repair, and band 3 now has a phase of its own.

The prompt now also carries three instructions for whoever runs it: count the files in `chapters/volume-19/` first and refuse to plan volume 20 if the count is forty; read the `close-0007` receipt before the plan if it is fifty; and take every figure off the page rather than off the forty-chapter close or the plan's tables.

## 0V19L.5 THE SIX STATE POINTERS. AMENDED, IN PLACE, WITHIN CAP.

Each of the six files the close wrote now carries one added sentence naming `workspace/volume-19/batch-0003-gap/` as the owner of `921`–`930`.

**The amendment was appended to the existing top block in every file. No block was moved, no block was summarised, and no existing sentence was removed.** All six remain under the 60,000-byte cap:

| file | before | after | headroom |
|---|---|---|---|
| `state/batch-summary.md` | 58,050 | 58,286 | 1,714 |
| `state/character-state.md` | 59,640 | 59,740 | **260** |
| `state/continuity.md` | 56,208 | 56,444 | 3,556 |
| `state/current.md` | 57,435 | 57,671 | 2,329 |
| `state/index.md` | 55,974 | 56,210 | 3,790 |
| `state/open-threads.md` | 52,236 | 52,472 | 7,528 |

**`state/character-state.md` is thin and is handled, not ignored.** The band prompt carries the remedy the repository already uses at `0T` and `2u`: move the oldest whole block out to `reviews/volume-19/` before appending, nothing summarised, nothing cut. That file's amendment was shortened from the other five so that it costs a hundred bytes rather than two hundred and thirty-six.

`state/current.md` keeps its rule of zero numbered data rows, and the ten rows plus the bold eleventh which is the water are directed into the band's own `batch-summary` block.

## 0V19L.6 FINDINGS 3, 4, 5 AND 6 — REPORTED, AND TWO OF THEM DELIBERATELY NOT REPAIRED

**Finding 3, the close ran on an incomplete volume.** The volume was forty of fifty. The close said so in those words at `§0V19J.11` clause (a) and asserted completeness nowhere. A close that runs on an incomplete volume and says so has done its work. The incompleteness is now cured by a named phase rather than by a close, and this is recorded at `§0V19J.12.3`.

**Finding 4, `state/phase-ledger.json` reads `currentPhase: batch-0002`, `volume: 1`.** Stale and inert — no script or workflow reads it; the only three mentions anywhere are skip-list entries in review helper scripts. **It is controller-owned and it was not touched. It is reported as it stands.**

**Finding 5, the receipts have degenerated past readability — five `⚠` a line, headings that are unbroken runs of bolded capitals.** It is true of the volume 19 close and true of every receipt behind it back to volume 18. It is measured: this receipt's predecessor carries 1,721 `⚠` and 2,640 `**` across 362 lines, against 29 clean lines in the volume 01 review.

**It is not repaired here, and the reason is not cost.** It is a house style, not a defect this close introduced. Restyling one receipt out of a hundred would make the document the next writer is told to read first the only one that reads differently from all the others, which trades a legibility problem for a consistency problem.

**The half that can be done safely was done: `workspace/volume-19/batch-0003-gap/PROMPT.md` is written in plain markdown with no glyph runs and no bolded-capital headings.** It is the one document the next writer must read before writing a word, so it was written to be read.

**Finding 6, `state/character-state.md` has thin headroom.** Handled at `0V19L.5`.

## 0V19L.7 ONE FACTUAL SLIP IN THE CLOSE RECEIPT, CORRECTED WHERE IT STANDS

At `§0V19J.0` the close printed **"the slot named for the missing band is `batch-0003`"** — and in the same sentence printed `batch-0003` = `911`–`920`. Both cannot be true, and the first is the false one. `batch-0003` is `911`–`920`, it is on disk, and it is complete. No slot was ever named for the missing band, and the sequence `0002` · `0003` · `0004` · `0005` skips no number because the band never entered it.

**The sentence was corrected in place and the correction is printed beside it. Nothing was silently rewritten.** The reviewer did not raise this one; it was found while verifying Finding 1, and it is left in the open because it is the kind of slip that sends the next phase looking in the wrong directory.

## 0V19L.8 THE STATE OF THE DISK AFTER THIS REPAIR

**Dispatch order, replayed against `scripts/novel_runner.sh`'s own loop:**

| order | phase | state |
|---|---|---|
| — | `workspace/volume-19/batch-0002/` … `batch-0005/`, `plan-0001/` | `.done`, skipped |
| **1** | **`workspace/volume-19/batch-0003-gap/`** | **no `.done` — selected next** |
| 2 | `workspace/volume-19/close-0006/` | completes with this commit's phase |
| 3 | `workspace/volume-20/plan-0001/` | reached only after the band and the re-close |

**The gap band is dispatched first. The volume 20 planner is not reached until `921`–`930` exist and volume 19 has been closed again over fifty chapters.**

**Files changed by this repair:**

- `reviews/volume-19/batch-0006-close-0V19J.md` — `§0V19J.12` added; one sentence at `§0V19J.0` corrected in place
- `state/` — six files, one added sentence each
- `workspace/volume-20/plan-0001/PROMPT.md` — correction block inserted; one misattribution amended
- `workspace/volume-19/batch-0004/`, `workspace/volume-19/plan-0001/` — completion markers written
- `workspace/volume-19/batch-0003-gap/PROMPT.md` — created

**Files deliberately not changed:** everything under `chapters/`; `scripts/`; `.github/workflows/`; `.opencode/agent/`; `AGENTS.md`; `PHASE_SYSTEM.md`; `REPO_PLAN.md`; `OUTLINE_GUIDE.md`; `opencode.json`; `state/phase-ledger.json`; `outline/series.md`; `outline/ending.md`; `outline/volume-19.md`; and the historical receipts behind this one.

## 0V19L.9 WHAT THE NEXT PHASE OWES

**Ten chapters, `921`–`930`, in one band, with two off-mornings, one anchor, no head count, no account written down, no third asking, and the standing offer unanswered on all ten mornings.**

**Nobody is asked twice so that the second time comes out different.**