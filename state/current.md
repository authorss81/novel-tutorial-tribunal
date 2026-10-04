# current

Where the project stands after the volume 22 planning phase. This file holds the
live record only. Anything that belongs to a finished band lives in
`state/batch-summary.md`; anything long-form lives in `state/continuity.md`.

## Status

- **Novel:** *The Tutorial Tribunal* — Ilyan Vester, a legal fantasy in which every
  adventure is a bounded case about a real conflict, a real burden, and a remedy
  people have to live with afterward.
- **Current volume:** 22, *The Hour Not Lent*, chapters 1051–1100. **Planned and
  not open. No chapter of it is on disk.**
- **Bands written:** none. Band 1 (`1051`–`1060`) is planned in
  `outline/volume-22.md` §7 and its prompt is
  `workspace/volume-22/batch-0001/PROMPT.md` — the exactly-one next phase. Bands
  2–5 have no prompt on disk, and that is correct; each is written by the band
  before it.
- **Chapters on disk:** 1050, in 21 volumes of 50 each.
- **The close record:** `reviews/volume-21/volume-21-close.md`. Its §11 is the
  review of the close and what was repaired in it. The volume 22 plan is
  `outline/volume-22.md`; §0 of it carries the length disagreement and §13
  carries the findings, and neither is resolved here.

## The live record at chapter 1050

Carried unchanged out of volume 21, which is closed. The plan `outline/volume-22.md`
§2 lists all twelve carried items; the short form:

- The confirming was said out loud on `1041` by the woman who saws lengths, and it
  settles nothing: she confirmed a name and gave nothing, and the landing went on.
- The man of thirty-one asked the man who cannot read one question about the barrow on
  `1046`, and was refused to his face in the man's own words. Nobody told Barnaby Crove
  he was wrong and nobody told him he was right, and nobody shaped it for him after.
  Asking cost the asker something that is not printed and is not the answer.
- The ordinary form was said from the wall by the woman of forty-four on `1048`, who
  said first that it does not answer her question. Nobody thanked her, nobody asked her
  whether she is in it, and nobody told her nobody is answering her.
- The standing offer stands unanswered at three hundred and fifty days, asked on no
  morning of the band and answered on none and withdrawn on none.
- No hand went on that ash on any of the ten mornings, and no new name was put on
  anything. The name on the second length is still wrong.
- The account is incomplete and still in use. Nobody is relieved, forgiven or thanked.

### The two decisions this file does not make

- **Where the book ends.** `outline/series.md` gives approximately 850 chapters and
  `outline/ending.md` ends at 850; the manuscript is at 1050, two hundred past the
  ending its own outline specifies. Nobody has decided whether the outline moves or the
  book stops. Owned by whoever owns the outline.
- **The primary relationship and the System.** `outline/series.md` names Ilyan and Sera
  Quill as the primary slow-burn relationship and calls the System the premise. Volumes
  19, 20 and 21 do not contain the word *Sera*, and *System* stands at zero in volumes
  18 through 21. Owned by whoever owns the outline.

**Both were re-recorded, unresolved, by the volume 21 close with the same standing.
Neither is a writer's decision and no chapter is to be written to satisfy either.**

## What the volume 21 close changed on the page

- **Thirty titles, `1001`–`1030`,** cut from whole plot summaries of sixty to a hundred
  and thirty-two words each to two to six words, against the body, naming nothing and
  printing no figure. **No prose was touched by any of the thirty cuts.**
- **`1016:1`** cut from its seventy-six-word summary to *Another Mouth*. The close first
  gave the reason *a title in this volume prints no numeral*, which is not the rule; the
  rule is the five prohibitions of `outline/volume-21.md` §7, and *Another Mouth* passes
  them. The closing record also first said the title *had been* *A Second Mouth*, a
  wording that never reached disk in any commit. Both are corrected in the record.
- **`1010:21` and `1010:23`:** the gravel's spoken subtraction read *one thousand and
  nine* less seven hundred and twenty-two and then one, which is two hundred and
  eighty-eighth, against an ordinal of two hundred and eighty-ninth on the same page.
  Corrected to **one thousand and ten** in both places. The figure did not change and no
  `CHAPTER:LINE` in this repository moved. **These two lines are prose and the close prompt
  said not to touch prose; the deviation is named in the close record at §3.1a, with the
  rejected alternative and the reversible action.**
- **Five findings were recorded and deliberately not repaired**, with the reading and the
  reason in each: the palm figure written in two forms on `1026`, one duration given as
  *about three weeks* at `1010:45`, a count of times over a span at `1045:43`, the
  volume's twenty-nine bare relative named days measured against three certified volumes in
  front of it, and three titles of the fifty that carry a plain count-word.
- **`outline/volume-21.md` §4.1 is wrong in one sentence about the seven off-mornings'
  weekdays** and says the missing Thursday sat at `1018`, which is a Saturday on the
  plan's own formula. The chapters are right; the plan is wrong; nothing was repaired in
  a chapter for it.

## What the review of the close changed

`logs/close-0006.review.log` found eight defects, **all of them in the record and none in
the fifty chapters.** No chapter was restarted, no prose rewritten, no title changed, no
figure on a page changed and no plot moved. The record was repaired in the open and
`reviews/volume-21/volume-21-close.md` §11 carries the table. The four that change what a
later writer inherits:

1. **The calibration table in the close's §2.2 was wrong in three of its eight cells** and
   had no instrument behind it. It now names one —
   `reviews/volume-21/volume-21-close-weekdays-0V21L.py` — and the bare relative named days
   for volumes 18, 19 and 20 are **252, 274 and 184**, not the 224, 268 and 174 first
   printed. Volume 21's own twenty-nine across twelve chapters and the whole anchored
   column reproduced exactly and stand. **The conclusion did not weaken; the margin went
   from about six to nine times to about six to ten.**
2. **The close's proof that no prose had changed was false.** A gate reading
   `body-changed chapters: NONE` sat three lines above the disclosure of the two words
   that did change. The true gate is printed now: thirty title lines changed, two body
   lines changed, both at `1010`, twenty chapters untouched, zero references moved.
3. **The byte-identical refrain in §2.5 was cited as a contiguous run** `1038`–`1050` and
   does not stand byte-identical at `1039` or `1040`, where the sentence opens a longer
   speech on the same line. Corrected to `1038` and `1041`–`1050`; the count of eleven
   stands.
4. **The reference count in §5 was ambiguous.** Nineteen `CHAPTER:LINE` references are in
   the band 5 block and twenty are in the whole of `state/batch-summary.md`; the twentieth
   is `1045:43` in the close's own block. All twenty were re-verified.

## What the review of the volume 22 plan changed

`logs/next-0013.review.log` found **two critical, eleven major and seven minor defects in
the plan and the band prompt, and not one of them in prose** — there is no volume 22
prose to be wrong. **No chapter was restarted, none exists, no title changed, no figure on
a page changed and no plot moved.** Every repair was made inside the plan or the prompt and
each is printed in the open with the rejected wording beside it. The receipt is
`reviews/volume-22/next-0013-review-repair.md`; the findings are also carried at
`outline/volume-22.md` §13.10–§13.13.

**The two that would have misled the band 1 writer into writing a wrong chapter:**

1. **The plan forbade a head count of people three times and then ordered its own midpoint
   in one.** §7's band 2 card and §7's placement rule both said the midpoint is said *in
   about nine people's hearing*, while §5.2 and §9 put *about nine* in the banned class and
   name *about nine of them*, a figure of a landing, as the only permitted substitute. **No
   writer could have satisfied both.** The head count is out of both places. The same
   contradiction is inherited from `outline/volume-21.md` §7 and stands there, unrepaired,
   and is owed to whoever owns that file.
2. **The band 5 card put the name back on the wood.** It read *the name is still on the
   wood in the mouths and still wrong* — the reversed canon fact the last four volumes
   exist to prevent. It is *not* on the wood and is in the mouths. Corrected.

**The five a later writer would otherwise have inherited as false instructions:**

3. **§8 certified relative named days at `0` as measured by hand on volume 21.** The
   measured figure is **29 across twelve chapters**, against 252, 274 and 184 for volumes
   18, 19 and 20, and all four are the output of
   `reviews/volume-21/volume-21-close-weekdays-0V21L.py`. **The class is real, so §9's zero
   for volume 22 is a figure owed and not printed while the claim about volume 21 is
   withdrawn.** A band that believed the zero would have skipped the hand-check.
4. **§8's heading said every figure in it was taken by running the tool,** and the rows
   below say in their own cells that two were counted by hand and one could not be run at
   all. The heading now says which is which.
5. **The one-out arithmetic class was not the offer.** The prompt told the writer the man
   of thirty-one spells the offer *a hundred and —*. **He does not**: `chapter-1050.md:31`
   spells it *three hundred and fifty days old* in full, and a search for *a hundred and*
   across volume 21 returns one hit, `chapter-1040.md:65`, where it is *a hundred and
   eight* and that is his mistakes and not the offer. Hand-run, the calibration's five
   one-outs are the boy's days and volume 21's fifty are the `1+ch-722` gravel, which the
   instrument labels `ASKING` and which is a man of fifty-four's mornings.
6. **The band 2 card named no week boundary and no anchor** while §4.2 puts two boundaries
   (`1062`/`1063`, `1069`/`1070`) and one anchor (`1067`) inside `1061`–`1070`. Bands 1, 3
   and 4 each stated their counts. `outline/volume-21.md:388` records the cost of that
   omission.
7. **The climax was ordered two ways** — *on a full bank* in §1.5 and *on `1094` or after*
   in §7 — and `1094` is the only full bank inside band 5, so the two are one placement.
   They now say so.

**And four smaller ones, each of which was a rule with no teeth:**

8. **§1.6's resolution did not parse** — *AND SHE SAYS SO IS NOT REQUIRED OF HER A SECOND
   TIME* — and carried no instruction; the operative rule was orphaned at §6 and is now
   where it is owed.
9. **The head of the shaft was dropped from §11** while §5.1 blanket-permitted *an eye* as
   a mouth figure, so a writer had the permission and not the prohibition: no depth, no
   grade, no length, no distance, not walked to, not looked into. Row restored, permission
   narrowed.
10. **The `gratitude` ruling was dropped from both new files.** `state/continuity.md`
    carries it: the nominal is not the banned word *grateful*, it stands at `1044:61` and
    `1048:41` as negations, both were left standing on purpose, and it is not to be
    re-opened or *fixed*. A writer sweeping `grateful` as a prefix hits both lines and both
    are correct.
11. **The band prompt had no reading list and no craft or title guidance.** It named
    `AGENTS.md`'s requirements nowhere, quoted none of the three refusals the band opens on,
    and never said what `1051` opens on. It now has a ten-item reading list, the three
    refusals as they were refused, the opening, a *How to write the morning* section, and
    the house title rule — **two to six words, thirty titles cut from sixty-one to a
    hundred and thirty-two words at the volume 21 close.**

**And the four citations that were pointing at nothing:** `1050:38` is a blank line and the
broom-hour is at `1050:39` with its working at `1050:43`; `1048:35` is *this does not
answer my question* and the forestall of thanks is at `1048:41`; `ending.md:178`–`188` is
**seven** forbidden substitutions and not eight; `series.md:304` names the **First Witness**
and not the Arrangement, and the error was already recorded at
`outline/volume-15-handoff.md:133`. `testimony` was banned in §3.3 and missing from §5.2's
list, so the two places disagreed.

## Archive

Pre-reset state blocks, review receipts and verification scripts are under
`reviews/volume-01/` … `reviews/volume-22/`. They are evidence, not live state. The
repair passes for bands 4 and 5 are written up in
`reviews/volume-21/batch-0005-review-repair.md` and
`reviews/volume-21/batch-0006-review-repair.md`, the close is
`reviews/volume-21/volume-21-close.md`, the instrument its weekday figures come from
is `reviews/volume-21/volume-21-close-weekdays-0V21L.py`, and the repair of the volume 22
plan and its band prompt is `reviews/volume-22/next-0013-review-repair.md`.
