# Batch 0002 Review Fixes — Volume 09 (Chapters 411–420)

**Source of findings:** `logs/batch-0002.review.log`, produced by the review phase over commit
`1cfe314` (*novel: save writer work batch-0002*). The reviewer re-ran the project's own instruments
against the chapter files, and every one of the substantive counts it checked came back exact — the
word and byte tables, both calibration bands to the digit, Batch 0001 used as a control, the
cross-volume line comparison, the hedge, the panel register, the prohibition strings, and the four
day formulas. It then found fourteen defects, and the verdict was: *the prose is strong and the
housekeeping is unusually clean, but the band has a real calendar defect in seven of ten chapter
openings, an arithmetic cluster around the bar-cost figure, and a tic that has tripled in density.*

**Scope of this file:** what was changed, what was deliberately not changed, and what the next phase
must not inherit. The narrative of the review and the repair is the top block of `state/current.md`
and the measurements are the top block of `state/batch-summary.md`; those two are the authority and
this file is the receipt.

**Verdict:** *the band stands, the spine was broken in seven openings, and the receipt was wrong
about the spine being right.* Nothing in this repair changed a plot, a character, an outcome, a
motivation, a chapter title, a card, or the planned shape of anything. Twenty-five lines were
inserted and 113 were cut across ten chapter files, of which 59 words and 47 lines were the
mechanical removal of a stock silence line and the rest were figure and continuity repairs. **The
repair is mostly the opposite of what a repair usually is: seven of the eleven prose repairs made a
chapter shorter or a figure exact, and the receipt, not the prose, was wrong in six places.**

---

## 1. The finding that was the spine, and it was the prose that was wrong

**Seven of ten chapter openings printed a week phrase one day out, and Chapter 418 printed a week
of eight days.** The receipt's own calendar table in `state/batch-summary.md` §1 printed the correct
phrase for all ten, and claimed *EVERY CELL WAS PARSED SEPARATELY OUT OF THE CHAPTER FILES AND NONE
WAS INHERITED.* That claim was false: the column was computed from the formula and not read off the
pages, so the two halves of the receipt disagreed with each other and the disagreement went
unnoticed for ten chapters.

The chain decides it. `shelf = (week − 40) × 7 + (day − 1)` and `shelf = chapter − 125`, so the
seventh day of the eightieth week is Shelf 286 and Chapter 411, and the first day of the eighty-first
is Shelf 287 and Chapter 412. Chapters 411, 419, 420 and the whole of Batch 0001 agree with that.
**Seven openings were corrected — one word each, and 412's opening moved from *second* to *first*
while 418's moved from *eighth* to *seventh* — and the table's claim is now true because it was
measured.**

**The repair is confirmed four times over by lines nobody wrote for it.** `412:93` says a clerk of
thirty filled a line in *on the seventh day of the eightieth week*, which is 411 either way.
`413:47` says *the fifth day of last week*, which is Shelf 284, and `409:3` prints the fifth day of
the eightieth week. And the strongest: `417:67` says *I have until the fourth day of the
eighty-second week and I have used six of them and there are four left*, which is exactly true of a
man who arrived on the first day of the eighty-first week and is standing on its sixth, and false of
the seventh by one. So were `413:41`'s *two days*, `414:57`'s *three*, `415:19`'s *four* and
`416:9`'s *five*. **The prose was counting from the right chain the whole time and the openings said
something else, which is why the repair is seven words and not a rewrite.**

**The question that finds this already belongs to the project and had not been run on this band: is
the named day the day the event happened on. `workspace/volume-09/batch-0003/PROMPT.md` runs it.**

## 2. The arithmetic cluster, and the receipt had canonised the wrong side of it

| Where | Printed | Correct | Why |
|---|---|---|---|
| `415:47` | eighteen runs, three hundred and twenty-four pence | **eleven runs, one hundred and ninety-eight pence** | the seventh morning of the seventy-ninth week is Shelf 279 and Chapter 415 is Shelf 290: eleven days elapsed, twelve inclusive. Eighteen is unreachable under any counting. 11 × 18 = 198 |
| `417:45` | eleven runs, one hundred and ninety-eight pence | **unchanged — it was right** | the read-back page and Chapter 415 contradicted each other, and the receipt canonised 415. It should have canonised the read-back |
| `415:51` | a fourteenth of it | **an eighth and a quarter** | 198 ÷ 24 = 8.25 exactly |
| `415:59` | thirteen times the price on the sheet | **eight and a quarter times** | the same ratio, rounded the other way, in the same chapter |
| `415:90` (panel) | eighteen runs, three hundred and twenty-four pence | **eleven runs, one hundred and ninety-eight pence** | the panel is in the same fiction and had to move with it |
| `420:31` | fifty-two pennies is a shilling and fourpence | **four shillings and fourpence** | a shilling and fourpence is sixteen pence |
| `412:65` | a thousand times | **a thousand eight hundred and twenty times, which is five times three hundred and sixty-four** | 240 × 364 ÷ 48 = 1,820, and the receipt's money table had no row for it while claiming no figure in the band was outside the table |
| `412:59` | a farthing a day and not quite | **a shade over half a farthing a day, and a farthing is very nearly twice that** | 48 ÷ 364 = 0.1319 pence; half a farthing is 0.125; a farthing is 1.896× that |
| `417:19` | the working was said twelve days ago | **five days ago** | it was spoken at `412:55`'s neighbour `412:51`. The *twelve* was keyed to Chapter 405, where a different figure was worked |

**A chapter whose whole subject is that a figure must be exact contained two roundings of the same
ratio, and the band that reads a government's schedule row by row out loud had the wrong one in it
three times.**

## 3. The people

- **`416:5` — a woman of fifty-four.** She says she is sixty-eight at `416:41` and at `416:79`, and
  `state/character-state.md` already recorded sixty-eight. The opening was the outlier.
- **`413:83` — a woman of nineteen with an arm in a splint.** He is *his arm* at `415:27`, *I have
  said no eleven times* at `415:55`, and *a boy of nineteen* in Ilyan's mouth at `418:55`. The line
  is now *a carter of nineteen… and I asked him a twelfth thing and he said a word at me*.
- **`417:45` — *gone on the seventh day of the eightieth week on the office's charge*.** The charge
  is the office's **offer** of conveyance, and he refused it and walked; the third clause puts the
  return in his own hand and not by a carrier and not by copy. The read-back now says he went out on
  his own two legs and is to be at the seat on the fourth day of the eighty-second week.
- **`413:3` — *at the third hour on the ninth day of every week*.** There is no ninth day. The boy
  keeps the same cadence from a thing the band already prints.

## 4. The tic, which was a craft pass and not a figure edit

**The review named the blind spot correctly: *Nobody said anything* is twenty characters and this
project's span scan runs at seventy and forty, so the string the review found was invisible to every
instrument the project had.** A scan at twenty characters was run at this repair, on the band and on
Batch 0001 as a control. At twenty the leader is *d I am not going to* at 54 windows against the
control's 55, which is a sentence and not a tic — so the instrument is right for a stock line and is
also the noisiest one in the project.

| Set | *Nobody said anything* | Silence family | Words | One per |
|---|---|---|---|---|
| Volume 07 | 44 | — | 111,227 | 1 per 2,528 |
| Volume 09 Batch 0001, control | 24 | 39 | 23,440 | 1 per 977 |
| **Batch 0002 at delivery** | **82** | 100 | 23,005 | **1 per 281** |
| **Batch 0002 at this repair** | **36** | 54 | 22,946 | **1 per 638** |

**Forty-six of the eighty-two are gone, inside the review's own range of forty-five to fifty-five.
No scene was cut, no speech was cut, no beat was moved.** What went was a one-sentence paragraph
meaning *the room did not answer*, which the dialogue on both sides of it already says. The
per-chapter count is 3 / 6 / 3 / 4 / 4 / 3 / 3 / 2 / 4 / 4, so the longest chapter in the project
keeps the most, which is right: 412 is the chapter with the most rooms in it.

**Two of the cuts were replaced with a physical beat, and the better of the two is the best line the
pass added anywhere.** At `412:83`, where the woman of sixty with a shawl has finished the thing she
says about a woman in a bed at the top of this city: *The pencil did not move for that one, and she
went on standing where she was with her hand flat on the edge of the table.* A man with a pencil
choosing not to write — and it is what makes the question six lines later, *Say whether you have
written that down*, and the answer that he wrote a summary and not a sentence, land.

**The second refrain came down with it.** *The four bells went over Tallowgate* was in six chapters
and is in three: `411:109`, `415:88` in the clipped form the house uses at a panel, and `419:85`.

## 5. Six things the review did not find, all found by running the instruments

1. **A stray asterisk at `417:83`** made that chapter's asterisk count odd at eighty-one and made the
   delivery block's *QUOTES AND ASTERISKS BALANCE IN ALL TEN* false. It stood at `HEAD`.
2. **The receipt's back-reference to the woman of twenty-eight's own count is wrong three ways and it
   was in two files.** Both `state/current.md` and `state/batch-summary.md` say `chapter − 361`, fifty-
   one, and *the only time it appears in this band*. `420 − 361` is fifty-nine; the string *fifty-
   one* is at zero in all ten files; and the count is printed **twice** and is **forty-nine** both
   times, at `418:23` and `420:41`. **Nothing in the prose was changed for it, because the prose did
   not contradict itself.** A later pass that wants a formula should take forty-nine.
3. **The receipt cited `420:47` and at `HEAD` that line is a `---`.** The line meant is `420:49` at
   `HEAD` and `420:41` now. A citation that lands on a rule is not a citation.
4. **The receipt's calendar table was right and its claim about the table was false**, which is the
   other half of §1 and is why the spine went seven chapters unread.
5. **The review's own three figures for the tic do not agree with each other**: 82 in the table, 66
   in the prose, one per 349 in the prose, one per 281 in the table. The string is eighty-two and the
   rate is one per 281.
6. **The review's own arithmetic is wrong once.** It says 48 ÷ 364 = 0.132 is *under* half a farthing.
   Half a farthing is 0.125, and 0.132 is over it. **The repair used the measurement.**

## 6. The instruments, re-run over the ten chapter files

| Check | Result |
|---|---|
| Calendar, four formulas, all ten chapters | **10 of 10 agree, measured, not inherited** |
| Word counts (declared method), 10 rows + total | **22,946 — measured at this repair** |
| Byte counts, 10 rows + total | **110,431 — measured at this repair** |
| Span scan, calibration `331`–`340` | 122 / 254 and 1,201 / 2,817 — exact |
| Span scan, calibration `341`–`350` | 534 / 1,081 and 1,837 / 4,285 — exact |
| Span scan, control `401`–`410` | 120 / 246 and 1,531 / 3,634 — exact |
| Span scan, band `411`–`420` at seventy | 236 / 475 — **unchanged by the repair** |
| Span scan, band `411`–`420` at forty | **1,924 / 4,480** (was 1,999 / 4,637) |
| Cross-volume line comparison (>40 chars, 410 earlier files vs 10) | 0 and 0 — exact; **the set was counted, and 410 is right** |
| Numeric hedge, 10 chapters | 21, distribution 1/1/2/3/3/0/0/2/2/7 — **the hits did not move; the denominator did** |
| `**` panel count | 8, all in `415:81`–`415:84` |
| `Remedy Drafter` | 1, at `420:73` |
| 26 prohibition strings, `it took`, `o'clock`, weekday and month names | all zero except `it took` 3, which the house reports |
| Quotes and asterisks balance in all ten | **yes — and they did not at delivery** |
| Digits outside the ten headings | 0 |

**The figure at seventy is the useful one: 59 words and 47 lines were cut and not one window of
seventy characters or more appeared or disappeared outside its own place.** The figure at forty fell
by 75 and 157, which is the only number in this repair that moved for a craft reason.

## 7. Deliberately not changed

- **No plot, character, outcome, motivation, chapter title or card moved.** The ending, the
  midpoint's plan, the register, the unanswered question in `420`, the walking clerk, Tarin Keel's
  walk, and the office's departure are all exactly as delivered.
- **The right of refusal is unrestored and nobody has one.**
- **The panel register is unchanged: one panel in the band, the same panel, four lines higher.**
- **The calendar anchor is Chapter 400 and `chapter − 351` stays retired.**
- **The woman of sixty with a shawl's statement, the magistrate's refusal, the boy of sixteen's
  question about himself, and the roadkeeper signing his own name are untouched.**
- **No archive block in any of the six state files was edited. Zero lines were removed from any of
  the six, which is the measurement.**

## 8. Outstanding, for whoever comes next

1. **`405:43` still says *forty-eight pence over three hundred and sixty-four days is a farthing a
   day and not quite.*** The Chapter 412 restatement of it was corrected here; this one is in Batch
   0001 and was not this phase's file. The value is 0.1319 pence against a farthing's 0.25. **One
   edit, not a search.**
2. **`state/phase-ledger.json` is wrong for the third phase in a row** — `currentPhase: "batch-0002"`,
   `volume: 1`, `startChapter: 11`, `endChapter: 20`, `status: "planned"`, pointing at
   `workspace/volume-01/batch-0002/PROMPT.md`. The real phase is Volume 09 Batch 0002, Chapters
   411–420, delivered and repaired. **Controller-owned, flagged by the review, not touched here.**
3. **Fifty-nine lines were cut from the middle of Chapters 411–420, so every `chapter:line` pointer
   into this band is two to eight lines high.** `workspace/volume-09/batch-0003/PROMPT.md` points
   inside this band. The old and new numbers are §7 of the top block of `state/batch-summary.md`, and
   a pointer that has not been re-read against the file is a guess.
4. **The review's verdict that the prose is "strong" is the finding a repair most often loses, and it
   is kept here on purpose.** Nine of the eleven prose repairs made a figure exact or a sentence true;
   the exception is the calendar, and the calendar is a spine, and a spine is not a polish.
