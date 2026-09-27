# Batch 0002 Review Fixes — Volume 08 (Chapters 361–370)

**Source of findings:** `logs/batch-0002.review.log`, produced by the review phase over commit
`cd89673` (*novel: save writer work batch-0002*). The reviewer ran the project's own instruments
itself, reproduced the calibration exactly, and confirmed findings 1–9 by opening the text.

**Scope of this file:** what was changed, what was deliberately not changed, and what the next
phase must not inherit. The narrative of the review and the repair is §8 of the top block of
`state/current.md`, which is the authority; this file is the receipt.

**Verdict:** *the band stands and the arithmetic inside it did not.* Nothing in this repair changed a
plot, a character, an outcome, a motivation, a chapter title or the planned shape of anything. Two
figures changed, one division was replaced by the multiplication it should always have been, one
name came back, one list stopped restating itself, and everything else is a line.

---

## 1. The five critical findings

| # | Finding | Action |
|---|---|---|
| 1 | **`0363:21` printed a division that does not produce its own answer.** *About thirty doors a fortnight … about two doors a day, and two doors a day is the whole of it. That is the rate. Two doors a day, nine hundred doors, so two doors a day for nine hundred doors is four hundred and twenty days.* Nine hundred divided by two is 450. 420 is 30 × 14. **This is the volume's spine figure** — it is quoted in `0363`, `0365`, `0367`, `0370` and was carried into `batch-0003/PROMPT.md` §3 as canon with the bad working attached. | The working is now the multiplication: *thirty doors in a fortnight is two doors a day and a seventh of a door, and that is the rate and I have never once rounded it. Thirty doors takes a fortnight. Nine hundred doors is thirty of those. Thirty times fourteen days is four hundred and twenty days.* **Every downstream figure is untouched** — 420, 364, the difference of 56, the year and fifty-six days, 234, the 12⅖ days of `0370:75`. `0363:39`'s flat *Two doors a day* became *Two doors a day and a seventh*, because she has just said she never rounds it, and `0363:99`'s closer now says thirty doors in a fortnight. `chapter-0355.md:39` already had the multiplication and was never wrong; it is now cited as the authority. |
| 2 | **`0365:29` said *Twelve shillings of plate for the names that are on a paper and not on a plate in this ward*** — which is this ward's **two** hundred names, and two hundreds at 4s is **eight** shillings, printed flat four chapters earlier at `0364:27` and again at `0361:123`. Twelve shillings is the 300-name plate, so 282 − 144 = 138 was correct for a figure the sentence did not describe. | The sentence now names all three. *Eight shillings of plate for the two hundred names in this ward … Twelve shillings of plate for the three hundred names that are in the fair hand on your second floor. And a hundred and thirty-eight pence between a date at this bench and that twelve shillings, and a hundred and eighty-six pence between a date at this bench and this ward's eight.* **138 survives**, and 186 is new, and 234 at `0367:89` is untouched. Three different subtractions off one base of 282 is not an inconsistency; a subtraction whose two terms the sentence does not identify is. `0365:99` now says *two differences off one bench date*. |
| 3 | **`0370:63` said *that is ten days* and `0370:75` said *I have been going eleven days*, twelve lines apart, in one speech.** The ten is right and the eleven is wrong — **the reviewer's own count of twelve is also wrong, and the chapter proves it**: nine marks on the first morning is **three days of chalk at three marks a day**, so twenty-seven marks fall over seven chalked days, plus the three unmarked days, is ten. `0368:111`'s *whose chalk ran out yesterday* and `0370:63`'s *three of them were today and yesterday and the day before* both land on the same ten. | `0370:75` now says **ten days**. Its two-door-a-day conversion was rebuilt on the round's real rate while the line was open: *at thirty doors a fortnight twenty-seven doors is twelve days and three-fifths of a day of that round* (27 ÷ 30 × 14 = 12.6). The old figure was 13½ at 2 a day, which is a different measure of the same 27 doors. |
| 4 | **`0364:69` put a clerk of forty in a public room on the seventh morning** writing the fair hand. The clerk of thirty describes that same act in his own mouth at `0361:49`. A repair two chapters earlier in the same file had already caught an attribution slip at `0364:51` and missed this one. | *a clerk of thirty*. The two clerks are distinct people and both still appear — the clerk of thirty at the desk, the clerk of forty at the end of the long table in `0365` — so the band now runs 18 and 5 and no reader has to reconcile an age that moves. |
| 5 | **`0369:61` and `0370:29` shared a near-verbatim clause**, and `0370:21–33` was a thirty-three-line list that restated `0369:73–79` and added no fact. | `0370:21–33` now **counts** the four things instead of re-narrating them, and the duplicated clause is gone. It is shorter, it is not a summary of the chapter before it, and it carries two facts the old list did not: the stranger's *price* was written down as well as his sentence, and the woman of forty-four was asked eleven questions and some more than were on the sheet. The word *anchor* is held at two, as the next band's prompt requires. |

## 2. The four major findings

| # | Finding | Action |
|---|---|---|
| 6 | **Residuals of the day-count class the first repair claimed to have closed.** `0367:59` still read *in seventeen days* on his sixteenth; `0366:37` still read *thirteen days* against `0366:99`'s *fifteen days* **in the same chapter**. | Fixed. A full sweep of every `N days` in the band against `chapter − 351` found **one more of the same fault the review did not flag**: `0362:99`'s *nine days ago* for the roll-room scene at `355`, which is **seven** days ago and which `0369:41` already gives as fourteen. Fixed too. Every remaining duration now reconciles — see §4. |
| 7 | **Fenna Rusk is named at `0360` and then never named in the ten chapters where she is the subject** — only *the woman of forty-four* and *the woman at the table*. Sera Quill gets named once at `0370:15`. | Her name is back in **twice**, in the two places the cost of putting it there is felt: `0363:7`, where he is alone in her room for the first time in the band, and `0369:33`, on the day she is in a room being examined. Neither is a reveal. Both are the same fact he has been carrying since his tenth morning, stated by the only person who can state it about him. |
| 8 | **`batch-0003/PROMPT.md` contradicted itself on its own instrument figures.** §4.2 listed Chapters 361–370 as `16/32` and `343/747` — Batch 0001's numbers — and then gave the right ones in the next clause of the same sentence. §4.3 said 22,890 words against a measured 22,889. §4.1 attributed *fifteen* to Batch 0002 when the second-check figure is sixteen. The list was numbered 1–6, 7, 7, 9. | All corrected against the chapter files, and the money table in §3 now carries **the multiplication** for the round plus explicit rows for **138** and **186**, with the rule stated: a difference must name the two things it is a difference between. §4.7 now also runs `(the\|this\|rest of the) (volume\|chapter\|band\|novel\|reader\|story)`, because §5 of this repair found an apparatus leak that none of the three standing phrases could see. |
| 9 | **Two figures in `state/current.md` §2 disagreed with the chapter files in the same commit** — `correct` was claimed at **six** and is **nine**, and `it took` was claimed at *twelve in Batch 0001* and is **eight** over 351–360. | Corrected, and the top block of `state/current.md` now carries measured figures only. §4.7 of the next prompt now says to run the cased forms separately, because a case-insensitive count of `correct` returns nine and uppercase `CORRECT` returns zero, and reading the first as the second reports a prohibition break that is not there. |

## 3. The five minor findings

| # | Finding | Action |
|---|---|---|
| 10 | **The apparatus tic recurred; `0361:89` was the worst** — *because a chapter about a thing that cannot be done is not finished by the not-doing.* | Cut to *a thing*. The same sweep found `0365:103`'s *he was going to be carrying the piece of paper **for the rest of the volume***, which none of the three standing apparatus phrases in §4.7 matched. Cut to *for as long as he was in this city*. Both pattern families are now zero. **The frame itself — *Here is the whole of it* — is untouched and is not a tic.** It is the band's structural device, it is defended in the band prompt, and Volume 07's last two bands do not use it, which is the actual contrast. |
| 11 | **`0369:75` and `0370:33` were a near-duplicate triple-negative litany, and `0370:33` added *redeemed*** — an abstract the book has not earned. | `0370:33` is now *And nothing else came out of it, and no other thing in this city is going to come out of it, and there is no office that would be told.* `redeemed` is at zero over the band. |
| 12 | **Six chapters closed on the same bells-did-not-stop litany.** | Two were varied: `0365:105` is *the four bells went at the change and there is nothing in this city that stops for them*; `0366:107` is *the four bells went over the low end of the ward the way they do*. The motif now opens at `361` and closes at `370`, which is where it belongs, and the exact pairing runs four times instead of six. |
| 13 | **Ilyan and Tarin Keel converged in `0364`** — the chapter whose subject is their disagreement stated one argument three times. | The four-sentence summary at `0364:59–71` is now two paragraphs instead of five: each man's method is stated once, with its cost, and the chapter's remaining beats carry it. `0364:91`'s third telling of the corridor-and-the-room is cut and the *no third thing between the two of them* line stands alone. The exchange at `0364:85–87` — *both of those are the same ignorance with a different coat on* — is the best writing in the chapter and is untouched. |
| 14 | **The protagonist pays nothing.** | `0365:97`'s *and it cost him nothing and it is the reason there is any point to the room at all* is now *and it was the only instrument he has and it costs him and it is the only one, and this was the first time in fourteen days that using it had cost him nothing at all, and he worked out why on the walk down the hill, and it was because he had not had to do anything, because a man whose job it is had already done it.* The instrument still costs. This use of it is free, and the reason is the finding. **The reviewer's other two citations do not survive checking**: `0367:53–65` says in as many words that the instrument has cost a woman at a bar, has cost him twice, and costs the same here, and `0369:47`'s *it did not improve* is about the instrument, not about him. |
| 15 | **`state/phase-ledger.json` still reads `currentPhase: batch-0002`, volume 1, chapters 11–20, `status: planned`.** | **Not touched. It is controller-owned** (`state/phase-ledger.json` is in the do-not-edit list in `AGENTS.md`) and this phase has no business writing to it. Flagged here so it is on the record and so the controller's own next dispatch is the thing that moves it. |

## 4. What was checked and found already correct

- **The days-in-city sweep.** Every `N days` / `N mornings` / `N weeks` in the ten chapters was
  extracted and checked against `chapter − 351` (elapsed) and `chapter − 250` (morning ordinal).
  All ten morning ordinals are right. All ten *the fourteenth was N days off* figures are right
  (`370 − ch`). The fever at `363` (eighty days = eleven weeks and three days) and at `366`
  (eighty-three days = eleven weeks and six days) are right, and the order at Shelf day 172 is
  right. `0365:11`'s seven mornings back to the candle bill at `358`, `0365:69`'s five days back to
  the yard at `360`, `0365:41`'s two days back to `363`, `0367:53`'s eight days back to `359`,
  `0368:47`'s five days back to `363`, `0369:41`'s fourteen days back to `355`, and `0370:53`'s six
  days back to `364` all reconcile.
- **`0362`'s *nine days* is NOT an error and was deliberately left alone.** It is the woman of
  thirty-four counting the mornings she has seen him at her own door — a count she owns — and it
  lines up with `0361:137`'s *the first question anybody in that ward had asked him in eight days*
  one day earlier. He concedes it out loud (*Nine. The counting is not exact and the arithmetic
  is*), which is the text marking it as her imprecision. **A count a character owns is not the
  book's count and must not be corrected against `chapter − 351`.** This is now written into
  §4.8 of the next band's prompt, because a repair that corrects it will break a working passage.
- **The chalk ledger, recomputed from `0361` forward.** Nine days bought with a penny, three marks
  to the day, nine marks on the first morning — which is **three** days of chalk on day one, and
  that is the fact the reviewer's count of twelve missed. End of day 1: six days left (printed at
  `0362:5`). End of day 3: four days left (printed at `0363:99`). Start of day 6: two days and six
  doors (printed at `0366:29`). End of day 7: nothing, which is his hundred and seventeenth morning,
  and `0368:111`'s *ran out yesterday* and `0370:63`'s *went on three days ago* are both that day.
  Twenty-seven marks. Ten days gone. The chain closes.
- **All the prohibitions, re-run after the repair.** `**bold**` 0, no panel spent, `this chapter` /
  `this volume` / `the band` 0, and the wider apparatus pattern 0, `arbiter` 0, `Remedy Drafter` 0,
  `healer` 0, `stone` 0, `system` 0, `stage` 0, `panel` 0, `seam` 0, `the reader` 0, `redeemed` 0,
  `first witness` 0, `Draymoor` 0, `rendering`/`rendered` 0, `vault|cave|ruin|temple|battlefield|
  relic|treasure` 0, `conspiracy` 0, `corrupt` 0. Weekday 0. Month-word = the modal verb *may*
  and nothing else, at two. `[0-9]` outside the ten heading lines: 0. Uppercase `CORRECT` 0;
  `correct` in any case 9, all nine the ordinary English word, now stated as nine.
- **Quotation and emphasis glyphs, all ten files, line by line.** `0361:79` was an unclosed
  *“\*No.\** with no closing mark; it is closed. `0370:67` carried a stray straight `"` inside a
  quotation; it is gone. Every line in the band now balances `“` against `”` and carries an even
  number of asterisks.

## 5. The instruments, re-run on the chapter files after this repair

The calibration is run first and reproduces all four published figures: `volume-07` 331–340 returns
122/254 at seventy characters and 1,201/2,817 at forty; 341–350 returns 534/1,081 and 1,837/4,285.

| Set | Seventy characters | Forty characters |
|---|---|---|
| **CALIBRATION, Volume 07 Band 0004 (331–340)** | **122 / 254** | **1,201 / 2,817** |
| **CALIBRATION, Volume 07 Band 0005 (341–350)** | **534 / 1,081** | **1,837 / 4,285** |
| Volume 08 Band 0001 (351–360) | 16 / 32 | 343 / 747 |
| **THIS BAND, 361–370, ON DELIVERY** | 199 / 398 | 992 / 2,166 |
| **THIS BAND, 361–370, AFTER THE FIRST REPAIR** | 213 / 426 | 1,023 / 2,228 |
| **THIS BAND, 361–370, AFTER THIS REPAIR** | **171 / 342** | **942 / 2,066** |

**342 ÷ 171 IS EXACTLY TWO**, so not one seventy-character window in the band occurs three times,
and that invariant has now held through three passes. The fall from 213 to 171 is not a discipline
loss: it is a list that stopped restating itself and a clause that stopped being printed twice.
Hedge **19 in 22,996 words, one in 1,210**, against Volume 07's five bands at 206 / 88 / 118 / 92 /
48 and a volume target under four hundred. Clock 22. `it took` 6, against Volume 07's 7 / 15 / 10 /
14 / 17 and Batch 0001's 8.

## 6. What the next phase must not inherit

1. **138, 186 and 234 are three different subtractions off one base of 282 and none of them
   contradicts another.** Do not let a sentence name a difference without naming its two terms.
2. **The round is thirty lots of a fortnight. It is never nine hundred divided by two.**
3. **The woman of twenty-eight has been going ten days, seven chalked and three not.** The chalk
   ran out at the end of his hundred and seventeenth morning. `batch-0003/PROMPT.md` said
   *eighteenth morning*; that was wrong and is now *hundred and seventeenth morning*.
4. **Fenna Rusk is named.** She is `Fenna Rusk` in narration and *the woman with the book* or
   *the woman at the table* in her own mouth, and the two are not used in the same sentence.
5. **A count a character owns is not `chapter − 351`.** `0362`'s nine days is hers.
6. **The bells open the band at `361` and close it at `370`.** Four exact pairings in between.
7. **The two clerks are thirty and forty and are different men.** Do not merge them.
8. **`state/phase-ledger.json` is stale and is not ours.** Volume 1, chapters 11–20, `planned`. The
   controller moves it, not a writer.
