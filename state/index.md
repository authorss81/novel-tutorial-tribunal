# index

Where every chapter is, and where the next one goes.

## On disk

| volume | chapters | count |
|---|---|---|
| 1–20 | `0001`–`1000`, fifty to a volume | 1000 |
| 21 | `1001`–`1040` | 40 |
| **total** | | **1040** |

## The current volume

| band | chapters | state |
|---|---|---|
| 1 | `1001`–`1010` | written, reviewed |
| 2 | `1011`–`1020` | written, reviewed; the midpoint landed |
| 3 | `1021`–`1030` | written, reviewed |
| 4 | `1031`–`1040` | written, reviewed, repaired |
| 5 | `1041`–`1050` | **owed** — prompt at `workspace/volume-21/batch-0005/PROMPT.md` |

Volume 21 closes at `1050`, week 172 day 2, a Wednesday, on an off-morning.

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
| this volume | `outline/volume-21.md` |
| the band being written | `workspace/volume-21/batch-0005/PROMPT.md` |
| the work | `chapters/volume-21/` |

## Known disagreement, unresolved

`outline/series.md` and `outline/ending.md` end the book at chapter 850. The
manuscript is at 1040. Nobody has decided whether the outline moves or the book stops.
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

`reviews/volume-01/` … `reviews/volume-21/` hold per-batch receipts, moved state
blocks and the verification scripts used against earlier volumes.