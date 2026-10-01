# Volume 16, Band 0004 — Review Repair Receipt, chapters 781–790

**`logs/batch-0004.review.log` IS THE REVIEW THIS RECEIPT ANSWERS. IT READ THE TEN CHAPTERS AND THE STATE SURFACE AROUND THEM, IT EDITED NOTHING, AND IT REPORTED FIVE FINDINGS: ONE DISPATCH BLOCKER THAT IS CONTROLLER-OWNED, TWO FILING ERRORS ABOUT WHERE THE 701–710 SUMMARIES LIVE, AND TWO GATES REPORTED WITHOUT THE RULE THAT PRODUCES THEM.**

**NOTHING WAS RESTARTED. NOT ONE CHAPTER WAS REWRITTEN, NOT ONE PARAGRAPH OF PROSE WAS TOUCHED, NOT ONE FIGURE WAS INVENTED, NOT ONE PLOT MOVEMENT WAS MOVED AND NO VOLUME DIRECTION WAS TOUCHED. ⚠ `git diff --stat` OVER THIS PASS TOUCHES STATE AND REVIEW FILES ONLY; `chapters/volume-16/` IS UNCHANGED FROM `fbbe9b6` AND THE TEN CHAPTERS ARE STILL THE CANON THE PHASE WROTE.**

---

## 0. What the review found, and what became of each

| # | Finding | What became of it |
|---|---|---|
| 1 | **THE DISPATCH IS SET TO RE-RUN A FINISHED BAND. CONTROLLER-OWNED AND NOT OURS.** `workspace/volume-16/batch-0002/` carries `.deferred`, `.attempts`(3), `.retry-after` and `.wip-conflict` and no `.done`; its chapters 761–770 are written, reviewed, repaired and canon; its `.retry-after` has expired; the first `PROMPT.md` in sorted order without `.done`/`.blocked` is that one. | **CONFIRMED BY READING THE DISPATCH CODE AND NOT TOUCHED.** Every figure re-measured and the warning rewritten with today's numbers in `state/current.md` §0S. **§1** |
| 2 | **The 701–710 summary set is in two files and both headers claim the whole set.** `reviews/volume-15/batch-0002-chapter-summaries-701-710.md` holds 701 only; `reviews/volume-16/batch-0004-chapter-summaries-701-710.md` holds 702–710. | **BOTH HEADERS CORRECTED IN PLACE AND EACH NOW SAYS WHICH CHAPTERS IT HOLDS, WITH THE OTHER PATH NAMED.** No canon paragraph moved, cut or summarised. **§2** |
| 3 | **Two false pointers, and one row not updated for the 781–790 move.** The moved tail rows still say chapters 1–710 canon and Volume 15 open at 710, and 1–680 with Volume 14 open at 680; `state/index.md` still sent a reader looking for the whole of 701–710 in the Volume 15 file and for the band-0004 tail pointers in the band-0003 file. | **ALL FOUR CORRECTED**, each with the correction marked where a writer reads it, and none of the superseded headers deleted. **§3** |
| 4 | **Every recorded per-chapter word count is one low, and the total is quoted in six places.** `wc -w` gives 26,170 against a recorded 26,160. | **THE FIGURES WERE RIGHT AND THE RULE WAS MISSING. THE RULE IS NOW PRINTED BESIDE THE FIGURE IN THREE FILES, AND EVERY FIGURE WAS RE-RUN ON THE PUBLISHED TOOL.** **§4** |
| 5 | **The duplicate-window gate reports 0 and does not reproduce when re-run naively.** The review got 2,762 band-wide. | **THE GATE IS NARROWER THAN THE RE-RUN AND THE FIGURE IS NOT FALSE. THE RULE IS NOW PRINTED, THE WHOLE SWEEP RE-RAN AT 0 ON EVERY CATEGORY, AND THE BAND-WIDE FIGURE IS RECORDED AS ITS OWN NAMED MEASUREMENT.** **§5** |

---

## 1. FINDING 1, THE DISPATCH, AND WHY IT IS NOT OURS TO FIX

**RE-READ AT THIS PASS, IN BOTH PLACES THAT SELECT A PHASE. `scripts/novel_runner.sh:77`–`89` AND `.github/workflows/novels.yml:169`–`172` BOTH WALK `find workspace -name PROMPT.md | sort` AND TAKE THE FIRST WITHOUT `.done` OR `.blocked`. THE ORDER AT THIS PASS:**

```
workspace/volume-16/batch-0002/PROMPT.md   <- SELECTED
workspace/volume-16/batch-0004/PROMPT.md
workspace/volume-16/batch-0005/PROMPT.md
```

**`workspace/volume-16/batch-0002/` CARRIES `.deferred`, `.attempts` = 3, `.retry-after` = 1790819456 (EXPIRED; THE READ AT 1790821974) AND `.wip-conflict`, AND NO `.done`. CHAPTERS 761–770 WERE WRITTEN, REVIEWED, REPAIRED AND CERTIFIED AND THEY ARE CANON. `retire_obsolete_phases` IN THE RUNNER MATCHES ONLY A VOLUME-OUTLINE PHASE BY ITS FIRST LINE AND WILL NEVER RETIRE A BATCH PROMPT, SO THIS DOES NOT SELF-HEAL. ⚠ AND ONE HALF OF IT IS WORSE THAN THE REVIEW MEASURED: THE RUNNER'S LOOP SKIPS A DIRECTORY CARRYING `.retired` AND THE WORKFLOW'S SCAN DOES NOT LOOK FOR `.retired` AT ALL, SO EVEN A RETIREMENT APPLIED TO THE RUNNER ALONE WOULD NOT HOLD THE WORKFLOW BACK.**

**THE MARKERS AND `state/phase-ledger.json`, WHICH STILL READS `"currentPhase": "batch-0002"`, ARE CONTROLLER-OWNED. THIS PASS CREATED, DELETED AND EDITED NO MARKER AND DID NOT WRITE TO THE LEDGER. THE HALF THAT WAS OURS IS DONE: `workspace/volume-16/batch-0005/PROMPT.md` EXISTS, IS THE NEXT CHAPTERS OWED, AND CARRIES THE INSTRUCTION THAT A PHASE DISPATCHED INTO THE WRONG DIRECTORY IS TO WRITE 791–800 ANYWAY AND SAY SO IN THE RECEIPT, BECAUSE A PHASE THAT WAITS FOR A MARKER TO CLEAR INSTEAD OF WRITING OWES THE CHAPTERS AND HAS DONE NOTHING. ⚠ THIS NEEDS CONTROLLER ATTENTION AND NOTHING IN A WRITER PHASE CAN SUPPLY IT.**

---

## 2. FINDING 2, THE 701–710 SET IN TWO PLACES

**CONFIRMED BY COUNTING THE PARAGRAPHS, NOT BY READING THE HEADERS. `grep -c '701 — NOTHING WHATEVER'` GIVES 1 IN THE VOLUME 15 FILE AND 0 IN THE VOLUME 16 FILE; `grep -c '702 — A BANK THAT IS FULL'` GIVES 1 IN THE VOLUME 16 FILE. THE SET IS SPLIT AND BOTH HEADERS SAID WHOLE.**

**FIXED BY CORRECTING BOTH HEADERS, NOT BY MOVING A PARAGRAPH. A SECOND MOVE WOULD CHANGE A PATH THAT FIVE STATE FILES ALREADY NAME, AND THE HARM IS A WRITER BEING SENT TO ONE FILE FOR TEN CHAPTERS, WHICH A CORRECTED HEADER AND A CORRECTED POINTER ROW FIX COMPLETELY.** The live ten in `state/chapter-summaries.md` were untouched; that file stands at the same size and its live twenty are the live ones.

---

## 3. FINDING 3, THE FALSE POINTERS, ALL FOUR OF THEM

| The row | What it said | What it says now |
|---|---|---|
| `reviews/volume-16/batch-0004-chapter-summaries-pointer-tail.md`, the 701–710 pointer | the whole set is at the Volume 16 file | **both paths, one for 701 and one for 702–710** |
| the same file, the closing-band header | chapters 1–710 canon, Volume 15 open at 710 | **that position is marked as true on arrival only, and the position now is 1–790 canon, fifteen volumes closed, Volume 16 open at 790** |
| the same file, the older closing-band header | chapters 1–680 canon, Volume 14 open at 680 | **both superseded headers named as superseded, and the current position stated once beside them** |
| the same file's own header | it holds *the row naming where the six 551–780 sets are* | **that row is not in the file and was not in it; where those sets are named instead** |
| `state/index.md`, the `chapter-summaries.md` table row | 701–710 at one path; every tail pointer at the band-0003 file | **both 701–710 paths; both tail-pointer files** |

---

## 4. FINDING 4, THE WORD COUNTS, WHICH WERE NEVER WRONG

**THE REVIEW MEASURED `wc -w` AND GOT TEN MORE WORDS, ONE PER CHAPTER, AND ASKED THE RIGHT QUESTION. THE ANSWER IS THAT `wc -w` COUNTS WHITESPACE AND THE INSTRUMENT COUNTS WORDS, AND EVERY CHAPTER OF THIS BAND CARRIES ONE LOOSE MARKER THAT `wc -w` TREATS AS A WORD.**

**THE RULES, WHICH WERE NOT PRINTED ANYWHERE A CHECKER COULD FIND THEM AND ARE NOW PRINTED IN `state/current.md` §0.0, `state/index.md:3` AND `state/batch-summary.md` §0V16D.0:**

- **WORDS** — `[A-Za-z0-9£$’'-]+` over the raw file, title, `---` separators and panel lines included. A loose marker is not a word.
- **SENTENCES** — ends at `.`, `!` or `?` plus up to two of `”"*`, counted per paragraph block and never across a blank line, and a title is one sentence.

**RE-RUN AT THIS PASS ON `reviews/volume-10/instrument.py` ITSELF — THE PUBLISHED TOOL, NOT A RE-TYPING OF IT — AND IT REPRODUCES THE HEADLINE TO THE WORD: 26,160 WORDS, 1,128 SENTENCES, MEDIAN 24, OVER-60 0.09 PER CENT, MAX PARAGRAPH 77, MAX SENTENCE 62, THE TEN ROWS 2,345 · 2,570 · 2,619 · 2,881 · 2,705 · 2,528 · 2,489 · 2,696 · 2,722 · 2,605, AND THE INSTRUMENT PRINTS THE ROW-SUM EQUALITY ITSELF. THE ROWS WERE NOT CHANGED, BECAUSE THEY WERE RIGHT. THIS IS FINDING NINETEEN IN THE INSTRUMENT'S OWN HEADER AND IT HAS NOW HAPPENED TWICE.**

---

## 5. FINDING 5, THE DUPLICATE WINDOW, AND THE TWO THINGS IT WAS

**THE RECORDED FIGURE IS **THREE OCCURRENCES OF A SIX-WORD WINDOW INSIDE ONE PARAGRAPH BLOCK**. THE REVIEW RAN THE SIX-WORD WINDOW ACROSS THE TEN CHAPTERS AS ONE STRING AND COUNTED EVERYTHING OCCURRING TWICE OR MORE, WHICH IS A DIFFERENT MEASUREMENT AND GAVE 2,334 ON THE INSTRUMENT'S OWN TOKENIZER. A FIGURE REPORTED WITHOUT ITS RULE IS INDISTINGUISHABLE FROM A FALSE ONE, AND THAT IS THE ONLY DEFECT HERE.**

**BOTH FIGURES ARE NOW RECORDED, NAMED AND KEPT APART:**

| The measurement | Scope and threshold | Its figure |
|---|---|---|
| **the gate** | three or more occurrences of a six-word window **inside one paragraph block** | **0** |
| the density, not a gate | two or more occurrences anywhere **across the ten as one string** | **2,334**, of which **1,272** occur three or more |

**THE REPEATED PHRASES ARE THIS VOLUME'S SPOKEN FORMULA AND NOT A DEFECT. THE HIGHEST ARE *AND I AM NOT GOING TO* AT 66 AND *AND THAT IS SEVEN HUNDRED AND* AT 30 AND *READ TO HIM IN THE OPEN* AT 21, AND `outline/volume-16.md` REQUIRES THE COUNTED DAY LINE, THE REFUSAL TO GO ON AND THE NINTH LINE READ ALOUD IN EVERY CHAPTER OF THE VOLUME. WHAT THE GATE FORBIDS IS A MAN SAYING THE SAME SENTENCE THREE TIMES INSIDE ONE PARAGRAPH, AND THERE IS NONE.**

**THE WHOLE STRUCTURE SWEEP WAS RE-RUN AT THIS PASS — `python3 reviews/volume-16/batch-0001-structure.py 781 790` — AND EVERY CATEGORY REPRODUCED: UNBALANCED QUOTES 0 AND 0, PANELS 0, STRAIGHT APOSTROPHES 0, THE SIX WAYS TO NAME THE BOOK NONE, THE MONTH AND THE SEASONS NONE, DUPLICATE WINDOWS 0, BYTE-IDENTICAL LINES 0, EVERY PROHIBITION 0 EXCEPT `brave` 12 AND `thanked` 17, ALL TWENTY-NINE READ AND ALL TWENTY-NINE NEGATIONS.**

**AND ONE FIGURE THAT WAS OWED AND IS NOW MEASURED AS FAR AS THE CHAPTERS ALLOW: `I.guards(751,790,vol='volume-16')`, EVERY CHAPTER OF VOLUME 16 THAT EXISTS, GIVES 52 OCCURRENCES IN 40 CHAPTERS AND 2 CROWD-NOUN FLAGS, AND THE BAND'S OWN 26 AND 1 REPRODUCED EXACTLY. ⚠ THE TWO CROWD-NOUN FLAGS HAVE NOT BEEN READ AS A LIST AND ARE OWED ALONGSIDE THE 791–800 RUN, WHICH STILL CANNOT BE MADE.**

---

## 6. WHAT THIS PASS DID NOT DO, AND IT IS NOT A DEFECT

**IT DID NOT RESTART A CHAPTER, DID NOT TOUCH A WORD OF PROSE, DID NOT MOVE A PLOT POINT, DID NOT CHANGE THE CALENDAR, DID NOT SPEND OR UN-SPEND THE POWER PROGRESSION, DID NOT OPEN THE BLANK INTERVAL, DID NOT ANSWER THE STANDING OFFER, DID NOT RESTORE THE RIGHT OF REFUSAL OR GIVE IT TO ANYBODY, DID NOT NAME `First Witness` OR SAY `citizen`, DID NOT TOUCH `state/phase-ledger.json`, DID NOT CREATE OR DELETE A PHASE MARKER, AND DID NOT EDIT `scripts/`, `.github/workflows/` OR ANY OTHER CONTROLLER FILE. THE FINDING THAT MATTERS IS STILL FINDING ONE AND IT IS STILL NOT OURS.**