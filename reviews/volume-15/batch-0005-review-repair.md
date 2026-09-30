# Volume 15, Band 0005 — Review Repair Receipt, chapters 741–750

**`logs/batch-0005.review.log` IS THE REVIEW THIS RECEIPT ANSWERS. IT READ ALL TEN CHAPTERS AGAINST THE CALENDAR FORMULA, AGAINST EACH OTHER AND AGAINST THE THREE ARTIFACTS AT THE CENTRE OF THE BAND, IT EDITED NOTHING, AND IT REPORTED FIVE DEFECTS AND TWO MINOR FINDINGS. IT ALSO RECORDED THE SHAPE, THE CALENDAR, THE ARITHMETIC AND THE CLOSINGS AS GENUINELY CLEAN, AND EVERY ONE OF THOSE WAS RE-RUN AT THIS REPAIR AND STANDS.**

**NOTHING WAS RESTARTED. NOT ONE CHAPTER WAS REWRITTEN. NOT ONE PLOT POINT WAS MOVED, NO BEAT WAS ADDED OR REMOVED, AND NO VOLUME DIRECTION WAS TOUCHED. SIX CHAPTERS AND SEVEN STATE FILES WERE EDITED AND EVERY EDIT IS A COUNT, A WORD, A SENTENCE, A POINTER OR A MEASUREMENT.**

---

## 0. What the review found, and what became of each

| # | Finding | Where | What was done |
|---|---|---|---|
| 1 | **Three sweeps took no arguments and silently measured the neighbouring band. `batch-0004-closing.py` hardcoded its pair list to 730/731 … 739/740; `batch-0004-structure.py` hardcoded `LO, HI = 731, 740`; `batch-0004-arithmetic.py` hardcoded all three sweeps in its entry point. `batch-0005-structure.py` had the same shape.** | four scripts | **ALL FOUR REPAIRED.** The range is an argument, the historical range is the default so every figure already printed still reproduces, and the band is announced before anything else is printed. **§1** |
| 2 | **The central artefact of the volume is counted wrong. The third column reads twelve words and the chapter says eleven, three times, and says the words are the nine with *two* in front of them when the front fragment is *three* words long.** | `745:73`, `745:77`, `745:79`, `745:189`, `745:191`, `745:195`, and six chapters and four state files downstream | **REPAIRED TO TWELVE, WITH THE WORKING PUT INTO A MOUTH.** **§2** |
| 3 | **A bare paragraph, `A person who.`, in the closing block of `745`, which reads as a truncation and is not a sentence in any register.** | `745:197` | **REPLACED WITH A COMPLETE LINE CARRYING THE DISCOVERY.** **§3** |
| 4 | **Stale `stat` figures in two places, and one list shorter than the other.** | `state/batch-summary.md` foot, `state/index.md:69` | **THE DUPLICATION IS THE FINDING AND IT IS REMOVED.** One file prints the list, every other file points at it. **§4** |
| 5 | **`state/phase-ledger.json` still reads `batch-0002` while the manuscript is at Volume 15 Chapter 750.** | the ledger | **NOT TOUCHED. CONTROLLER-OWNED, AND THE BAND PROMPT DIRECTED THE WRITER TO LEAVE IT.** Flagged again here for the controller. **§9.1** |
| m1 | *The reading found three closings on the same inventory and the worst of those pairs measures 0.257.* | `state/index.md:3` | **NOT A DEFECT AND NOT CHANGED.** `0.257` IS THE `743`/`744` PAIR, IT IS PRINTED AS SUCH IN THE BAND'S OWN TABLE AT `state/batch-summary.md` §0V15E.9 AND IN `state/current.md` §0.0, AND IT REPRODUCES. **§5** |
| m2 | `A 95 AT 32.0 PER 10k AND B 257 AT 86.4 on a base of 29,731` in `state/index.md:3` against `A 95 AT 31.9 … B 257 AT 86.3 … 29,791` everywhere else. | `state/index.md:3` | **REAL, AND IT HAD BEEN CORRECTED ONCE ALREADY AND NOT IN THAT FILE. RE-MEASURED AND PRINTED ONCE, IN ONE PLACE.** **§6** |

---

## 1. FINDING 1, THE FOUR SWEEPS THAT MEASURED A BAND THEY WERE NOT ASKED ABOUT

**THE REVIEW'S OWN WORDS ON THE WORST OF THEM: *"Running it on 741–750 silently re-measures the previous band and prints a clean-looking table."* AND: *"an instrument that measures its neighbour is worse than no instrument, because it is believed."***

**THIS IS NOT A COSMETIC DEFECT. `batch-0004-structure.py 741 750` REPORTED `forgiven 2` — A VIOLATION THE REVIEW THOUGHT IT HAD FOUND AT `chapter-0740.md:121`, WHICH IS IN THE PREVIOUS BAND. A WRITER WHO BELIEVED THAT OUTPUT WOULD HAVE GONE TO FIX A PROHIBITION THAT IS AT ZERO IN THE CHAPTERS THEY WERE WRITING.**

| Script | Was | Now |
|---|---|---|
| `batch-0004-closing.py` | a literal of ten pairs, no `argv` | `argv` builds the pair list from `lo`; bare, it runs its own historical band and says so |
| `batch-0004-structure.py` | `LO, HI = 731, 740`, no `argv` | `argv` overrides; the default is unchanged; the band is printed first |
| `batch-0005-structure.py` | `LO, HI = 741, 750`, no `argv` | same |
| `batch-0004-arithmetic.py` | three literal sweeps in `__main__` | `argv` names the band; the two calibrations run first regardless, as before |

**THE `sweep` AND `counters` FUNCTIONS WERE ALWAYS CORRECT AND ONLY THE ENTRY POINT LIED, WHICH IS WHY THE BAND'S FIGURES WERE RIGHT WHILE THE INSTRUMENTS WERE WRONG.**

**EVERY HISTORICAL FIGURE REPRODUCES AFTER THE REPAIR, AND THIS WAS CHECKED, BECAUSE AN INSTRUMENT THAT FIXES ITSELF AND LOSES A CERTIFICATION IS NOT A REPAIR:**

```
batch-0004-structure.py        -> MEASURING 731-740 · forgiven 2   · Veyra 0 · amendment 0   (unchanged)
batch-0004-structure.py 741 750-> MEASURING 741-750 · forgiven 0   · Veyra 1 · amendment 6   (the band, correctly)
batch-0005-structure.py        -> MEASURING 741-750 · forgiven 0   · Veyra 1 · amendment 6   (unchanged)
batch-0004-closing.py          -> band maximum 0.347 at 739/740, drift 0.0004                 (unchanged)
batch-0004-closing.py 741 750  -> band maximum 0.284 at 749/750, drift 0.0004                 (the band, correctly)
batch-0004-arithmetic.py       -> SUMMARY: calibration 0, 721-730 0, band 731-740 0            (unchanged)
batch-0004-arithmetic.py 741 750 -> SUMMARY: calibration 0, 721-730 0, band 741-750 0          (the band, correctly)
```

**AND THE FIGURE THE REVIEW SAID WAS NOT THE STANDING ACT'S — *THE 0.284 BAND MAXIMUM QUOTED IN `state/index.md:3` AND §0V15E WAS OBTAINED BY AN AD-HOC SCRIPT, NOT BY THE STANDING ACT* — IS NOW THE STANDING ACT'S OWN OUTPUT, PAIR FOR PAIR, INCLUDING `740`/`741` AT 0.077, `743`/`744` AT 0.257 AND `749`/`750` AT 0.284. THE AD-HOC RUN WAS RIGHT AND THE INSTRUMENT COULD NOT SAY SO.**

---

## 2. FINDING 2, THE COUNT AT THE CENTRE OF THE VOLUME, AND WHY IT IS TWELVE AND NOT ELEVEN

**WHAT THE CHAPTER READS OUT LOUD, AT `745:75`, WHICH IS THE ARTEFACT AND WAS NEVER IN QUESTION:**

> *“*A. Person. Who. Is. Not. There. On. A. Day. Agrees. To. It.*”*

**THAT IS TWELVE WORDS. THE CHAPTER SAID ELEVEN IN THREE PLACES AND SAID THE WORDS WERE THE NINE FROM THE BACK OF THE SHEET WITH *TWO* IN FRONT OF THEM, AND THE FRONT FRAGMENT *A PERSON WHO* IS THREE WORDS LONG.**

**THE THREE-WAY QUESTION WAS WHICH THING WAS WRONG, AND IT WAS NOT ANSWERED BY PREFERENCE:**

| Candidate | Verdict |
|---|---|
| Shorten the reading at `745:75` to eleven words | **REJECTED.** The printed column is an artefact four counties cannot send anybody for, read aloud in a mouth and counted in front of about nine people. Rewriting it to fit a count would make the volume's central object wrong on the page to make a state-file sentence right. |
| Drop the count to twelve and leave it there | **REJECTED.** A corrected figure with no working is the same defect wearing different clothes. |
| **Make the count twelve, and have the mouth that counts it say how the twelve is made** | **ADOPTED.** This is what the manuscript's own rule asks for and what §0T.6 already half-knew. |

**THE REPAIRED PASSAGE, IN A MAN OF THIRTY-EIGHT'S MOUTH, AT `745:77`–`745:85`:**

> *“*Twelve. And I am going to say the other half of it and nobody asked me.*”
>
> *“*That is the nine words from the back of the sheet with three words in front of them. A person who. Three and nine is twelve and I counted it twice and about four of you counted it with me.*”
>
> *“*And one of the nine is not the word that is on the back of it. That one says agrees. The back of that sheet says is agreeing.*”
>
> *“*A rule about a day is one thing and a thing a person does is another one, and the three words in front are what turn the first into the second, and I am not going to say that makes it a different rule.*”

**AND THIS IS THE PART THAT WAS WORTH FINDING. THE BACK OF THE SHEET SAYS *IS AGREEING* AND THE COLUMN SAYS *AGREES*, AND THE COLUMN PUTS *A PERSON WHO* IN FRONT. THAT IS NOT A TYPO TO BE REPAIRED; IT IS THE WHOLE OF WHAT THE AMENDMENT DOES, IT IS WHY A MAN OF FIFTY-FOUR'S FOUR SENTENCES AT `745:95`–`745:103` MATTER, AND IT IS WHY A THING THAT CANNOT TELL A PERSON WHO AGREED FROM A PERSON WHO WAS NOT THERE WILL GET IT WRONG ABOUT EVERYBODY ON THAT LINE. THE CHAPTER HAD THE DISCOVERY AND HAD NEVER SAID IT. IT SAYS IT NOW, IN A MOUTH, WITH THE WORKING GIVEN, AND IT IS NOT SAID IN A PANEL AND NOT SAID BY A NARRATOR.**

**PROPAGATED TO EVERY PLACE THAT CARRIED IT, AND NOT ONE OF THEM WAS LEFT HOLDING THE OLD FIGURE:**

| File | What moved |
|---|---|
| `chapter-0745.md` | `745:73` count, `745:77` the spoken figure, `745:79` the arithmetic, `745:189`, `745:191`, `745:195` the closing block |
| `chapter-0746.md` – `chapter-0750.md` | one reading line each: *the **twelve** words at the top of the third column* |
| `state/continuity.md` | §0T head-list, §0T.6 heading and text, §0T.8 thread 2 |
| `state/character-state.md` | §1t, what the man of thirty-eight found |
| `state/chapter-summaries.md` | the `745` heading and paragraph, and the reading line in `746`, `747`, `748`, `749`, `750` |
| `state/current.md` | the central-pressure line |
| `state/index.md` | three lines |
| `state/open-threads.md` | thread 1 |
| `state/batch-summary.md` | §0V15E.9, the sentence that records which closing was rewritten onto what |

---

## 3. FINDING 3, THE TRUNCATED CLOSING BLOCK

**`A person who.` STOOD ALONE AS A PARAGRAPH IN THE CLOSING BLOCK OF `745`. THE REVIEW WAS RIGHT THAT IT IS NOT A SENTENCE IN ANY REGISTER. IT WAS ALSO RIGHT TO SAY IT *MAY* BE INTENTIONAL MID-SPEECH, WHERE IT NAMES THE FRONT FRAGMENT, AND IT WAS RIGHT THAT IN THE CLOSING BLOCK IT CARRIES NOTHING.**

**IT WAS THE TAIL OF A FIGURE THAT HAD BEEN MISCOUNTED TWICE. IT IS NOW THE HEAD OF THE FINDING THE MISCOUNT WAS HIDING:**

> *One of the nine is not the word that is on the back of it. A man of thirty-eight read the two of them out loud in the same morning, and one of them says agrees and the other one says is agreeing.*

**THE CLOSING BLOCK OF `745` STILL OPENS AND RE-OPENS ON THE SAME INVENTORY — THE SHEET, THE THREE COLUMNS, THE WORDS AT THE TOP OF THE THIRD — WHICH IS THE DEVICE THE BAND PROMPT ASKS FOR AND WHICH THE STANDING ACT MEASURES. IT IS NOT A CHAPTER END THAT SAYS NOTHING.**

---

## 4. FINDING 4, THE TWO SIZE LISTS, WHICH WERE ONE LIST PRINTED TWICE

**THE REVIEW MEASURED BOTH AND FOUND: `open-threads.md` OUT BY 876 BYTES, `batch-summary.md` OUT BY 672, BOTH WRITTEN AFTER THE FOOTER WAS SET; AND `state/index.md:69` STILL CARRYING THE **BAND 0004** SIZES — 54,608 / 52,883 / 58,461 / 55,686 / 40,981 / 31,519 — WITH EVERY ONE OF THEM WRONG AND A SENTENCE ASSERTING ALL SIX ARE UNDER THE CAP.**

**THE FINDING UNDER THE FINDING IS THAT THERE WERE TWO LISTS AND BOTH WERE WRONG, AND THE REASON IS STRUCTURAL RATHER THAN CARELESS: A FIGURE DUPLICATED IN TWO FILES HAS TO BE CORRECTED IN TWO FILES, AND THE FILE WRITTEN LAST INVALIDATES THE ONE WRITTEN FIRST. `state/index.md` PRINTED ITS OWN SIZE AND SAID IT EXCLUDED ITSELF; `state/batch-summary.md` PRINTED ITS OWN SIZE AND SAID IT EXCLUDED ITSELF WHILE PRINTING IT.**

**THE DUPLICATION IS REMOVED. `state/index.md` PRINTS THE LIST AND EXCLUDES ITSELF, BECAUSE A FILE CANNOT PRINT ITS OWN FINAL SIZE. `state/batch-summary.md` NO LONGER PRINTS ANY SIZE AND POINTS AT `state/index.md`, AT §0V15E.14 AND IN ITS FOOTER, AND THE FOOTER NOW SAYS WHY IT STOPPED PRINTING THEM.**

---

## 5. MINOR FINDING 1, THE 0.257, WHICH IS NOT A DEFECT

**THE REVIEW COULD NOT FIND 0.257 ANYWHERE AND READ IT AS A NUMBER THAT MIGHT NOT BE CHECKABLE. IT IS THE `743`/`744` PAIR, IT IS PRINTED AS THAT PAIR IN THE BAND'S OWN TABLE AT `state/batch-summary.md` §0V15E.9 AND IN `state/current.md` §0.0, IT REPRODUCES UNDER THE REPAIRED STANDING ACT, AND THE BAND MAXIMUM OF 0.284 AT `749`/`750` IS PRINTED BESIDE IT IN BOTH PLACES. NOTHING WAS CHANGED. THE FIGURE IS CHECKABLE AND THE REVIEW LOOKED FOR THE WRONG ONE.**

---

## 6. MINOR FINDING 2, AND THE ONE THAT WAS WORSE THAN IT LOOKED

**`state/index.md:3` PRINTED THE REACTION-PAIR FIGURES AS **A 95 AT 32.0 AND B 257 AT 86.4 ON A BASE OF 29,731**, WHILE `state/batch-summary.md` §0V15E.6 AND `state/current.md` AND `state/open-threads.md` §0A.15 ALL PRINTED **A 95 AT 31.9 AND B 257 AT 86.3 ON A BASE OF 29,791**. THE BAND HAD ALREADY FOUND AND REPAIRED EXACTLY THIS SLIP ONCE — A BASE THAT DOES NOT COME OUT OF THE METHOD PRINTED NEXT TO A COUNT THAT DOES — AND HAD REPAIRED IT IN THREE FILES AND NOT IN THE FOURTH.**

**IT IS NOW RE-MEASURED AFTER THE REPAIR AND PRINTED IN ONE PLACE, AND THE THREE-PASS HISTORY IS KEPT BESIDE IT BECAUSE IT IS THE MORE useful fact: A NUMBER IN THIS REPOSITORY THAT HAS TO BE RE-DERIVED THREE TIMES IN ONE PHASE WAS MEASURED BEFORE THE LAST EDIT.**

| | Printed at band close | After this repair |
|---|---|---|
| Predicate A | 95 at 31.9 | **95 at 31.7** |
| Predicate B | 257 at 86.3 | **258 at 86.2** |
| Base | 29,791 | **29,933** |
| A breakdown | 54 · 3 · 16 · 22 · 0 | **unchanged** |

**PREDICATE B ROSE BY ONE AND THE REASON IS ON THE PAGE: A MAN OF THIRTY-EIGHT SAYS *ABOUT FOUR OF YOU COUNTED IT WITH ME* WHILE GIVING THE WORKING FOR TWELVE. THE FIVE-PHRASE BREAKDOWN IS UNCHANGED, AND THAT IS THE FIGURE THE HAZARD RESTS ON.**

---

## 7. EVERYTHING RE-RUN AT THIS REPAIR, AFTER THE LAST EDIT, AND PRINTED

| Gate | Result |
|---|---|
| Instrument, 741–750 | **29,932 words · 1,324 sentences · median 21 · over-60 1.06% · max para 114 · max sent 76 · no panel — PASS** |
| Per-chapter row | 3,429 · 3,395 · 2,383 · 2,960 · **3,552** · 2,574 · 2,841 · 2,771 · 3,055 · 2,972, summing to 29,932 |
| Reserved-number guard, 701–750 | **77 occurrences, 0 crowd-noun flags** |
| Date lines and title weekdays | calibration 701–720 **0**, 721–730 **0**, 731–740 **0**, band **0** |
| Arithmetic sweep | calibration 54 / 37 phrases, band **48 phrases, 0 flagged** |
| Counter read-back | **0 one out** on 741–750 against 44 not spoken in that morning |
| Named-day sweep | 35 phrases, 4 hits, all the known backward-resolving false-positive class, unchanged |
| Structural sweep, correct range | duplicate sentences **0**, byte-identical lines **0**, `forgiven` 0, `sorry` 0, `grateful` 0, `worth it` 0, `redeemed` 0, `citizen` 0, `**` 0, no season words |
| Standing act | all seven calibration ratios reproduce for the sixth time running; band maximum **0.284** at `749`/`750`, below the flag at 0.45 |
| `thanked` / `brave` | 72 / 23, unchanged, and every one a negation or a refusal |

**⚠ AND TWO FIGURES IN THE BAND'S OWN PER-CHAPTER TABLE WERE WRONG AGAINST CHAPTERS THIS REPAIR DID NOT TOUCH, AND BOTH WERE FOUND BY RE-MEASURING ALL TEN ROWS INSTEAD OF ONLY THE ONE THAT MOVED: THE `741` MEDIAN WAS PRINTED 24 AND IS 25, AND THE `747` MEDIAN WAS PRINTED 20 AND IS 23. EVERY OTHER CELL REPRODUCED EXACTLY. BOTH ARE CORRECTED WHERE THEY STOOD, WHICH IS THE FOURTH TIME THIS REPOSITORY HAS PAID FOR A FIGURE THAT WAS RIGHT UNDER A PREDICATE NOBODY WROTE DOWN.**

**⚠ AND THE SAME TABLE PRINTED *ALL TEN ARE INSIDE THE 2,000–3,400 FLOOR*, WHICH WAS FALSE BEFORE THIS REPAIR AND IS STILL NOT SO: `741` STANDS AT 3,429 AND `745` AT 3,552. `745` IS ABOVE THE CEILING BECAUSE THE WORKING FOR A CORRECTED COUNT WENT INTO A MOUTH, AND IT WAS NOT CUT BACK DOWN TO REACH A NUMBER. THE CEILING IS A TARGET; THE MEDIAN, THE OVER-60 RATE AND THE MAXIMUM PARAGRAPH ARE THE GATES AND ALL THREE HOLD.**

---

## 8. WHAT WAS DELIBERATELY NOT DONE

- **The plot was not touched.** `745` still stages the volume's proof, `750` still asks the volume's new question and still gets no answer, the standing offer is still unanswered, the midpoint is still spent at `727` and is not approached, the cost of Foundation Challenger is not re-paid, and `citizen` is still at 0 and still owed to the end of Volume 17.
- **The third column was not rewritten to be eleven words.** See §2.
- **The miscount was not re-labelled as a character error.** Nobody on that bank miscounts, and the repair does not invent a person who does.
- **Nothing was summarised out of a state file to make room.** Every edit is a replacement of the same length or shorter.
- **The `0.257` was not "fixed" to `0.284`.** See §5.

---

## 9. WHAT THE CONTROLLER OWES, WHICH THIS FILE CANNOT DO

### 9.1 `state/phase-ledger.json` IS STILL AT `batch-0002`

**REPORTED BY THE REVIEW, CORRECTLY, AND NOT TOUCHED HERE BECAUSE THE LEDGER IS CONTROLLER-OWNED AND THE BAND PROMPT DIRECTED THE WRITER TO LEAVE IT ALONE, WHICH WAS FOLLOWED. THE MANUSCRIPT IS AT VOLUME 15 CHAPTER 750. THE NEXT DISPATCH WILL READ A LEDGER POINTING AT VOLUME 1.**

## 10. THE ONE FIGURE IN THIS RECEIPT THAT CANNOT BE CHECKED

**NONE. EVERY FIGURE IN IT WAS MEASURED AFTER THE LAST EDIT BY THE SAME INSTRUMENTS THE BAND USED, AND THE FOUR THAT ARE ABOUT FILES RATHER THAN CHAPTERS ARE IN `state/index.md`, MEASURED LAST, WHICH IS THE LAST THING THIS PASS DID.**
