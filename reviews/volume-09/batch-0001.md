# Batch 0001 Review Fixes — Volume 09 (Chapters 401–410)

**Source of findings:** `logs/batch-0001.review.log`, produced by the review phase over commit
`9d90c42` (*novel: save writer work batch-0001*). The reviewer re-ran the project's own instruments
against the chapter files instead of reading the band's numbers, and the batch figures it did not
challenge came back exact.

**Scope of this file:** what was changed, what was deliberately not changed, and what the next
phase must not inherit. The narrative of the review and the repair is the top block of
`state/current.md`, which is the authority; this file is the receipt.

**Verdict:** *the band stands and the record of the band was wrong in five places.* Nothing in this
repair changed a plot, a character, an outcome, a motivation, a chapter title, a card, or the
planned shape of anything. One word count and one set size were re-measured and written in five
places, and no chapter was opened for writing.

---

## 1. The first finding, which the review raised

**`state/batch-summary.md` printed Chapter 406 at 2,331 words and the band at 23,459. Measured, 406
is 2,312 and the band is 23,440.** The house's declared method — `len(re.findall(r"[A-Za-z’'\-]+",
text))` over the whole file — was applied to all ten chapter files and **nine of the ten rows
reproduce to the word.** The tenth is nineteen out, which is the size of error a figure typed from a
whitespace-token count leaves, and 406 is the panel chapter.

| Ch | Printed at delivery | Measured at this repair |
|---|---|---|
| 401 | 2,641 | 2,641 |
| 402 | 2,564 | 2,564 |
| 403 | 2,559 | 2,559 |
| 404 | 2,227 | 2,227 |
| 405 | 2,220 | 2,220 |
| **406** | **2,331** | **2,312** |
| 407 | 2,048 | 2,048 |
| 408 | 2,046 | 2,046 |
| 409 | 2,288 | 2,288 |
| 410 | 2,535 | 2,535 |
| **TOTAL** | **23,459** | **23,440** |

**The hedge did not move.** The declared pattern re-ran and still returns **fifteen** hits — 401
one, 402 three, 405 two, 406 two, 409 one, 410 six. Only the rate changed, because fifteen into
23,440 is one in 1,563 and not one in 1,564. The byte column was not touched and all ten byte rows
reproduce.

## 2. The second finding, which the review repeated from the band instead of counting

**The cross-volume line comparison named its own set and the set was two files short, in two
places.** `state/batch-summary.md` §2 said *the three hundred and ninety-eight earlier chapter
files*; `state/current.md` §1 of the band said *all three hundred and ninety-eight others*. The
project has **410** chapter files and ten of them are this band, so the set is **400**.

**The result is unchanged and is zero and zero, re-run at this repair against all four hundred:**
no line over forty characters is duplicated anywhere in the band, and none in the band appears in
any of the four hundred others, in either direction. But a comparison that misses two files can
still return zero, and the zero is not the finding — the size of the set is. This is the same defect
as the word count one level up: a figure describing the instrument rather than the result, carried
forward instead of counted. **The review's own verification table reports the comparison "against
the other 398 chapter files" — it reproduced the band's figure instead of counting the files.**

The `398` in a chapter number, in a measured span figure such as `199 / 398`, and in a count of the
word *nine* are none of them this finding, and none was touched.

## 3. The five edits, in place, in the live blocks

All five are in live top blocks. The corrections are named in the superseding block at the top of
`state/current.md`, so the blocks they sit in are now archive and are not byte-identical to what the
band wrote.

| § | Before | After |
|---|---|---|
| `batch-summary` 7, row 406 | `\| 406 \| 10,938 \| 2,331 \| 281 \| 156 \| 6 \| 123 \| 8 \|` | `\| 406 \| 10,938 \| 2,312 \| 281 \| 156 \| 6 \| 123 \| 8 \|` |
| `batch-summary` 7, total | `**110,939** \| **23,459**` | `**110,939** \| **23,440**` |
| `batch-summary` 4, hedge rate | **FIFTEEN IN 23,459 WORDS, ONE IN 1,564** | **FIFTEEN IN 23,440 WORDS, ONE IN 1,563** |
| `batch-summary` 2, set size | *the three hundred and ninety-eight earlier chapter files* | *the four hundred earlier chapter files* |
| `current` 1, set size | *all three hundred and ninety-eight others* | *all four hundred others* |

The first three replacements are digit-for-digit the same length, so `state/batch-summary.md` grew
only by the fourth edit.

**Why the disagreement survived a whole phase:** `state/current.md` §6 of the band printed
23,440 and 1,563 — the correct pair — and `workspace/volume-09/batch-0002/PROMPT.md:77` prints
23,440 and 1,563 too, because the prompt was built from the receipt and not from the table. The bad
number was never going to reach the next band. It was also never going to be *noticed*, which is the
worse half. The string `23,459` occurred twice in the repository and `2,331` once, all three in
`state/batch-summary.md`; no outline file, no other state file and no review file carried either.

## 4. What reproduced, and was not touched

Every one of these was re-run at this repair, not read out of the band's receipt, and every one came
back exact, so none of them was edited.

| Claim | Measured |
|---|---|
| Duplicate windows @70 = 120/246, @40 = 1,531/3,634 | exact |
| Calibration `331`–`340`: 122/254, 1,201/2,817 | exact |
| Calibration `341`–`350`: 534/1,081, 1,837/4,285 | exact |
| No line >40 chars duplicated in band, or against the other 400 files | 0 / 0 |
| Twenty-six prohibition strings (`arbiter`, `system`, `panel`, `stone`, `March`, …) | all 0 |
| Day formulas `ch−125` / `ch−250` / `ch−283` / `ch−400`, all ten chapters | all ten |
| Panel register: one panel, four fields, ≤1 per ten chapters | `406:85`–`406:88`, 8 `**` |
| `Remedy Drafter` ×1, in narration, in nobody's mouth | `410:81` |
| Undeclared clock ×1, inside the declared hour vocabulary | `406:83` |
| Band bytes, and all ten byte rows | 110,939 |
| §6's manuscript column: 5,634,397 in 410 files, and the band inside it | exact, and not touched |
| `**` count and the twenty-one odd lines in `state/batch-summary.md` | 3,461 and 21, both pre-dating and both unchanged at the same line numbers |

## 5. What was deliberately not changed

1. **`state/phase-ledger.json` reads `currentPhase: batch-0002`, volume 1, chapters 11–20, and has
   not been touched in 172 commits.** The file is controller-owned and this phase did not open it.
   The review also found the risk underneath it and it is real: **the ledger's phase ids are global
   while the workspace paths are per-volume, so this phase's commit is `batch-0001` in Volume 09
   while the ledger's `batch-0001` is Volume 1, chapters 1 to 10, done.** Any dispatch that resolves
   the next phase by id reads eight volumes wrong. It should be corrected, with the id collision, by
   whoever owns the file.
2. **`reviews/` holds volumes 01, 02, 03, 04, 07 and 08, and nothing for 05 or 06.** Those two look
   dropped rather than intentional. This phase did not write them, because a review of a batch that
   was not read is a fabrication.
3. **No chapter file was opened for writing.** `find chapters -name '*.md' | wc -l` is 410 and the
   manuscript is 5,634,397 bytes, both measured at this repair and both identical to the band. The
   prose was already right.
4. **`state/continuity.md`, `state/character-state.md`, `state/open-threads.md` and
   `state/chapter-summaries.md` were not touched**, because none of the four carried either figure.

## 6. What this repair added, against the ceiling it set itself

Measured by added lines against `9d90c42`: `state/current.md` **+48 / −1** and **+10,507 bytes**;
`state/batch-summary.md` **+4 / −4** and **−18 bytes**. Total added 52 lines, total removed 5.

The first three table edits are byte-neutral because the digits are the same length; the fourth
shortens the sentence, which is why `state/batch-summary.md` nets eighteen bytes *down* while adding
a line. Its `**` count and its twenty-one odd lines are unchanged at the same line numbers, which is
pre-dating and was not touched.

`state/current.md` is the only file this repair grows and **+10,507 is under the twelve-thousand
ceiling** the project sets on itself, by 1,493. This receipt is the third file and is new; its own
size is counted in lines rather than bytes so that the sentence counting it cannot change it.

**THE SIX STATE FILES NOW STAND AT 5,602,016 AGAINST THE SAME 5,634,397, WHICH IS 0.9943, against
0.9924 at the band.** §6 of the band's receipt measured the moment the band was written and is not
edited; a later reading of that column is a different measurement and not a discrepancy, and it is
printed here rather than described.

## 7. What the next phase must not inherit

**Do not trust a figure in a table because a receipt above it says the method. Re-run it.** This band
had a bad figure in one table, the correct figure in the receipt above it, and the correct figure
already copied into its own successor prompt — and the disagreement was still there at review.

**Count the set as well as the result.** The second finding is a comparison that skipped two files
and still returned zero, and a review is exactly the place where a set size gets copied instead of
counted. A figure that describes the instrument is not a smaller claim than one that describes the
result; it is the same failure one level up.

**Do not touch `state/phase-ledger.json`, and do not mark any phase directory.** The marker and the
ledger are the controller's, and no phase in this project writes its own.

**The band itself is unchanged and stands:** the rail across the Low Road, the three people who
could do something about the eleven yards of it and cannot see each other, the empty register at
`405:51`, the panel spent at `406:85` and never chosen out of, the woman of twenty-eight's name at
the top of a line, and the road coming down at the fourth hour from a room four hundred miles off.
Nothing in this repair touches any of it, and the finding is not restated here.
