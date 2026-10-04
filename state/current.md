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

## Archive

Pre-reset state blocks, review receipts and verification scripts are under
`reviews/volume-01/` … `reviews/volume-21/`. They are evidence, not live state. The
repair passes for bands 4 and 5 are written up in
`reviews/volume-21/batch-0005-review-repair.md` and
`reviews/volume-21/batch-0006-review-repair.md`, the close is
`reviews/volume-21/volume-21-close.md`, and the instrument its weekday figures come from
is `reviews/volume-21/volume-21-close-weekdays-0V21L.py`.
