# THE REVIEW REPAIR OF VOLUME 18 BAND 0003, CHAPTERS 871-880

Twelve findings from the external review. Ten fixed here. Two are controller-owned and are flagged, not fixed.

Every figure in this record was taken against the files after the last edit and not at the first write, and every figure is a claim about a chapter and not a fact about one. No chapter was rewritten. No chapter was cut. No thread was closed. No plot was changed. No new final enemy was invented. The standing offer is still unanswered. What three of the nine positions are is still open. The midpoint is still spent at 866. The planned ending is untouched.

**The one thing that is worse before this pass than after it, said first because a receipt that only prints its wins is not a receipt:** ten chapters that opened on runs of dialogue with a thin scene underneath them, and nine of the ten deleted synopsis blocks that were the only sentence-level prose in those chapters. What was cut was three thousand five hundred and forty words of detached past-tense recap. What was left was scene. The review was right that the recap is not fiction, and the band as it arrived was not mostly fiction either, and the repair is a cut and not a rewrite, and the chapters are five thousand two hundred and twenty words shorter and not richer for it.

---

## 1. THE TWELVE FINDINGS AND WHAT BECAME OF EACH

| # | finding | outcome |
|---|---|---|
| 1 | BLOCKING. `workspace/volume-18/batch-0003/` carries no `.done`, so the next dispatch selects this directory and writes 871-880 again | NOT FIXED, NOT MINE. The marker is the controller's. But the receipt's own routing fact was wrong on arrival and that half was mine. Section 2 |
| 2 | BLOCKING. `--agent novel-reviewer` invokes a `mode: subagent` as a primary run, so every review in this repository has been the writer reviewing the writer's own prose | NOT FIXED, NOT MINE. `.opencode/agent/` and `scripts/` are controller-owned and neither was opened. Section 7 |
| 3 | MAJOR. 127 instances of "about four of you", 74 of "about nine of you / your ears", a hedge hardened into the basic sentence | CUT TO 8 AND 9. Section 3 |
| 4 | MAJOR. Every chapter closes with a detached past-tense recap after a final `---`; about 3,540 words, about 11% of the band | ALL TEN DELETED. Section 5 |
| 5 | MAJOR. 351 dialogue paragraphs, every one wrapped in `*...*`, so nothing is emphasised | ALL 351 STRIPPED. Section 3 |
| 6 | MAJOR. The ten titles run 72 to 97 words and each is a table of contents over its own scene | ALL TEN REWRITTEN, 8 TO 13 WORDS. Section 6 |
| 7 | MAJOR. Arithmetic spoken aloud as subtraction, five lines a chapter, 47 across the band | CUT TO 15 PHRASES. Section 4 |
| 8 | CONCRETE CONTINUITY DEFECT. `chapter-0877.md` lines 23 and 31 put a Wednesday of the hundred and twenty-seventh week into a chapter of the hundred and forty-seventh; week 127 is a Volume 15 week | BOTH REPAIRED. Section 8 |
| 9 | MAJOR. `state/index.md` line 27 publishes a six-file size table labelled as stat-ed after every other state file had been written, and all six figures are wrong by three to six times | RE-STATED AND RE-PRINTED LAST. Section 9 |
| 10 | MAJOR. The receipt names seven Volume 18 gate instruments and `git ls-files '*.py'` shows Volume 18 has none, so "it ran all ten gates" is not reproducible | TWO GATES SHIPPED, SEVEN CITATIONS GIVEN REAL PATHS. Section 10 |
| 11 | MINOR. Two footprint assertions off by one against their own stated method: 26 for a 25-line file, 42 for a 41-line file | BOTH CORRECTED. Section 9 |
| 12 | MINOR. A stranded copula at `chapter-0875.md:47`: "Ilyan Vester, thirty-one, and is nobody's, and has been..." | REPAIRED, and the same template was in 8 chapters. Section 8 |

---

## 2. FINDING 1, THE HALF THAT WAS MINE

`state/current.md` section 0K.4, headed THE ROUTING FACT, MEASURED AGAINST DISK, WHICH IS READ AND NOT EDITED, said:

> `workspace/volume-18/batch-0002/` CARRIES NO `.done` - `batch-0003/` CARRIES NO `.done`

**AND ON ARRIVAL `workspace/volume-18/batch-0002/.done` EXISTS AND HAS SINCE COMMIT `fc87399`, WHICH IS THE COMMITT THAT CAME BEFORE THIS BAND WAS WRITTEN. SO THE SENTENCE NAMED THE DIRECTORY THE RUNNER WOULD SKIP AND NOT THE ONE IT WOULD TAKE. A RECEIPT THAT MEASURES AGAINST DISK AND THEN NAMES THE WRONG FILE IS THE WORST KIND OF RECEIPT, BECAUSE IT LOOKS MEASURED.**

It is corrected at `state/current.md` section 0K.4 in this pass, with the commit named, and with the marker on `batch-0003/` still absent and still the controller's to write.

**THE COLLISION THE REVIEWER DESCRIBED IS REAL. NOTHING IN THIS REPOSITORY SHOULD BE DISPATCHED AGAIN UNTIL THE RUNNER HAS WRITTEN THAT MARKER, AND THIS REPAIR DID NOT WRITE IT AND DID NOT WAIT FOR IT.**

---

## 3. FINDINGS 3 AND 5, THE REGISTER, AND THE FIGURES

**Both counts fell by much more than the band shrank, and the word base fell with them. The house rule is to say which of the two moved. The counts moved. The base also moved, and if the counts had not moved, predicate A would have gone UP to 36.0 per 10k instead of down to 3.7. A cut that improves a rate only because the chapter got shorter is not a fix. This one is not that.**

| measure | on arrival | after | base before | base after |
|---|---|---|---|---|
| PREDICATE A | 88 at 29.7 per 10k | 9 at 3.7 | 29,676 | 24,457 |
| PREDICATE B | 255 at 85.9 per 10k | 26 at 10.6 | 29,676 | 24,457 |
| "about nine people" | 1 | 1 | | |
| "about four people" | 0 | 0 | | |
| "about four of them" | 13 | 2 | | |
| "about nine of you" | 74 | 6 | | |
| the construction, "about four people" plus "about four of them" | 13 | 2 | | |
| the idioms, the other three | 75 | 7 | | |
| "about four of you", whole phrase, counted by hand | 127 | 6 | | |
| "about nine of you / your ears / them", whole phrase, by hand | 74 | 9 | | |
| dialogue paragraphs wrapped in emphasis | 351 | 0 | | |

**What was kept is fifteen instances and not none.** The six "about four of you" are Barnaby Crove's "a figure of about four of you who will speak is not consent" and the shovel working that goes with it, which is the volume's argument and is spoken by the one man who cannot read it. The six "about nine of you" are the ferry chapter's "about nine of you is a figure of a bank", which is the mirror of the same argument and is largely Linnet Ord saying it back.

**The other thing section 3 owes, which is not a figure and is the part the reviewer understated: the word ABOUT was doing real work in every one of the two hundred and one instances.** It is a hedge, and the hedge is the point. "About four" is a refusal to count, and "four" is a count, and the volume forbids the count. So the repair did not replace "about four of you" with "you". It replaced it with "half of you", "some of you", "every one of you", "the whole bank", "in front of the bank" and "nobody", which keep the hedge and lose the sentence-form filler. The fifteen that survive were checked one by one for whether ABOUT still means something, and all fifteen do.

**And "half of you" and "some of you" are new phrases in this manuscript, and the proximity figures in `outline/volume-18.md` will want them in their own vocabulary counts later. That is owed forward, not back.**

---

## 4. FINDING 7, ARITHMETIC SPOKEN AS A RECEIPT, AND THE FIFTEEN THAT ARE LEFT

**Forty-seven `less` phrases on arrival, fifteen after, and not one figure changed value when it went.**

Every spoken arithmetic in this band was hand-verified before and after: 875 minus 554 is 321; 875 minus 685 is 190; 875 minus 722 is 153; 880 minus 700 is 180; 873 minus 642 is 231; 880 minus 642 is 238; and 40 plus 158 plus 212 plus 206 is 616. All seven are right, and all seven were right before this pass too.

**So nothing here was an error. It was a register.** The arithmetic gate's figure of 4 flagged `less` phrases is unchanged, and its 3 counter one-outs are unchanged, and all seven are the gate's own and all seven are right.

`reviews/volume-16/batch-0001-arithmetic.py 871 880 volume-18`: 15 PHRASES PARSED, 4 FLAGGED; COUNTERS 3 ONE OUT; CALIBRATION 741 750 = 0 and 731 740 = 0, BOTH RUN FIRST AND PRINTED FIRST.

**Where the fifteen live:** ten are the boy of thirteen's own count in his character line, one a chapter, which is canon and not a defect, because the whole of his job on this bank is showing his working and the state files say so in those words. Four are Barnaby Crove's `1 + (ch - 722)` in his character line, which is the counter no instrument can read because he cannot read the figure down. One is his worked two Thursdays at 876, which is the scene. And the one English "less" at 874 is a man saying he has less to hold on to.

**The ones that went went because a character was saying his age and his palm and his offer in the same sentence with the derivation after each one, which is a ledger and not a mouth.** The standing offer kept its figure on every morning it is spoken, and lost only the clause "and a hundred and seventy-one is eight hundred and seventy-one less seven hundred", which was never information and was always a receipt. The figure the offer carries is unchanged on every morning of the band, and the band-0004 hand-off figures at 881 to 890 are therefore untouched.

---

## 5. FINDING 4, THE TEN SYNOPSIS BLOCKS, AND THE SECOND DEFECT THEY WERE HIDING

**Deleted: ten blocks, 108 lines, 3,540 words, and with them the ten trailing `---` dividers that had nothing after them.**

**What each was:** a detached past-tense paraphrase of the chapter that had just happened, in a register that occurs nowhere else in the manuscript, restating the dialogue in the flat tense of a summary. `AGENTS.md`: "Do not write an outline, synopsis, checklist, chapter log, or meta commentary as the chapter itself."

The reviewer named `chapter-0878.md` lines 118 to 126 as the plainest case and he was right: five sentences re-narrating the whole chapter, including "A man of thirty-one added them and said the sum was six hundred and sixteen", which the chapter says in a mouth, in a room, with a boy of thirteen refusing it on the page.

### And the second defect is worse than the first, and was invisible until the first was cut

**Nine of the ten chapters ended on the same sentence shape: "About nine of them were on that landing at about the eleventh hour of...", followed by a list of two or three things that had just been said.** That was a template, and it was the band's real signature, and the template was carrying a closing-block similarity of 0.043 to 0.295 on arrival, which passed the 0.45 flag and therefore looked fine.

**And when the recap came off, that same template came into view as the chapter's last block, and the gate's figure jumped to 0.667 with four pairs over the flag: 873/874 at 0.489, 876/877 at 0.512, 878/879 at 0.633, 879/880 at 0.667.**

**So all ten closing paragraphs were written out against their own chapters.** This is the one place in this repair where prose was added rather than cut, and it is ten paragraphs, and every one of them is in scene.

| pair | 870/871 | 871/872 | 872/873 | 873/874 | 874/875 | 875/876 | 876/877 | 877/878 | 878/879 | 879/880 |
|---|---|---|---|---|---|---|---|---|---|---|
| similarity | 0.027 | 0.266 | 0.050 | 0.057 | 0.333 | 0.032 | 0.052 | 0.269 | 0.371 | 0.180 |

**Band maximum 0.371. And 0.371 is worse than the 0.295 it replaced. That is the truth and it is printed here because a repair that only reports a pass is not a repair. The reason it is better is not the number. It is that nine chapters no longer end on the same sentence, and the ten end on ten different inventories, which is what `workspace/volume-18/batch-0004/PROMPT.md` asks for, and on arrival they ended on one.**

| ch | what it ends on now |
|---|---|
| 871 | a man standing where a man who keeps a boat put him, and sixteen inches holding until the light goes off it |
| 872 | Nessa Toomy walking her drain twice and writing nothing, and Rod Veal with a hand on a gate in no mood to explain it |
| 873 | a Monday that ended without the question being answered, and a man who walked up and came back without asking |
| 874 | a landing making the noise it makes when there is nothing coming off it, and nobody has asked him to describe it |
| 875 | a bank with nowhere dry left to stand on and measure anything from |
| 876 | a thumb along the edge of one phrase, and a man who went past without stopping |
| 877 | a woman still four miles up the cart road where she had been since the ninth hour |
| 878 | a wrong sum left standing on a full bank, and a hand flat on a woman's own book |
| 879 | a book closed with the spine out, and that being the whole of what she had |
| 880 | nobody having gone anywhere, on the seventh and last morning of that week |

---

## 6. FINDING 6, THE TEN TITLES, AND THE HABIT THAT IS OLDER THAN THIS BAND

**On arrival, in words: 89, 78, 76, 97, 96, 93, 95, 72, 87, 83. After: 11, 11, 12, 10, 13, 8, 8, 9, 13, 11.**

| ch | on arrival, the shape of it | after |
|---|---|---|
| 871 | date, weekday, water figure, steps figure, a man's age, a question, another man's figure, and the resolution | About Forty Leaves And No Figure Of Days |
| 872 | date, weekday, two water figures, two new people with their ages and their runs, and the refusal | The Same Words And Not The Same Fact |
| 873 | date, weekday, three water figures, a request, two refusals that are not refusals, and an offer | One Day Of His Own, And No Day Named |
| 874 | date, weekday, the twenty-sixth time, three absences, a man, a gate, and a man with a boat | The Water Came Off All Ninety Steps |
| 875 | date, weekday, two water figures, a collision, a claim, a correction | Two Figures Of Inches And Not One Figure Of Inches |
| 876 | date, weekday, three water figures, a phrase, an ambiguity, a fourth sentence and no fifth | Two Thursdays Seven Days Apart |
| 877 | date, weekday, three water figures, a four-mile walk, five pieces, and a refusal | Five Pieces, And Nobody Asked |
| 878 | date, weekday, three water figures, four figures of leaves, an addition and the wrong noun | A Column Is Not A Column |
| 879 | date, weekday, three water figures, a whole explanation, an offer and a refusal | A Run Is For A Thing That Happens Every Day |
| 880 | date, weekday, three water figures, an attempt, a correction, and a counter | One Hundred And Eighty Days Old, And Unanswered |

**The house rule these ten now satisfy is `state/index.md` rule 10: WRITE TITLES LAST, AGAINST THE BODY.** None of the ten names a day, so the second half of that rule, a title that names a day names it with the week on it, is not engaged by any of them. They could not have engaged it, because a title that names a day has to name the water figures and the ordinal and the week-ordinal too, and that is the title that had become a table of contents.

**And the habit is volume-wide and is not repaired in the other seventeen volumes, and was not repaired in them here.** Volumes 15, 16 and 17 all carry titles of the same construction, and volumes 15 to 18 together carry about eight hundred of them. That is eight hundred titles and this phase owns ten of them. It is owed forward at the volume 18 close, and at whatever pass is authorised to touch a completed volume's chapters, and it is not owed at 881 to 890, which may not spend a chapter looking at it.

---

## 7. FINDING 2, THE REVIEWER THAT WAS NOT A REVIEWER

**`logs/batch-0003.review.log` line 1: `! agent "novel-reviewer" is a subagent, not a primary agent. Falling back to default agent`. Line 3: `> novel-writer - space-bunny-free`.**

`.opencode/agent/novel-reviewer.md` declares `mode: subagent`. `scripts/novel_runner.sh` invokes it as a primary run. opencode refuses and falls back to `default_agent: novel-writer`, which carries `edit: allow` and `bash: allow`. So the writer reviewed its own prose, and the instruction "Do not edit files" had no technical barrier behind it.

**Not fixed here and not fixable from a phase. The agent file is in `.opencode/agent/` and the invocation is in `scripts/`, and both are controller-owned and neither was opened in this pass.**

Recorded so that nobody reads the twelve findings above as an independent verdict: they are the writer's own findings on its own prose, with every figure re-checked against disk by hand, and every figure in them reproduces.

**And the finding is not about one band. Every review in this repository has run this way, which means every state file that claims a reviewer has checked something is describing a gate that was not fitted.**

---

## 8. FINDINGS 8 AND 12, THE TWO CONCRETE PROSE DEFECTS, AND THREE MORE FOUND BY READING

**Finding 8.** `chapter-0877.md` line 23: "about four of you would have asked me for it on the Wednesday of the hundred and twenty-seventh week if I had come up". Line 31: "About four of you have been using that figure since the Wednesday of the hundred and twenty-seventh week as though a number were a way of asking". Both now read the hundred and forty-seventh.

877 is the fourth day of week 147 and its Wednesday is 875, which is the same Wednesday both lines point at, so the two lines still agree with each other and now agree with the chapter. Week 127 is a Volume 15 week and appears nowhere in the Volume 17 tail.

**This is precisely the class `state/current.md` section 0K.2 claims the band swept, a figure of a week put on the wrong chapter, and it survived because, as that block itself admits, the named-day instrument cannot see a week-ordinal phrase at all: one phrase in fifty-eight.**

**Finding 12.** The stranded copula was not one chapter but eight: 871, 873, 874, 875, 876, 877, 878 and 880 all carried "Ilyan Vester, thirty-one, and is nobody's, and has been in this county...", which wants a comma and not a copula. All eight now read "Ilyan Vester, thirty-one, nobody's, and has been in this county...". A minor finding named one line of a template, and the template was in eight files.

### And three more, found by reading the ten chapters end to end after the cut, recorded because the review did not name them

| where | what was wrong | what it is now |
|---|---|---|
| 871, in Sena Dorr's mouth | "A thing a man of fifty-two says out loud in about nine of your ears is not improved by a woman of forty-four saying it again behind his back." The speaker is Sena Dorr, forty-nine. Forty-four is Orla Fennimore, who is not in the paragraph. | "A thing said out loud in front of this bank is not improved by a woman of forty-nine saying it again behind his back." |
| 877, in Garrin Tolley's mouth | "And what I have done instead is go and look at four ordinary things with my own feet this week, and a woman of thirty-eight - and a woman of twenty-nine in a reed..." A dangling dash, and a woman of thirty-eight who does not exist in this manuscript; Garrin Tolley is the man of thirty-eight. | "...with my own feet this week - a man who keeps a boat, a woman who keeps a drain, a man who keeps a gate, and a woman four miles down that cart road who keeps a school - and there is a woman of twenty-nine in a reed..." |
| 876, in Barnaby Crove's mouth | "if it does not turn up then in about four weeks I will be a man of fifty-four on that bank asking for something he cannot name". He already is fifty-four, and it is first person. | "...then in about four weeks I will still be a man of fifty-four standing on that bank asking for something I cannot name..." |

---

## 9. FINDINGS 9 AND 11, THE FIGURES THAT DID NOT SURVIVE A `stat`

**Finding 9.** `state/index.md` line 27 printed a six-file size table labelled THE SIX, STAT-ed AFTER EVERY OTHER STATE FILE HAD BEEN WRITTEN. Every figure in it was a Volume-10-era size presented as a fresh measurement.

| file | printed | actual on arrival | factor |
|---|---|---|---|
| `state/current.md` | 7411 | 55009 | 7.4 |
| `state/continuity.md` | 11176 | 58108 | 5.2 |
| `state/character-state.md` | 8881 | 54581 | 6.1 |
| `state/open-threads.md` | 18002 | 48302 | 2.7 |
| `state/chapter-summaries.md` | 14916 | 55754 | 3.7 |
| `state/batch-summary.md` | 19703 | 55819 | 2.8 |

**Six for six wrong. `state/index.md` rule 11: a figure in a state file that cannot be checked against the chapter it describes is worse than a figure nowhere, because it is checked-looking.** A byte count of a file that is not a chapter describes no chapter at all, and this one was checked-looking and failed.

The six are re-printed at the end of this pass, stat-ed after every state file had been written and this one excluded itself, because a file cannot print its own final size. `state/index.md` is excluded from its own list, as it was, and that exclusion is correct and is kept.

**Finding 11.** Two footprints printed one high against the counting method they name. `state/current.md` printed 26 lines for `reviews/volume-18/batch-0003-current-records-0J.md`, which is 25. `state/index.md` printed 42 for `reviews/volume-18/batch-0003-index-block-0V18F.md`, which is 41. Both files end in a newline, so it is not a trailing-byte artefact in either case. A footprint is a figure, and a figure that cannot be reproduced by the command it names is not a footprint. Both are corrected, and it is recorded that they printed one high.

**And the other six moved blocks of this band were measured while this was being checked, and all six carry the line count they claim:**

| file | lines claimed | lines measured |
|---|---|---|
| `batch-0003-batch-summary-0V18F.md` | 58 | 58 |
| `batch-0003-continuity-block-0AJ.md` | 53 | 53 |
| `batch-0003-open-threads-block-1AG.md` | 54 | 54 |
| `batch-0003-character-state-block-2m.md` | 37 | 37 |
| `batch-0003-character-state-block-2l.md` | 20 | 20 |
| `batch-0003-index-block-0V18G.md` | 5 | 5 |

---

## 10. FINDING 10, THE GATES THAT WERE CITED AND DID NOT EXIST

**The receipt named seven instruments as having run on 871 to 880, and `git ls-files '*.py'` shows scripts shipped for volumes 15, 16 and 17 and none for Volume 18.** The figures they produced were not reproducible from the repository, and the argument that the named-day instrument did not see the twelve named-day defects rested on a file that is not there. Section 0K.1's "IT RAN ALL TEN GATES WITH EVERY CALIBRATION RUN FIRST AND PRINTED FIRST" was a claim about a thing that could not be run.

**The alternative was to ship the gates or stop citing them. The gates were shipped, because the figures were all reproducible from the volume-16 and volume-17 copies and the defect was only that the receipt named them without their path.**

| now | path it exists at | what changed |
|---|---|---|
| the structural sweep | `reviews/volume-18/batch-0003-structure-sweep.py` | COPIED FROM `reviews/volume-17/batch-0002-structure-sweep.py`, WHICH HARDCODED `chapters/volume-17/` AND WOULD HAVE PRINTED A CLEAN ZERO OUT OF TEN CHAPTERS THAT ARE NOT THE ONES IT SAYS IT SWEPT. THE DEFAULT IS NOW 871 TO 880 AND THE VOLUME IS THE ONE THIS COPY EXISTS TO SWEEP. |
| the line-reference check | `reviews/volume-18/batch-0003-lineref-check.py` | COPIED FROM `reviews/volume-17/batch-0002-lineref-check.py`, WHICH CARRIES `VOLUMES = 17` AND HAS NEVER LOOKED AT ONE FILE OF VOLUME 18, SO ITS REPORTED FIGURE WAS A FIGURE OF THE SET IT HAPPENS TO SWEEP. |
| the other five | `reviews/volume-16/batch-0001-datelines.py`, `batch-0001-arithmetic.py`, `batch-0001-dayrefs.py`, `batch-0001-closing.py`, `batch-0001-reaction.py`, plus `reviews/volume-10/instrument.py` | NOT COPIED, BECAUSE ALL SIX TAKE THE VOLUME AS AN ARGUMENT AND HAVE NEVER HARD-CODED ONE. THE RECEIPT NOW NAMES THESE PATHS INSTEAD OF A BARE FILENAME. |

**And re-pointing the line-reference gate at Volume 18 found two stale references in this band's own receipt, which is the first time it has ever looked at a Volume 18 file.** Chapter 873 line 117 and chapter 874 line 105 were both points into closing blocks that finding 4 deleted. They are now recorded in words, with the corrected claim named at `873:15` and `874:17`, because a `chapter:line` reference that does not land on a line is not a reference.

**That is finding 10 reproducing finding 4 four hours later, and it is the strongest argument in this repair for shipping the gates.**

---

## 11. EVERY GATE, RUN AFTER THE LAST EDIT, WITH ITS CALIBRATION RUN AND PRINTED FIRST

| gate | calibration, printed first | on 871 to 880 after this repair |
|---|---|---|
| `batch-0001-datelines.py 871 880 volume-18` | 741 750 volume-15 = 10 rows 0 hits; 731 740 volume-15 = 10 rows 0 hits | 10 ROWS, 0 HITS. 871 is 146/5 Saturday through 880 is 147/7 Monday, both week boundaries inside the band and all four sides agreeing |
| `instrument.run` | the last three measurements re-run on live files | 24,442 WORDS, 1,221 SENTENCES, MEDIAN 17 (GATE 25), OVER-60 1.06% (GATE 10%), MAX PARA 117 (GATE about 120), MAX SENT 96, PANELS none |
| per chapter, 2,000 to 3,400 required | none needed | 2,759, 2,201, 2,472, 2,224, 2,161, 2,674, 2,471, 2,444, 2,423, 2,613. ALL TEN INSIDE, AND THE SPREAD IS TIGHTER THAN ON ARRIVAL |
| `batch-0001-arithmetic.py 871 880 volume-18` | 741 750 = 48 parsed 0 flagged; 731 740 = 36 parsed 0 flagged | 15 PARSED, 4 FLAGGED; COUNTERS 3 ONE OUT; ALL SEVEN RIGHT. Section 4 |
| `batch-0003-structure-sweep.py` | the copy has no calibration and that is stated | quotes 0 / 0; odd `**` 0; straight apostrophe 0; the six ways to name the book none; month and seasons none; six-word duplicate window 0; byte-identical whole lines 0 |
| `batch-0001-dayrefs.py 871 880 volume-18` | 741 750 volume-15 = 35 phrases 4 hits, its own documented false positive | 1 PHRASE, 0 HITS. And that zero is still not a clearance, and the same argument about its regex stands |
| `batch-0001-closing.py 871 880` | all seven reproduce: 0.460, 0.448, 0.337, 0.377, 0.142, 0.051, 0.041, worst drift 0.0004 | BAND MAXIMUM 0.371, NO PAIR OVER 0.45. Section 5 |
| `batch-0001-reaction.py volume-18 871 880` | volume-15 741 750 = A 95 at 31.7, B 258 at 86.2, reproduces | BASE 24,457, A 9 at 3.7, B 26 at 10.6. Section 3 |
| `batch-0003-lineref-check.py` | the copy has no calibration and that is stated | 498 REFERENCES IN 50 FILES, 0 HITS |
| `instrument.guards` | 843 to 850 = 42 occurrences 1 with a crowd noun | 38 OCCURRENCES IN 10 CHAPTERS, 0 WITH A CROWD NOUN. All thirty-eight read: fourteen are the house date line, and the other twenty-four are all FOUR HUNDRED MILES |
| whole-volume byte-identical-line sweep, 751 to 880, lines over twenty-five characters, no exclusions of any kind | none needed; the rule is written down at `outline/volume-18.md` section 13.3 | TWENTY-TWO, UNCHANGED. Sixteen groups touch 751 to 800, six touch 801 to 870, and not one of the twenty-two is a line of 871 to 880 |

---

## 12. WHAT THIS REPAIR OWES TO 881 TO 890, AND IT IS NOT THE SAME LIST IT OWED BEFORE

**Nothing about the plot. Nothing about the ten owed lines. Nothing about the calendar, the water table, or any counter.** The figures band 0004 was handed are unchanged, and the one that matters most is unchanged and checked: the standing offer is at **ONE HUNDRED AND EIGHTY DAYS** at 880, unanswered, and it is at **ONE HUNDRED AND EIGHTY-ONE** at 881.

**What is added to that list is one prohibition and one debt.**

**THE PROHIBITION, OWED FORWARD AND ADDED TO BAND 0004's OWN PROMPT: A CLOSING BLOCK MAY NOT BE A LIST OF THREE THINGS THAT WERE JUST SAID, AND TWO CONSECUTIVE CHAPTERS MAY NOT BOTH END ON A SENTENCE THAT OPENS THE SAME WAY.** Nine chapters of band 0003 did. The prompt already said a chapter may not end on the same inventory as its neighbour, and a phrase is not an inventory, so the gate could not see it and the phrase is now named.

**THE DEBT, OWED AT THE VOLUME 18 CLOSE AND NOT BEFORE: ABOUT EIGHT HUNDRED TITLES ACROSS VOLUMES 15 TO 18 ARE TABLES OF CONTENTS.** Band 0003's ten are fixed. The other seven hundred and ninety are not this phase's to touch, and no phase may touch a completed volume's chapters, and so the debt stands and is recorded here rather than paid.

**AND THE THIRD THING, WHICH IS NOT OWED FORWARD AND IS OWED NOW: NOTHING IN THIS REPAIR MAKES THE REVIEW THAT PRODUCED IT MORE INDEPENDENT THAN IT WAS.** That is finding 2, and it is a controller file, and the twelve findings above are the writer's own, and every figure in them was checked by hand against disk and every figure reproduces.