# Batch 0005 — review repair

**THE REVIEW OF BATCH 0005 FOUND NINE FINDINGS. SIX ARE REPAIRED IN THE CHAPTERS OR THE STATE FILES, ONE IS A FALSE POSITIVE AND IS RECORDED AND NOT REPAIRED, AND TWO ARE CONTROLLER-LEVEL AND ARE RECORDED HERE AND NOT TOUCHED. NO CHAPTER WAS RESTARTED, NO PLOT WAS CHANGED, NO MONEY FIGURE MOVED, NO DATE LINE MOVED AND NO CLOSING FEVER MOVED.**

**THE BAND'S OWN CERTIFICATION WAS EXACT. `python3 -c "import sys;sys.path.insert(0,'reviews/volume-10');import instrument as I;I.run(541,550,vol='volume-11')"` on the committed files reproduced every figure in `state/batch-summary.md` §0 line for line, including the per-chapter row and all four refrain figures. **THE WEAKNESS WAS NOT THE MEASUREMENT AND IT WAS THE REPAIR PASS BEHIND IT, WHICH FIXED EIGHT INTERVAL STRINGS AND ONE VENUE WITHOUT CHECKING THREE THINGS THE SAME RULE GOVERNS.**

## 1. What the review pass got wrong, and what it cost to check

**THE REVIEW REPORTED THAT `chapter-0546.md:135` — *that is the same thing I said to a man from a town four days off in a porch a fortnight ago* — CONTRADICTS *twenty-four days ago* AT LINES 95 AND 103. IT DOES NOT, AND IT WAS NOT REPAIRED, BECAUSE IT IS NOT A CONTRADICTION.**

Lines 95 and 103 are about **a lane** and about **a woman of about seventy**, and the lane is at `522`, which is twenty-four days before `546`. Line 135 is about **a porch** and about **a man of thirty-four from a town four days off**, and that porch is at `531`, which is fourteen days before `546`. `546 − 531 = 14`, and a fortnight is fourteen days exactly. The same chapter already uses *a fortnight* twice for its own fourteen days, at the first asking and at the standing-in-the-porch exchange. **THE REPAIR TO THAT LINE FROM *three weeks* TO *a fortnight* WAS CORRECT AND STANDS.**

**A FIGURE THAT IS RIGHT ABOUT ONE THING AND READ AS THOUGH IT WERE ABOUT ANOTHER IS FINDING ELEVEN PAYING A SECOND TIME IN ONE REVIEW, AND THE CURE IS THE DERIVATION AND NOT THE EDIT. THE RULE THIS REPAIR APPLIES IS THE ONE `state/index.md` LINE 11 ALREADY CARRIES: A READER WHO CHECKS THE COUNT FINDS IT TRUE.**

## 2. Repaired in the chapters — four edits, three chapters

1. **A COUNT IN A TITLE AGAINST ITS OWN BODY. `chapter-0546.md`.** The title read *Two People And One Afternoon*. The body read *two people and one afternoon each* (line 87), *two afternoons* (line 99) and *two people and two afternoons* (line 147). `outline/volume-11.md` §5: *a number in a title is checked the way a date line is checked*. **THE CHAPTER WAS RIGHT AND THE TITLE WAS WRONG.** The count at `522` is *one woman and one name and one afternoon*; the count at `546` is two people and two afternoons; the count at `549` is two people and **three** afternoons, because the woman of about seventy is asked a second time in between. The title now reads **Two Afternoons**, and the sequence 1 → 2 → 3 now holds across three chapters.
2. **AN ATTRIBUTION THE VENUE REPAIR DID NOT CARRY WITH IT. `chapter-0548.md:141`.** A weaver of sixty-two said *I said in a kitchen at Kiln Row three days ago that a page says what was done*. The sentence is spoken at `545:73` by **a boy of about nineteen**. The interval and the venue were right and the speaker was not checked. The line now reads *And a boy of about nineteen said in a kitchen at Kiln Row three days ago…*, which keeps the place, the interval and the argument and gives the sentence to the person who said it.
3. **A CLOSING LINE THAT WAS NOT CATALOGUED. `chapter-0547.md`, last paragraph.** The checkpoint replaced the volume's climax close with a new paragraph that dropped the refusal the chapter's own title promises and ended on a clause in which *last* appeared twice. **THE PARAGRAPH NOW KEEPS THE NEW BEAT AND THE TITLE'S BEAT: *Not one of the nine lines is in a book, and a man of thirty-one asked for the list to be entered before it was read out and was refused in a market square in about four seconds.*** The refusal survives in the body at lines 25, 181 and 187 and in the title, so nothing was lost by the earlier edit and nothing is lost by this one. No scene moved and no other line of the chapter was touched.
4. **ONE MORE VAGUE UNIT OF THE CLASS ALREADY REPAIRED EIGHT TIMES. `chapter-0547.md:175`.** A narration said the man from four days off had said his thing *three times in four weeks*. The three occasions are `531`, `533` and `547`, which is **sixteen days**, and `550:165` prints the same fact from the same first occasion as **nineteen days**. It is sixteen days now, and the two chapters agree about one man in one span of time.

**NOTHING ELSE WAS OPENED. NO DIALOGUE WAS REWRITTEN, NO SCENE WAS MOVED, NO CHARACTER WAS CHANGED, AND THE FIVE OUTLINE FIXED LINES ARE UNTOUCHED.**

## 3. Repaired in the state files and the next prompt

| Where | What was wrong | What it is now |
|---|---|---|
| `state/batch-summary.md` §0 header | *27,689 words*; said the volume is open at 540, that §0 is Batch 0004, and labelled two different files `§0M` | 27,673 words; volume written and closed at 550; §0 is Batch 0005; §0B1–§0B4 are the four moved blocks |
| `state/batch-summary.md` §0.1 | *SIXTEEN sentences over sixty words, FOURTEEN of them the ten titles and THREE dialogue lines … the figure is 2.79%* — 14 ≠ 10, 14 + 3 ≠ 16, and 2.78% of 1,186 is about 33 | **THIRTY-THREE**, split **TEN titles / NINE dialogue lines / FOURTEEN narration**, counted and not estimated, and 2.78% |
| `state/batch-summary.md` §0.2 | `151.1` per 10k for the dialogue rate | `151.0` |
| `state/batch-summary.md` §0.3 | *the five weeks and three weeks named at `547`* — there is no three weeks left in `547` | *the five weeks and the nineteen days named at `547`* |
| `state/current.md` §0.6 item 16 | *two people and three afternoons* for `546` | **two** afternoons |
| `state/current.md` §0.3a | one bullet asserted the sentence *was spoken by a boy of about nineteen* and *is the weaver's* in the same line | split into two bullets, and the speaker is now recorded as repaired |
| `state/chapter-summaries.md` 546 | *three afternoons*; *a lane four weeks ago* | **two** afternoons; **twenty-four days ago** |
| `state/chapter-summaries.md` 547 | described a close the chapter no longer had | records the refusal close and says it is the beat the title promises |
| `state/character-state.md` | the woman of about seventy gave the same reason *in a lane four weeks ago* | **twenty-seven days ago**; `three afternoons` there is right and stands |
| `state/open-threads.md` | *a widow of sixty-eight who said no in a lane three weeks ago* | **at her own door on the upper row sixteen days ago**, which is `523` → `539`, and the chapter says sixteen days in her own mouth |
| `workspace/volume-11/volume-close/PROMPT.md` | hard-coded **27,643 / 1,181 / 2.79%** and a dialogue rate of **151.3** | **27,673 / 1,185 / 2.78%** and **151.0**, with the superseded figures named and the line-start figure (399 at 144.2) printed beside it |

**THE LAST ROW MATTERS MOST. THE PROMPT WAS WRITTEN BEFORE THE CHECKPOINT REPAIR AND WAS NEVER UPDATED, SO THE NEXT PHASE OPENED BY COMPARING ITSELF AGAINST NUMBERS KNOWN TO BE WRONG — THE EXACT FAILURE ITS OWN §1 WARNS ABOUT. THE DIALOGUE RATE CARRIED THREE DIFFERENT VALUES ACROSS THE REPOSITORY AND NOW CARRIES ONE.**

## 4. Re-measured after every edit

`python3 -c "import sys;sys.path.insert(0,'reviews/volume-10');import instrument as I;I.run(541,550,vol='volume-11')"`

**27,673 words · 1,185 sentences · median 19 (gate ≤ 25) · over-60 2.78% (gate ≤ 10%) · max para 113 (gate ≈ 120) · max sent 136.** Row sums to 27,673 and the band total is 27,673.
541 2498/110/2.73%/79/44 · 542 2779/120/4.17%/93/43 · 543 2716/117/3.42%/105/39 · 544 2761/109/2.75%/113/37 · 545 2140/88/3.41%/90/28 · 546 2616/118/0.85%/97/42 · 547 3134/136/5.15%/103/56 · 548 2685/120/0.83%/95/50 · 549 2846/114/3.51%/81/34 · 550 3498/153/1.31%/104/45.

Refrains 61 / 0 / 0 / 418 at **151.0 per 10k**, and 399 at line starts at **144.2**, and the larger is the certified one. Tics and meta sweeps at 0, `thanked` 53 and all fifty-three read and all negations, silence 10 (3.6/10k), chorus 0, `said nothing` 16 (5.8/10k), no panel.

**THE TEN DATE LINES WERE RE-READ ONE BY ONE AFTER THE EDITS AND ALL TEN STILL AGREE FIELD BY FIELD WITH `outline/volume-11.md` §2'S FORMULA AND WITH EACH OTHER'S CLOSING FEVER: 541 99/4 · 542 99/5 · 543 99/6 · 544 99/7 · 545 100/1 · 546 100/2 · 547 100/3 · 548 100/4 · 549 100/5 · 550 100/6; mornings 291–300; settlement 141–150; fevers 36w 6d – 38w 1d. THE GUARD WAS RE-SWEPT ACROSS ALL FIFTY CHAPTERS AND STILL PRINTS 157 OCCURRENCES, ALL READ.**

**THE ONE CHAPTER-LENGTH FIGURE THAT MOVED IS `547`, 3,154 → 3,134, AND IT IS STILL THE SECOND-LONGEST CHAPTER OF THE VOLUME. `550` IS STILL NINETY-EIGHT WORDS OVER THE 3,400 CEILING AND THAT IS STILL A RECORDED FIGURE AND NOT A CUT SCENE.**

## 5. Recorded and not touched, because the phase prompt does not own them

1. **`workspace/volume-11/batch-0005/` carries BOTH `.checkpoint` AND `.done`**, and batches 0001–0004 carry only `.done`. The controller may read this batch as resumable. **A MARKER FILE IS NOT A FICTION, SUMMARY, CONTINUITY, CHARACTER OR OPEN-THREAD FILE AND WAS NOT DELETED.**
2. **`reviews/volume-10/__pycache__/instrument.cpython-312.pyc` IS TRACKED IN GIT** although `__pycache__/` and `*.pyc` are in `.gitignore`, because gitignore does not apply to a tracked file. It appears as a binary diff inside a fiction commit. Fixing it is `git rm --cached` at the controller's hand and not this phase's.
3. **`state/phase-ledger.json` still reads `currentPhase: batch-0002`, volume 1**, while the manuscript is at volume 11, band 5. That file is owned by the workflow and is not edited here.
4. **THE CARD FOR `549` IN `workspace/volume-11/batch-0005/PROMPT.md` SAYS *a Saturday three weeks ago*** for a striking that is thirty-five days before and is printed as *five weeks* at `549:105`. The card was paid for in the chapter and the correction is recorded at `state/current.md` §0.3, which is this repository's standing practice: **a card claim is recorded, not edited.**
5. **`outline/volume-11.md` §2's RANGE COLUMN IS WRONG FOR THE FIFTH BAND RUNNING** (`99 / 6 – 101 / 4 | Mon–Wed` and a `38w 0d` upper bound, where the formula gives `99 / 4` Friday to `100 / 6` Sunday and `38w 1d`). **THE OUTLINE WAS NOT REPAIRED MID-BAND, BECAUSE A BAND THAT RE-PLANS AN OUTLINE MID-BAND HAS RE-PLANNED A CARD, AND THE REPAIR IS OWED IN THE CLOSE, WHICH IS WHERE NO BAND IS RUNNING AND WHERE THE CLOSE PROMPT ALREADY ASKS FOR IT.**

## 6. What this pass is actually about

**THE REPAIR PASS THAT FIXES COUNTS IS THE ONE THAT BREAKS PROSE, AND THE PASS THAT BREAKS PROSE IS THE ONE THAT LEAVES COUNTS STALE. EIGHT INTERVALS AND ONE VENUE WERE REPAIRED AND NOBODY OPENED THE TITLE OF THE CHAPTER THAT HAD BEEN REPAIRED, NOBODY ASKED WHO SPOKE THE SENTENCE THE VENUE HAD BEEN MOVED TO, AND NOBODY RE-RAN THE INSTRUMENT ON THE FILES THEY HAD JUST CHANGED — WHICH IS WHY A CERTIFICATION THAT MATCHED ITS OWN FIGURES STILL CONTAINED A STALE 2.79 PER CENT, A TITLE THAT SAID ONE AFTERNOON WHERE THE CHAPTER SAID TWO, AND A PROMPT FOR THE NEXT PHASE CARRYING NUMBERS NOBODY HAD MEASURED SINCE THE TEXT MOVED.**

**THE THREE CHECKS THAT WOULD HAVE CAUGHT ALL THREE ARE NOT A TOOL AND NOT AN INSTRUMENT. THEY ARE: OPEN THE TITLE OF EVERY CHAPTER YOU TOUCHED AND MAKE IT AGREE WITH ITS OWN BODY; FOLLOW EVERY SENTENCE YOU MOVED TO THE MOUTH THAT SPOKE IT; AND RE-RUN THE PUBLISHED INSTRUMENT ON THE FILES YOU JUST WROTE, AND WRITE WHAT IT PRINTS, AND NOT WHAT IT PRINTED BEFORE.**
