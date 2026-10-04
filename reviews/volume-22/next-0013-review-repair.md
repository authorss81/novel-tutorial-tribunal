# Review repair — volume 22 plan and its band 1 prompt

Source: `logs/next-0013.review.log`. The phase under review was `next-0013`, a
**volume-planning phase**: it wrote `outline/volume-22.md`,
`workspace/volume-22/batch-0001/PROMPT.md` and eight state-file updates, and it wrote
no prose. Nothing was restarted. No plot moved, no event was rescheduled, no title
changed, no figure on a chapter changed, and neither of the two unresolved items the
plan carries — the two-hundred-chapter length disagreement and the Sera/System absence —
was touched or resolved.

**There is no volume 22 prose, so none of the twenty findings was a prose finding.**
Every repair was made inside the plan, the prompt or a state file, and every one of them
prints the rejected wording beside the accepted one so a later writer inherits the
correction and the reason together. The findings are also carried in the plan itself at
`outline/volume-22.md` §13.10–§13.13.

The reviewer certified the following, and this repair changed none of it: the calendar
in §4 (fully re-derived from `week = 40 + (ch−125)÷7`, `day = (ch−125) mod 7 + 1`, day 1
= Tuesday, all correct); the titles in §7 (the plan proposes none, which matches volumes
17–21 and the write-last rule); the structure of §0–§§16 against `OUTLINE_GUIDE.md`; the
absence of invented canon; every cited file and section resolving; and every age,
identity and spot-checked `CHAPTER:LINE`.

---

## CRITICAL

### C1. The plan ordered its own midpoint in a wording the plan forbids three times — fixed

`outline/volume-22.md` §7's band 2 card and §7's placement rule both put the volume's
midpoint **"in about nine people's hearing"**. §5.2, §9 and the band prompt each put
**any head count of people** at zero in any wording, *including `about nine`* and
including inside a quotation, and name **`about nine of them` — a figure of a landing,
not of people — as the only permitted substitute.**

A writer could not have satisfied both instructions. **This is the first file in the
manuscript to carry the prohibition and the instruction in the same document.**

Both occurrences now read *"in the hearing of a landing at its work and not in a room,
and no figure of how many people heard it is printed in any wording"* — the permitted
substitute's shape, used where a head count used to be. The withdrawn wording is printed
in both places and named withdrawn, and at §13.10.

**Inherited and not repaired here:** `outline/volume-21.md` §7 at `:271` and `:279`
carries the identical contradiction for the volume 21 midpoint. That file was not part of
this phase and is owed to whoever owns it. Recorded in `state/open-threads.md`.

### C2. §7's band 5 card put the name back on the wood — fixed

The card read *"and the name is still on the wood in the mouths and still wrong"* —
garbled, and the reversed canon fact the last four volumes exist to prevent. The name is
**not** on the wood and is in the mouths: `chapters/volume-21/chapter-1050.md:73`,
`chapter-1046.md:79`, `chapter-1047:71`, and §15 of this same plan.

Now reads *"and the name is not on the wood and is in the mouths, and it is still
wrong"*, with the withdrawn wording and the three chapter citations printed beside it, and
named at §13.10.

---

## MAJOR

### M1. §8 certified a figure of zero that is 29 — fixed

The §8 table reported **"relative named days of the banned class — 0"** inside a cell
headed *"the house figures that carry, measured by hand today on volume 21's fifty
chapters."* The measured figure is **29 across twelve chapters**, against **252, 274 and
184** for volumes 18, 19 and 20.

Re-derived here with the preserved instrument:

```
$ python3 reviews/volume-21/volume-21-close-weekdays-0V21L.py
  volume 18   851- 900  bare     =  252   in 46 chapters
  volume 19   901- 950  bare     =  274   in 38 chapters
  volume 20   951-1000  bare     =  184   in 42 chapters
  volume 21  1001-1050  bare     =   29   in 12 chapters
```

Every other cell of that row was re-counted by hand and **stands**: pipe-leading lines 0,
`**` 0, `citizen` 0, `Veyra` 0, `sorry`/`grateful`/`forgiven`/`redeemed`/`worth it` 0
each, months 0 case-sensitively and word-bounded, seasons 0. `testimony` was added at 0.

**Why this mattered and not just accuracy:** the class is banned in §5.2 and §9, so a
writer reading §8 was told to skip the hand-check that the count exists to force. §9's
zero for volume 22 is untouched — it is a figure *owed* and not printed — and the claim
about volume 21 is withdrawn.

### M2. §8's heading described provenance its own cells contradict — fixed

The heading said *"every figure in this section was taken by running the tool."* The rows
below it say in their own cells that the structural figures were counted **by hand**, and
that `batch-0001-structure.py` **hard-codes `volume-16`** so the volume 22 figure **could
not be run at all** and is owed to the first band. The heading now says that the
calibration column was run on each instrument's own calibration first, that the volume 21
column is a mix of run instruments and hand counts, and that each row says which it is.

### M3. §7's band 2 card named no week boundary and no anchor — fixed

`§4.2` puts **two** week boundaries (`1062`/`1063` and `1069`/`1070`) and **one** anchor
(`1067`, one hundred and twelve weeks, a Saturday) inside `1061`–`1070`. The card named
neither. Bands 1, 3 and 4 each state their boundary count and their anchors.
`outline/volume-21.md:388` records the cost of exactly this omission.

The card now reads **two boundaries, one anchor `1067`, two full banks (`1062` and
`1070`), one off-morning (`1066`)**, and all four verified by running the formula:

```
1062  shelf 937  week 173 day 7 (Mon) | 1063  174 day 1 (Tue)   boundary
1066  shelf 941  week 174 day 4 (Fri) | residue 2 on eight      off-morning
1067  shelf 942  week 174 day 5 (Sat) | fever 112 weeks         anchor
1068  shelf 943  week 174 day 6 (Sun) | residue 4               midpoint lands here or after
1069  shelf 944  week 174 day 7 (Mon) | 1070  175 day 1 (Tue)   boundary, full bank
```

### M4. The climax was ordered two ways — fixed

§1.5 ordered the second asking **"on a full bank"**; §7's band 5 card and §7's placement
rule ordered it **"on `1094` or after."** `1094` is the only full bank inside band 5, so
the two are one placement, not two. §1.5 now says so in full and §7 says *"`1094` is the
last full bank of the volume and the only one inside band 5, so §1.5's *on a full bank*
and this *on `1094` or after* are one placement."* A band that lands after `1094` is not
on a full bank and is not owed one.

### M5. §1.6's resolution did not parse and carried no instruction — fixed

The resolution read *"IT DOES NOT ANSWER THE WOMAN OF FORTY-FOUR'S QUESTION AND IS NOT
MEANT TO AND SHE SAYS SO IS NOT REQUIRED OF HER A SECOND TIME, AND NOBODY IS TO THANK
HIM."* There is no recoverable instruction in the middle clause. The operative rule was
orphaned two hundred lines away at §6.

It now reads *"her one question at `1000:53` is not answered and is not meant to be, she
may not be asked whether she is in it, nobody may tell her that nobody is answering her,
and she is not required to put it again and may not be asked to"* — the §6 rule, in the
place that owes it, with `1000:53` attached.

### M6. The band prompt had no reading list — fixed

`AGENTS.md` requires the series outline, the ending, the previous twenty chapters,
`state/character-state.md` and `state/batch-summary.md` before a batch. The prompt named
none of them, quoted none of the three refusals the band opens on, and never said what
`1051` opens on.

The prompt now opens with a **ten-item reading list in order** — `AGENTS.md`,
`NOVEL_SPEC.md`, `series.md` and `ending.md`, all of `outline/volume-22.md`, the volume 21
close record, `chapter-0992.md` for the shaft, `1046`/`1047`/`1048`/`1050` at their
lines, `1031`–`1050` then `1021`–`1030`, the five state files, and the last band prompt
— followed by **the three refusals as they were refused, at `1050:39`/`1050:43` and
`1047:47`, with the house sentence at `1050:49`**, and then **what `1051` opens on**,
including the sentence `1050` ends on so the writer can see what it may not finish.

### M7. The `gratitude` ruling was dropped from both new files — fixed

`state/continuity.md` carries the ruling of the review of band 5: **the nominal
*gratitude* is not the banned word *grateful*.** It stands at `chapter-1044.md:61` and
`chapter-1048.md:41`, both as negations, both were left standing on purpose, and it is
not to be re-opened and not to be *"fixed"*.

Both new files listed `grateful` at zero and said nothing about `gratitude`. A writer
sweeping `grateful` as a prefix hits both lines, both hits are correct, and nothing told
them so. Re-verified by hand:

```
$ grep -ow gratitude chapters/volume-21/*.md
chapters/volume-21/chapter-1044.md:61
chapters/volume-21/chapter-1048.md:41
```

The ruling is now in §5.2, in the prompt's prohibited-figures list and in its structural
sweep row, and restated in `state/continuity.md`'s volume 22 block so it survives a reset.

### M8. `testimony` was banned in one section and missing from the list — fixed

§3.3 bans the word for the house substance in a mouth; §5.2's banned-word list did not
contain it. The two disagreed, and a writer working from the list had no way to know.
`testimony` is now in the list and `0` is certified on volume 21. Both files updated.

### M9. The prompt told the writer a false thing about how the lead spells the offer — fixed

The arithmetic gate row said *"the man of thirty-one keeps spelling it **a hundred and
…** in his own mouth."* **He does not.**

```
$ sed -n '31p' chapters/volume-21/chapter-1050.md
"Four hundred and ninety-six days in this county, … the standing offer asked at the
 eight-hundredth is three hundred and fifty days old, which is one thousand and fifty
 less seven hundred. It is unanswered."

$ grep -rno "a hundred and [a-z]*" chapters/volume-21/
chapters/volume-21/chapter-1040.md:65:a hundred and eight
```

**One hit in fifty chapters, and it is not the offer.** At `1040:65` the phrase is *"ask
me whether a hundred and eight is a lot"* — the figure of his mistakes, not the offer.
Following the prompt would have introduced an error into a mouth that is right.

Run by hand, the class that actually trips the instrument is a **cardinal spelled against
an ordinal**: the calibration's five one-outs are the boy's days (`ch − 653`) and volume
21's fifty are all the `1+ch-722` gravel, which the instrument labels `ASKING` and which
is a man of fifty-four's mornings — the count of asking was spent at `947` and is a
different thing. **The offer is clean on both ranges.** §8 and the prompt now say this.

The claim is inherited from `workspace/volume-21/batch-0001/PROMPT.md:123` and
`workspace/volume-21/batch-0002/PROMPT.md:115`, which are not part of this phase.

### M10. The head-of-a-shaft prohibition was dropped while its permission stayed — fixed

`outline/volume-21.md` §11 carries a row for the eye at the head of the shaft, `992:57`,
which a woman of thirty-eight calls the only eye on that landing: **it may not be given a
depth, a grade, a length or a distance from any mouth, and it may not be walked to and it
may not be looked into.** Volume 22's §11 table omitted the row, and §5.1 kept
volume 21's blanket permission — *"a length, a notch, a split, a hole, **an eye**, a
wedge may be given"* — so a writer had the permission and not the prohibition.

The row is restored in §11 and §5.1's permission is narrowed to carry the prohibition
with it. The prompt's prohibited-figures list gains the same rule. `992` is in
`chapters/volume-20/`, which is worth knowing before looking for it.

### M11. The prompt had no craft guidance and no title guidance — fixed

The plan says *titles are written last, against the body* — a rule nobody could fail,
because nobody was told what to aim at. The volume 21 close had to cut **thirty** titles
of `1001`–`1030` from whole plot summaries of sixty-one to a hundred and thirty-two words
down to **two to six**, which is recorded at `reviews/volume-21/volume-21-close.md` §1.

The prompt now carries a **How to write the morning** section — make something happen; a
person may be wrong and the wrongness is theirs and nobody resolves a mouth afterwards;
vary the sentences around the ritual clause, which itself stays word for word; a closing
is a beat and not a status report and ten closings may not use one device twice; figures
are spoken inside a sentence somebody is already in, with `1050:31` named as the model;
and `1058`, the off-morning, is the hardest morning in the band because a morning with no
figure on it wants to be about that. It then carries **And the titles**, with the two-to-six
word rule, the five prohibitions, the three titles of volume 21 that legitimately carry a
count-word, and the test a title has to pass.

---

## MINOR, all verified and all fixed

| # | was | is | verified by |
|---|---|---|---|
| 1 | §2 item 4: broom-hour asked at `1050:38` | **`1050:39`**, with the working at `1050:43`; `1050:38` is a blank line | direct read of `chapter-1050.md` |
| 2 | §2 item 5: thanks forestalled at `1048:35` | **`1048:41`**; `1048:35` is *This does not answer my question* | direct read of `chapter-1048.md` |
| 3 | §0: "**eight** forbidden substitutions" at `ending.md:178`–`188` | **seven** — the range is seven bullets, `:182`–`:188` | line-numbered read |
| 4 | §9: the Arrangement is the previously seeded antagonist at `series.md:304` | `series.md:304` names the **First Witness**, absent from volumes 18–22; citation dropped and the prohibition restated on what is true | `series.md:304` read; error already recorded at `outline/volume-15-handoff.md:133` |
| 5 | prompt: dayrefs row omitted the instrument's own warning | now carries both of its warnings at `batch-0001-dayrefs.py:85`–`:91`, including *an empty sweep is not a clearance* | source read |
| 6 | prompt: table headed "the ten owed lines, **one per chapter**" | heading corrected; rows 1–3 are all owed by `1051` and rows 4–10 are band-wide, now said under the table | table read |
| 7 | prompt: *three sentences at `outline/volume-22.md` §2 item 12* | those sentences are at **`outline/volume-21.md:369`**; §2 item 12 carries the contradiction and not the reason — the three are now quoted in full | both files read |
| 8 | `state/character-state.md`: *Every name here was made in a mouth in an earlier chapter* printed twice, the second a run-on | printed once | file read |

---

## Gate

```
prose chapters of volume 22 on disk .............. 0 (chapters/volume-22/ does not exist)
chapters of volume 21 changed .................... 0
title lines changed ............................. 0
CHAPTER:LINE references that moved .............. 0
plot events moved or rescheduled ................ 0
new names, new words, new stages, new powers ..... 0
new final enemy ................................. 0
open items resolved that are not ours ........... 0
files edited .................................... outline/volume-22.md
                                               workspace/volume-22/batch-0001/PROMPT.md
                                               state/current.md  state/index.md
                                               state/continuity.md  state/batch-summary.md
                                               state/open-threads.md  state/character-state.md
                                               reviews/volume-22/next-0013-review-repair.md
controller files edited ......................... 0
```

**No chapter of any volume was opened for editing, because there was nothing to repair in
one and no repair in this pass was permitted to touch a chapter.** The exactly-one next
phase is unchanged: `workspace/volume-22/batch-0001/PROMPT.md`. No new next-phase
directory was created, and none should be — the repair is not a phase.

## Left open, deliberately

1. **The volume 21 plan carries both the head-count contradiction (C1) and the
   `series.md:304` mis-citation (minor 4).** Repaired in volume 22; unrepaired in
   `outline/volume-21.md` and `outline/volume-17.md`, which are not this phase's files.
   Recorded in `state/open-threads.md`.
2. **§1.5's derivation citation.** It reads *"derived from `ending.md:152` and
   `series.md:304`–`306`"*, and those are the founding-settlement chapter and the ending
   guardrails, neither of which concerns a broom. Reported, **not repaired**: the
   derivation is a claim about the shape of the book, not about a chapter, and rewriting
   it would be moving the plan's plot claim rather than fixing a defect. Recorded in
   `state/open-threads.md`.
3. **The two standing items are untouched.** The two-hundred-chapter length disagreement
   and the Sera/System absence were printed by this review, were declared not the
   writer's, and are still not the writer's. No file written in this repair resolves
   either, and no chapter is to be written to satisfy either.
4. **`state/phase-ledger.json` still reads `currentPhase: batch-0002`, volume 1,
   chapters 11–20** — stale since bootstrap. The reviewer flagged it and correctly declined
   to edit it; it is controller-owned and this repair did not touch it.