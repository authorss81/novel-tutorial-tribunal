# index

Where every chapter is, and where the next one goes.

## On disk

| volume | chapters | count |
|---|---|---|
| 1–21 | `0001`–`1050`, fifty to a volume | 1050 |
| 22 | `1051`–`1100` | 0 — planned, not open |

## The current volume

Volume 22, *The Hour Not Lent*, is planned in `outline/volume-22.md`. No band is
written. Band 1 (`1051`–`1060`) is the owed next phase; bands 2–5 have no prompt
on disk.

## Where the next chapter goes

`workspace/volume-22/batch-0001/PROMPT.md` — volume 22 band 1, chapters
`1051`–`1060`. That is the exactly-one next phase. **The manuscript still owes
no chapter until that phase writes one.** The length disagreement
(`outline/volume-22.md` §0: seventeen volumes and chapter `850` against 1050 on
disk) is carried as an open item into the band prompt and is not resolved by
planning. `state/phase-ledger.json` still reads `batch-0002`, volume 1; it is
controller-owned and was not edited, so this section is the designation until
the controller corrects it. The self-dispatch workflow still chooses which phase
runs — this section is what it would be choosing.

## What each state file is for

| file | holds |
|---|---|
| `state/current.md` | the live record: where the book stands, and the two decisions that are not the writer's |
| `state/batch-summary.md` | what each band did, what it left, what it owes |
| `state/chapter-summaries.md` | a chapter a piece for the current volume, a band a line for the rest |
| `state/continuity.md` | calendar, counters, water ladder, places, objects, house rules |
| `state/character-state.md` | the cast, with what each one wants, refused and gave |
| `state/open-threads.md` | what is open, what is owed, and what is spent |

**Keep these six compact.** They were reset on the review of band 4 after they grew to
373 KB of self-measurement and pointer bookkeeping. Pre-reset blocks are under
`reviews/volume-*/` and are evidence, not live state.

## Where the authority for the book lives

| question | file |
|---|---|
| the shape of the whole book | `outline/series.md` |
| how it ends, and what stays open | `outline/ending.md` |
| this volume, planned | `outline/volume-22.md` |
| what the review of that plan repaired | `reviews/volume-22/next-0013-review-repair.md` |
| volume 21, closed | `reviews/volume-21/volume-21-close.md` |
| the review of that close, and its eight repairs | `reviews/volume-21/volume-21-close.md` §11 |
| the weekday figures the close certifies | `reviews/volume-21/volume-21-close-weekdays-0V21L.py` |
| the phase before the volume 22 plan | `workspace/continuation/next-0013/PROMPT.md` |
| the volume 22 plan's first batch | `workspace/volume-22/batch-0001/PROMPT.md` |
| the work | `chapters/volume-21/` |

## Known disagreement, unresolved

`outline/series.md` and `outline/ending.md` end the book at chapter 850. The
manuscript is at 1050. Nobody has decided whether the outline moves or the book stops.
It is recorded here and in `state/current.md` because every batch re-reports it and it
is not a writer's decision to make.

## Older block identifiers

The state files used to carry numbered blocks — `§0V…`, `§1A…`, `§2…` — and
several outlines and older band prompts cite them, for example `outline/volume-21.md`
§0 pointing at `state/open-threads.md` §1AP3. **Those anchors no longer exist.** The
reset kept the story and dropped the scheme, so a citation of that kind now resolves
to nothing. This is stated here rather than papered over: the blocks that had already
been moved out are whole under `reviews/volume-*/`, and anything that was live in
`state/*.md` at the reset is whole in that commit. Rewriting the citations is a
housekeeping pass of its own and has not been done.

## Archive

`reviews/volume-01/` … `reviews/volume-22/` hold per-batch receipts, moved state
blocks and the verification scripts used against earlier volumes. Volume 22's holds one
file: the repair of its own plan, which is not a batch receipt because no batch has run.
