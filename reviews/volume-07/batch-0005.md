# Batch 0005 Review Fixes — Volume 07 (Chapters 341–350)

**Source of findings:** `logs/batch-0005.review.log`, produced by the Batch 0005 reviewer.
**Scope of this file:** what was changed against the chapter files and the state files, what was
deliberately not changed, and what the next phase must not inherit. The narrative of the review and
the repair is §11 of the top block of `state/current.md`, which is the authority; this file is the
receipt.

**Reviewer's own closing sentence:** *the volume-close prompt is the blocker — create it and drop the
combined `volume-08/plan-0001` file, then correct §3.7's method or drop its numbers. Everything else
is cosmetic.* The first half was right. The second half was not, and understating it was how this
project has twice now shipped a state layer that flatters its own prose.

**Reviewer's verdict on the prose, in its own words:** it re-ran the band's instruments, found word
count, hedge rate, the board chain, the figure-in-words discipline, the morning ordinals, the digit
discipline, the month-word discipline and all the prohibited strings reproducing exactly, and
concluded that the prose is sound and the record of the prose is not. **Both halves of that are
carried forward below, and the second half turned out to be worse than it looked.**

---

## The two high findings

| # | Finding | Action |
|---|---|---|
| 1 | The next-phase artifact was the wrong phase. Volume 07 is complete — fifty chapter files, `outline/volume-07.md:78` ends the volume at 341–350, the top of `state/current.md` says so — and both `AGENTS.md` and `PHASE_SYSTEM.md:151` require exactly one **volume-close** prompt. The band wrote `workspace/volume-08/plan-0001/PROMPT.md`, whose own first line asks one run to plan a fifty-chapter volume *and* write its first ten chapters, and skipped the phase that would author `outline/volume-08.md`, which does not exist. | **Fixed.** `workspace/volume-08/` is deleted. `workspace/volume-07/volume-close/PROMPT.md` is the next phase, in the shape `workspace/volume-05/volume-close/PROMPT.md` used. Measured after the change, the two directories carrying no marker are `workspace/volume-07/batch-0005` and `workspace/volume-07/volume-close`, and the dispatcher takes the first in `sort` order, so the close runs next and sorts ahead of anything in `volume-08` if one is ever created. |
| 2 | `state/phase-ledger.json` is six volumes stale **and the dispatcher trusts it**, which would make self-dispatch re-run a phase that finished long ago. | **The first half is true and is not mine to fix; the second half is false and it matters.** The ledger does read `currentPhase: batch-0002`, Volume 01, `planned`, and it is controller-owned, and it is recorded at `state/current.md` §11.2 and not edited. But `scripts/novel_runner.sh:26-40` selects by `find workspace -name PROMPT.md -type f \| sort` and takes the first directory with no `.done`, `.blocked` or `.retired` marker, and `grep -rn "phase-ledger" scripts/ .github/` returns nothing. The ledger is inert. This was already measured at `state/index.md` machinery items 1 and 7; the reviewer restated the earlier claim without reading item 7. |

**And a third defect of the same class, which neither the reviewer nor the band found, and which is
the one with teeth.** Two directories carried no marker after the batch: `volume-07/batch-0005` and
`volume-08/plan-0001`. The dispatcher takes the first in `sort` order, so it would have marked this
batch done and then run the *plan-and-write* prompt — leaving `volume-07/volume-close` unmarked
behind it, and the volume's close record unwritten until after Volume 08's first ten chapters were
on disk. This is the failure `state/index.md` machinery item 1 records having already happened once,
when a state file named a next phase for six phases that had never existed on disk — except that
this time the file existed and was the wrong job. **A volume-close prompt must sort ahead of any
prompt for the volume it closes, and it does.**

---

## The medium finding, and the two figures underneath it

**`state/current.md` §3.7 declared half a method.** It said *take every window of exactly k characters
at every position* — a sliding window — and then printed figures a sliding window cannot produce: a
sliding window over these ten files returns 101,093 positions at k=70 and 111,447 at k=40. The
block also contradicted itself in the same section, declaring **20 distinct / 20 occurrences** at
seventy characters while stating in the next paragraph that the offending sentence is *printed at both
ends* of Chapter 342, which makes occurrences exceed distinct and makes 20/20 impossible.

**The missing half of the method was recovered by calibration against the four earlier bands**, and
it reproduces **all eight** of their published figures exactly — 331–340 at 122/254 and 1,198/2,810,
and 163, 144, 235 at k=70 with 1,351, 796, 876 at k=40. The method is: strip the heading, normalise
whitespace, take every window of exactly *k* characters at every position **within each chapter
separately**, and **keep only the windows that occur more than once**.

**The recovered method then said something the block said the opposite of:**

| k | as first written | as delivered |
|---|---|---|
| 70 | 700 distinct / 1,489 occurrences | **533 / 1,079** |
| 40 | 2,069 distinct / 4,903 occurrences | **1,836 / 4,282** |

The block called twenty *the lowest figure in the project at either threshold* and called the band a
trajectory. **The true figure was 700 at seventy characters, the worst of the five bands, and the
band went up at both thresholds against the band before it.** §3.7 now carries the whole method, both
columns, and the withdrawal of the trajectory claim.

**And two more figures were wrong, in the same direction, which nobody found and which the repair
measured rather than inherited:**

- **§3.13, the word *nine*.** Printed as 135 for this band and 163 for the one before. Measured: **177
  after the repair, 176 before it, and 184 for 331–340.** The sentence those two numbers supported —
  *all three habits fell together for the first time in this project* — is withdrawn as unsupported.
  The measured five-band series is 157 / 171 / 217 / 184 / 177.
- **§3.14, the cross-band total.** Printed as 777 in 110,963 words, one in every 145. Measured:
  **552 in 111,227 words, one in every 201** — and 552 *is* the sum of §3.12's own five-band row, so
  the block contradicted itself about the number it was going to be the record of. §3.12's word count
  and rate were corrected to 21,681 and one in 452.
- **§3.12's undeclared clock.** Printed as *about four hundred instances across fifty chapters*.
  Measured: **184**, of which 172 are `at about the <ordinal> hour` and 40 are the literal *about the
  seventh hour*.

---

## The low findings

- **The opening frame was a formula, and that was the same finding as the span scan.** Seven of ten
  chapters open by saying why there is no figure. That is the place rule at
  `chapters/volume-07/chapter-0316.md:7` and it is not negotiable — but the frame had been written as
  a formula: **344 and 346 opened with 132 characters word for word identical, 345, 347, 349 and 350
  shared a seventy-character window, 349 and 350 shared an eighty-nine-character prefix, and three
  chapters copied the sentence *The day came to four bells and nothing whatever on top of them,
  which is four* out of Chapter 341 verbatim.** **Fixed in prose**: six openings rewritten and two
  weight sentences varied, with every fact kept — the distance, the ladder, the woman of forty-one,
  the second light, the leg, the reason a stroke does not travel — the day's own total still printed
  in words in all ten chapters, the figure still in three of ten, and no plot touched. The band now
  has **no band-wide repeated sentence of forty-five characters or more** and the worst shared prefix
  between any two openings is 70 characters, which is the three chapters that print a figure sharing
  the declared device with each other. **Batch 0004's review left this device at seven of ten and
  recorded why; this repair kept the device and cut the formula, which is the difference between the
  two. The ceiling is now written down at §1.5.**
- **Tense slip at `chapter-0346.md:25`**, *she counts* inside narration that has *had a wash and a
  child and an hour`. **Fixed**: *she counted*, with the two general clauses either side left in the
  habitual present, which is the book's standing register for a rule. **The parallel case at
  `chapter-0343.md:81`** — *the round goes round … nobody knows yet where that is* — **was looked at
  and left**, because it is a rule stated in the general and not a slip, exactly as at `346:43`, so
  changing it would have cost the book its register and bought nothing.
- **Unlogged beat tic.** *it took N seconds* and its relatives stand **seventeen** times across the
  band, by chapter 3/1/3/0/1/3/0/2/1/3, of which five are the exact form
  *it took [a person] [a number] seconds*. §3.12 logged the undeclared clock and not this.
  **Recorded at §3.12 and not cut** — cutting seventeen instances by hand is the move that corrupted
  six files once already at §7.10. **The finding under the finding: a band that declares fifteen
  instruments clean has declared itself clean on the instruments it built, which is the standing
  lesson at `state/index.md` machinery item 1 and the first time this project has written it about
  itself.**
- **`reviews/` has no `volume-05` or `volume-06` directory and `volume-01` is missing batches 0002
  and 0004.** **Left alone, deliberately.** A phase may not write a review into a directory it did not
  review from; that is the Volume 05 close's own rule and it is correct. Each of those is its own
  phase and nothing in this repair is owed one.

---

## Every instrument re-run over the ten chapter files after the repair

| Instrument | Result |
|---|---|
| Weekday, plural-safe | **0** |
| Month-word | 24 raw, 24 modal *may*, **net 0** |
| `**` marks and panels | **0 / 0** |
| `[0-9]` | 30, three per file, all ten the chapter number in the heading |
| Four- and five-digit numerals | **0** |
| Board figure in words | **3** — `341`, `343`, `348`. `sixty-five thousand`: **0** |
| Day-phrase sweep, three alternatives | **7** (unchanged) |
| Day-phrase sweep, fourth form | **0** |
| Prohibited strings | `cannot read`, `first witness`, `system`, `panel`, `Remedy Drafter`, `stage`, `would like`, `the reader`, `anchor`, `vault\|cave\|ruin\|temple\|battlefield`, uppercase `CORRECT` — all **0**. `correct` in any case: 3, all ordinary English |
| Meta sweep, wider pattern | **0** |
| Span scan, k=70 | **533** distinct, 1,079 occurrences (was 700 / 1,489) |
| Span scan, k=40 | **1,836** distinct, 4,282 occurrences (was 2,069 / 4,903) |
| Band-wide repeated sentence, 45+ chars | **0** (was 1) |
| Words, method of §3.12 | **21,681** (was 21,663) |
| Numeric hedge | **48**, by chapter 1/5/3/6/5/4/4/6/5/9, one in every 451 |
| Undeclared `about the <ord> <unit>` | **40** |
| Italic spans | **49** |
| *Man of thirty-one* | **0** |
| *Nine* | **177** |
| `it took` | **17**, of which the exact *it took … seconds* form is **5** |

**The board chain was not touched and still closes from 64,091 in both directions: the ten own rings
are 4 / 7 / 8 / 6 / 11 / 4 / 7 / 12 / 4 / 8, they sum to 71, 64,083 is Chapter 340's morning, and
64,091 + 71 = 64,154 + 8 = 64,162, which is Chapter 351's morning.**

---

## What was deliberately not changed

- **No planned plot moved.** The porch still burns, the seventh is still physically gone, the bell
  network is still a replacement and not a repair, the man with the cart is still on the list he did
  not agree to, the two missing positions are still missing, the hundredth morning is still noticed
  by nobody, and the question about the basin and the town is still asked once and unanswered. The
  ending's held cards are untouched and no new antagonist or power was introduced.
- **No archive block was edited.** Every state-file change is inside the top block, per
  `outline/volume-07.md:212` item 15.
- **No earlier band was re-written.** The canon split on the barwoman's age — *about fifty* at
  `276:58`, `297:31`, `302:3`, `322:77` against *about thirty-four* at `308:3`, `319:57`, `320:59` —
  is real, predates this band, and stays open for the volume close. It is carried at §8.14 and a
  Volume 08 card must not name her age without naming which chapter.
- **The barwoman is still a person in a record.** She is mentioned and not asked for anything, in no
  chapter of the band, and nobody thanked her and nobody is going to.
- **`state/phase-ledger.json` was not touched**, and the reason it does not matter is now recorded
  with a line number instead of an assertion.
- **The span scan's 533 is not presented as a success.** A long tail of two-instance overlaps at
  21,681 words is what stock country-vocabulary produces, and 122 — the figure the previous band
  reached — was measured in a shorter book. The close is told so at §8.5 and in the next phase's
  prompt, because a band that reads 533 as a fall has been had by the same mechanism that printed
  twenty.

---

## The one sentence a later pass needs

**The band was good and its record of itself was not, and every figure the review could not reproduce
was wrong in the direction that flattered the prose.** Three of the four wrong figures — the span
scan, the count of *nine*, and the cross-band total — were in sections whose stated purpose is to let
a later pass re-run the instrument and get the same number. §3.7 now can. **The fourth, the ledger,
was wrong in a state file's account of the controller, and the controller is four lines long and
should have been opened instead of believed.**
