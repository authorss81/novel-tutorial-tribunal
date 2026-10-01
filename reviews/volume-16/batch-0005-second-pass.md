# Volume 16, Band 0005, Chapters 791–800 — Second Pass

**THIS IS THE RECORD OF THE PASS THAT RAN AFTER `reviews/volume-16/batch-0005-review-repair.md`. IT REPAIRED TWENTY-FOUR FIGURES ACROSS ALL TEN CHAPTERS AND IT RESTARTED NO CHAPTER AND IT CHANGED NO PLANNED PLOT AND IT ADDED NO CHARACTER AND IT INVENTED NO PLACE. EVERY FIGURE THE REPAIRED BEAT RESTS ON WAS ALREADY ON THE PAGE IN A CANON CHAPTER BEFORE THIS PASS RAN.**

**THE ONE LINE THAT MATTERS: THE BAND PROMPT PRINTED THE START DAY OF A MAN OF THIRTY-EIGHT'S COUNT OF THE MORNINGS HE HAS SAID THE NUMBER OF NAMES OUT LOUD AS `779`, AND THE CANON FIXES IT AT `781` BY TEN ORDINAL-BEARING LINES IN SEVEN CHAPTERS OF BAND 0004, WHICH CARRY SEVEN DISTINCT ORDINALS. EVERY ONE OF THE TEN FIGURES THAT RUN GENERATES WAS INHERITED WRONG, EIGHT OF THEM ARE ON THE PAGE, AND `797` HAD A SECOND SLIP OF ITS OWN WHICH MADE IT COLLIDE WITH `796`. ⚠ NOT ONE GATE IN THIS REPOSITORY CHECKS THE LENGTH OF A RUN, AND THE COUNTER READ-BACK REPORTED `0 ONE OUT` ON A BAND WITH EIGHT RUN FIGURES WRONG.**

---

## 1. What this pass was, and what it was not

**The chapters and the state files for `791`–`800` were already on disk when this phase opened.** `git log` shows them written in `6ee278d *save writer work batch-0002*` — a phase dispatched into `workspace/volume-16/batch-0002/`, which had already been completed, and which therefore read this band's prompt instead and obeyed it. That is the misroute the phase prompt anticipates and the first pass disclosed. **A ten-chapter receipt replaces the last one and is never added to it, so the second thing this pass did was read the band as a checker, not as a writer, and take every figure in it back to the chapter that made it.**

**What it did not do: it did not re-derive any of the volume's spent substance. The proof is spent, the power is spent, the seven offers and seven refusals stand at seven and seven, the right of refusal is unrestored and given to nobody, the standing offer is unanswered at a hundred days, `citizen` is at 0, and the volume's new question is asked at `800` and is not answered.** Those are all still true and none of them was touched.

---

## 2. The findings, one by one, with the working

### 2.1 BLOCKING — A WHOLE RUN-LADDER, INHERITED FROM THE PROMPT, WRONG IN EIGHT CHAPTERS. **REPAIRED ON THE PAGE.**

A man of thirty-eight said the number of names he can see on the ninth line out loud once a morning. The count of that is a **run**, not a `ch − n` counter, so the only thing that can fix it is another run figure somewhere else. The canon has ten lines carrying one, in seven chapters of band 0004, and they give seven distinct ordinals:

| Chapter | The figure, in his own mouth | Day |
|---|---|---|
| `783:59` | *I have said the number on **three** mornings running* | Tuesday, week 134 |
| `784:39` | *it is the **fourth** morning running* | Wednesday, week 134 |
| `785:33`, `785:83`, `785:89` | ***Five** mornings running* | Thursday, week 134 |
| `786:37` | ***Six** mornings running* | Friday, week 134 |
| `787:35`, `787:39` | *the **seventh** morning of saying it* | Saturday, week 134 |
| `788:41` | *eight mornings* | Sunday, week 134 |
| `790:39` | ***it is the tenth morning running*** | Tuesday, week 135 |

`790 − 9 = 781` and `779 + 9 = 788`. The prompt's `779` gives a tenth at `788`, and `788:41` says **eight**. The canon says `781`, and every one of the ten lines above agrees with it. **The ninth is never printed anywhere: `789` gives the number and the figure for being left alone but carries no run ordinal of its own, so the ladder runs three, four, five, six, seven, eight and then ten.** **The run began on the Wednesday of the hundred and thirty-fourth week, on which a man of thirty-four said four names before he read anything else.**

| Ch | Was | Now | Rule |
|---|---|---|---|
| `791` | thirteenth | **eleventh** | `791 − 781 + 1` |
| `792` | fourteenth | **twelfth** | `792 − 781 + 1` |
| `793` | fifteenth | **thirteenth** | `793 − 781 + 1` |
| `794` | sixteenth | **fourteenth** | `794 − 781 + 1` |
| `795` | seventeenth | **fifteenth** | `795 − 781 + 1` |
| `796` | eighteenth | **sixteenth** | `796 − 781 + 1` |
| `797` | eighteenth | **seventeenth** | `797 − 781 + 1` |
| `800` | twenty-second | **twentieth** | `800 − 781 + 1` |

`798` and `799` carry no figure of the run and need none; a man of thirty-eight has no dossier line in either, and the run is a run of mornings he was on that bank, which is every morning.

**`797` had a second and separate slip.** It said *the eighteenth morning*, which is the figure `796` gives in the chapter before it, in the same mouth, on the same beat. A run that repeats itself in consecutive chapters is not a run, and two adjacent chapters carrying the same ordinal is the one thing no sweep in this repository compares. That is a third instance of the §4 finding in the first repair record.

**Eleven state-file figures carried the wrong value and are corrected:** `state/open-threads.md` §1T.6 · `state/continuity.md` §0Y.5 · `state/character-state.md` §1y · seven chapter summaries in `state/chapter-summaries.md` · and `state/batch-summary.md` §0V16E.4, which printed the run as *the thirteenth to the twenty-second*.

### 2.2 BLOCKING — A NAMED DAY OUT BY A WEEK-ORDINAL, NINE TIMES, IN SIX CHAPTERS. **REPAIRED ON THE PAGE.**

Hazard eighteen at `state/open-threads.md` §0A.18 records that the manuscript's weeks run **Tuesday to Monday**, and that twelve such phrases in `781`–`790` were out by one chapter and every one of them was that class. **Nine more were out in this band and the same class found them, and `batch-0001-dayrefs.py` flagged three of the ten it saw and all three were correct.** Each was resolved against the chapter that made the claim.

| Ch | Was | Now | Resolves to |
|---|---|---|---|
| `791:19` | *He announced on the Sunday* | *on the Thursday of last week* | `785`, which is what `789:29` and `790:25` both say |
| `793:79` | *on the Thursday of this week*, and a claim `792` does not make | *on the Wednesday of this week*, and the claim `791:47` does make | `791` |
| `795:9` | *on the Sunday of the week before last* | *on the Sunday of last week* | `788`, which `789:11` calls yesterday and `790:11` calls *the Sunday of last week* |
| `795:89` | *put the sixth count down on the Thursday of the week before last* | *on the Thursday of last week* | `785` |
| `796:9` | *on the Sunday of the week before last* | *on the Sunday of last week* | `788` |
| `796:89` | *the Thursday of the week before last* | *the Thursday of last week* | `785` |
| `796:49` | *on the Monday of the week before last* | *on the Monday of last week* | `789`, which `793:61` and the band's own ground both give |
| `799:53` | *on the Monday of that week* | *on the Monday of the week after, which is seven hundred and eighty-nine* | `789` |
| `800:7` | *it is the first morning of a week* | *it is the fourth morning of that week* | `800` is day four of week 136 |

**`795` and `796` are the two chapters the hazard predicted.** From a day in week 135, *the week before last* is week 133; from a day in week 136 it is week 134, which is where the stone and the sixth count actually are. `797`–`800` were right, and they are right for the reason the hazard gives.

**And one misattribution, which is not a week-ordinal at all.** `796:77` credited a woman of forty-four with having said *a case is not a set of figures* on the Monday of that week. It is a woman of forty who says it, at `796:51`, and the same block's own speech at `796:85` credits her correctly. The dossier line now says what she did say, and what `791:47` supports.

### 2.3 BLOCKING — THREE FIGURES PRINTED WITHOUT THE RULE THAT MAKES THEM. **REPAIRED ON THE PAGE.**

**`798:51`.** A man of about fifty-two checks eleven figures out loud and catches himself. He said he had said *ninety-one* for a counter where the true figure is *ninety-three*, and said *ninety-one is the figure for Tuesday*. **Ninety-one is `796 − 705` and `796` is the Monday; Tuesday is `797` and Tuesday's figure is ninety-two.** So the slip he describes as *a day from yesterday* was two days, and the day-name was wrong. It is now *ninety-two*, which is Tuesday's figure, and the sentence's own claim — a day from yesterday — is true for the first time.

**`800:125`.** *A hundred days. A hundred is eight hundred less seven hundred, and I have given that figure ninety-nine times.* The count is right and the band gives it every morning from `791`, so a hundredth figure belongs in the mouth on the morning it is a hundred. It is now the house form of `781`–`784` and `790` — *I have given that figure every morning since the fifty-first* — **with the rule made visible: *and this morning is the hundredth of them*.** A figure printed without the rule that makes it is the failure this file has been charged with twice already.

**`800:17`.** A man of forty-three said *a hundred days is a figure I have heard twice this week from a man of thirty-one.* The figure of a hundred days had not been given this week at all; the man of thirty-one gives a figure of days on **every** morning of this week, `797` to `800`, and it is a round one this morning for the first time. It now says that, and it dates the man's own round-figure statement to the Tuesday of last week, which is `790` and is where he said it.

### 2.4 MAJOR — A CHAPTER SAYS IT HAS READ A LIST OF SEVEN AND LISTS SIX, AND A CLOSING BLOCK NAMES A DAY THE LIST WAS NOT MADE ON. **REPAIRED.**

`795:101` said *a list of seven things* over a list of six. It is now six, and the seven-item list at `798:119` is a different and later one, which is why `798` can say seven. The closing block of `798` said *a list he made on Wednesday*; the list was read out on the Saturday at `795`, and the closing now says so without a day it cannot support.

### 2.5 MAJOR — A FIGURE IN THIS BAND INHERITED A CONTRADICTION FROM FOUR CHAPTERS IT DOES NOT OWN. **PARTLY REPAIRED, AND THE REST CARRIED AS A HAZARD.**

`798:121` said *I have walked about four miles*. The walked total is either `3,580` yards — three miles and six hundred yards, at `782:53`, `782:55` and `790:55` — or `2,940 paces × 2` yards = `5,880`, which is what Simon Rook checks out loud at `798:37` and which divides exactly. **Neither is about four miles.** It is now *about three miles*, against the `5,880`.

**The contradiction underneath it is not repaired, because none of the four chapters that carry it is this band's.** `782:49` puts the low gate at *three miles and two hundred yards*, `5,480` yards, which is `2,740 paces × 2` exactly — and `782:53` puts the **total walked** at *three miles and six hundred yards*, `3,580`, **which is less than the distance to the low gate inside the same chapter**, and which is not `2,940 × 2`. It is off by `2,300` yards. Carried as **hazard twenty** at `state/open-threads.md` §0A, with the working, for the close to dispose of.

**And `chapter-0779.md:93` was examined and not repaired.** The seventh-hundred-and-sixty-yard sum is real, it is on the page, and `779` and `776` are bands 0003 and 0002. The lawful disposition taken is the one that leaves it: **left, and not added to.** That disposition is now recorded once in hazard seventeen so that *neither is done yet* is not left dangling, which is §0A.5's own shape.

### 2.6 THE FIGURES THIS PASS LEFT ALONE, AND WHY

- **`799:25` says the reading of the ninth line *has been a man of thirty-eight for seventeen of them*.** No canon ordinal pins when he began reading it in the open, and `781` is the earliest morning on which a chapter shows him doing both things. Seventeen and eighteen are both defensible and neither is checkable, so the figure was not made more precise by being changed.
- **`787:35` and `790:43` carry a ten-day figure on two different anchors.** `787:35` says *the tenth day of nobody asking me for anything* and `790:43` says *Ten days. That is the longest anybody has gone without asking me for a thing*, and `790:149` and `790:35` are the same ten days again. It belongs to band 0003 and band 0004 and no figure in `791`–`800` is derived from it.
- **⚠ `780:23` SHOWS HIM SAYING THE NUMBER AND `781` SHOWS HIM SAYING IT, AND ONLY ONE OF THEM CAN BE THE FIRST MORNING, AND ⚠ THIS PASS DID NOT SETTLE IT.** `780:23` says *the man of thirty-eight said the number of names before he read anything else, because he said on Friday that he would*, and `780:39` confirms the promise was made on `779`. So on the reading of `780` the first morning is `780` and `783:59`'s *three mornings running* is one out; on the reading of the seven distinct ordinals the first is `781` and `780:23` is a chapter that overstates by one. **THE SEVEN ORDINALS WERE TAKEN OVER THE ONE, BECAUSE SEVEN CHAPTERS AGREE WITH EACH OTHER AND ONE CANNOT, AND BECAUSE `788:41`'s *EIGHT MORNINGS* AND `790:39`'s *TENTH MORNING RUNNING* ARE BOTH IN CHAPTERS THAT ALSO CARRY OTHER FIGURES THIS BAND USES AND NEITHER OF THEM IS A STRAKE.** ⚠ **IT IS RECORDED HERE AND NOT REPAIRED, BECAUSE REPAIRING IT WOULD MEAN CHANGING A FIGURE IN A CERTIFIED CHAPTER OF BAND 0003 ON THE WORD OF A BAND THAT HAS ALREADY REPAIRED EIGHT FIGURES THIS PASS, AND NO FIGURE OF `791`–`800` DEPENDS ON WHICH OF THE TWO READINGS IS RIGHT.** IT IS THE ONE THING IN THIS RECORD THAT IS A JUDGEMENT AND NOT A PROOF.

---

## 3. The gates, re-run on the published tool after the last edit

Every calibration ran before the thing it calibrates. Figures are from `reviews/volume-10/instrument.py` and `reviews/volume-16/`, not from a re-typing.

| Gate | Result |
|---|---|
| `I.run(791,800,vol='volume-16')` | **27,428 words · 1,079 sentences · median 24 (≤25) · over-60 1.58% (≤10%) · max para 98 · max sent 80** |
| per-chapter rows | 2,577 · 2,147 · 2,257 · 2,266 · 2,394 · 2,375 · **4,771** · 2,835 · 2,589 · 3,217 — **sum to 27,428** |
| `wc -w` on the same ten | 27,439 — eleven higher, the loose markers |
| date lines (3 args) | **10 rows · 0 hits** |
| arithmetic + counter read-back | **62 phrases · 0 flagged** · **0 one out** of 64 · calibrations 741–750 at 48/0 and 731–740 at 36/0, and the read-back's own calibration still returns **5 one out** |
| structure sweep | quotes **0/0** · panel 0 · ASCII apostrophe **0** · month/seasons **none** · the six book-namings **none** · duplicate six-word window **0** · byte-identical whole lines **0** |
| prohibitions | `citizen` 0 · `arbiter` 0 · `villain` 0 · `grateful` 0 · `sorry` 0 · `forgiven` 0 · `coalition` 0 · `First Witness` **1** · `brave` **13** · `thanked` **16** — **all twenty-nine read, all negations or refusals of thanks** |
| silence beat | **0** across 27 wordings · said-nothing **0** · panels **none** |
| named-day sweep | **37 phrases · 3 hits** — `793` and `796` *the Wednesday of this week* → `791`, `800` *the Wednesday of this week* → `798`. **All three correct backward references. All three read.** |
| standing act | calibration reproduces all seven · band max **0.419** at the volume boundary `790`/`791`, flag at 0.45 |
| reaction sweep | six-band calibration run first, and the `721`–`730` row still returns **135 at 55.7** against a printed 137 · base **27,439** · **A 56 at 20.4/10k · B 197 at 71.8/10k** · *about four people* **0** |
| reserved-number guard | `651,700 v14` → 98 · `701,750 v15` → 77 · **`751,800 v16` → 70 in 50 chapters, 2** · `791,800` → 18, 0. **All seventy read.** |
| titles | ten, and the longest is `797` at **78 words** against a guidance of about seventy, and no title names the book it is printed in |

**`797` is 4,771 words and is outside the 2,000–3,400 target, and it was 2,935 on arrival.** It is long because it carries the beat the volume owed and did not have, and the first repair's reasoning for that stands and was not disturbed here. This pass added **55 words to the whole band** and took none out. No chapter was padded to reach a figure and none was cut to get back under one.

---

## 4. The finding to carry into Volume 17

⚠ **Twenty-four figures were wrong across ten chapters, and ⚠ NOT ONE OF THE TWENTY-FOUR WAS FLAGGED BY ANY GATE IN THIS REPOSITORY.** A run length, a week-ordinal, a figure of a *relative*, an attribution, and a list's own length. Every gate came back clean on arrival: the instrument, the date lines, the `LESS` sweep, the structure sweep, the closing act, the reserved-number guard and the named-day sweep all reported their passes, **and the named-day sweep reported three hits and every one of the three was a correct backward reference, so a reader of its output would have concluded the band was clean of named-day error while nine phrases in it were wrong.**

**The first repair's finding stands and this pass is the second half of it: not one gate here measures whether the event the volume owes is on the page, and not one gate measures whether a figure in a chapter is the figure the chapter before it makes.** Both are reading steps, and both cost this band.

**And the generalisation, which is the third time this repository has paid for it: the cheapest thing in a band is a figure with a rule behind it, and the second cheapest is a figure with a named anchor, and the most expensive is a figure whose rule lives in a chapter the band does not own.** A run is the last of the three, because its anchor is an ordinal in some other band's mouth, and this repository has no instrument for an ordinal in a mouth.
