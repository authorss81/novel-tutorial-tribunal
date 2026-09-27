# Batch 0001 Review Fixes — Volume 08 (Chapters 351–360)

**Source of findings:** `logs/next-0003.review.log`, produced by the phase that ran on the generic
continuation prompt at `workspace/continuation/next-0003/`. **That log contains no findings.** The
review agent fell back to the default writer agent, began an inspection, and was killed mid-command,
so what exists in that file is a transcript of a session that never reached a verdict. The findings
below were therefore produced by running the band's own declared instruments against the chapter
files and reading the band against the outline that the same phase wrote.
**Scope of this file:** what was changed, what was deliberately not changed, and what the next phase
must not inherit. The narrative of the review and the repair is §11 of the top block of
`state/current.md`, which is the authority; this file is the receipt.

**Verdict:** *the prose is sound and the record of the prose is not, and in fifteen sentences of the
prose too.* That is the same verdict the Volume 07 close review reached, and it is the sixth time
this project has arrived at it. Nothing in this repair changed a plot, a character, an outcome, a
motivation or the planned shape of anything. Every prose edit is a figure.

---

## The nine findings

| # | Finding | Action |
|---|---|---|
| 1 | **The span scan's calibration named the wrong file set and one of its four published figures does not reproduce.** §3.1 said `chapter-0331.md`–`chapter-0334.md` returns 122/254 at seventy characters. It returns 39/78. The set that returns 122/254 and 1,201/2,817 is Band 0004 in full, `chapter-0331.md`–`chapter-0340.md`. The fourth figure, 1,838/4,287 at forty for Band 0005, measures 1,837/4,285. | Corrected in `state/current.md` §3.1 and in `workspace/volume-08/batch-0002/PROMPT.md` §4.2, with the method now declared whole — including the one previously undeclared decision, that **the heading line stays in the tally**, which is worth two figures at forty. The line no longer claims four exact reproductions. |
| 2 | **The band's own figure at forty characters was wrong by seven.** 350/761 printed; 343/747 measured. | Corrected in three files. |
| 3 | **The word count and the rate beside it were measured under a different method from the one declared.** The declared method includes the heading line and returned 21,655 as delivered and returns 21,645 after this repair's fifteen figure-edits. The printed 21,528 is the same count with the ten heading lines removed. The hedge count of sixteen is right. | Corrected in `state/current.md` §3.3, `state/batch-summary.md` item 3, `state/continuity.md` §6.15 and the batch-0002 prompt §4.3. Both counts are now printed so the mistake cannot be made twice. |
| 4 | **Four more instrument figures were off by small amounts.** The word *nine* on a word boundary is 103, not 102; the substring count is 121, not 124; `stone` is ten, not eleven; the italic inventory is 300 spans, not 304. | Corrected in place at §3.6, §3.9, §3.11 and in `state/batch-summary.md` item 11. Each correction is marked where it is made. |
| 5 | **The band's own count of the days he had been in the city was wrong in seven places — the finding that matters.** | Fifteen sentences corrected across Chapters 352, 353, 355, 357, 358 and 360, and every downstream copy in the six state files. See the table below. |
| 6 | **A figure in Chapter 352 contradicted the entire band.** Magistrate Rell said she wrote the order *in the fifth week when I had about nine hundred of them dead*, against about a hundred and forty dead everywhere else, and nine hundred is Tallowgate's door count. The same sentence contradicted the clerk's *the order has been up since the second week* two pages later. | `352:81` is now the **third** week and **about forty** of them dead, which is what `state/continuity.md` §2.14 and §3.1 already said and what makes the order's eight weeks fit; `352:103` is now *since the third week*. Nine hundred is at zero over the band. |
| 7 | **The eleventh week was a week-ordinal where the book needed a count.** *This eleventh week* and *when the water came in the eleventh week* both collided with the eleventh week of the Shelf year, which is 230 days before the band opens, while the same chapters and three state files say the water came eleven weeks ago. | `353:9` and `355:39` corrected; `outline/volume-08.md`'s money table and `state/continuity.md` §1 carry the count. The number eleven is right; the ordinal was the error. |
| 8 | **An age was wrong in Chapter 354 and it named the wrong person.** The second name on the witness sheet was *a man of forty-four who works in a yard at the low end of Tallowgate*, and the next line says the Bench wants anybody who can say what a plate is for — Bevin Tarr, **fifty-nine**, twice established. The only other man of forty-four in Tallowgate is Ivo Serrel, in a room, who cannot leave. | `354:79` is now **fifty-nine**, which is what two state files already said. |
| 9 | **The record asserted three things the chapters do not contain, and a fraction that contradicts the band's own arithmetic.** | See the second table below. |

---

## Finding 5 in full: the seven day-count errors

The band fixes its own calendar in the text. He arrives at the gate at the seventh hour of Shelf day
226; Chapter 360 calls itself the tenth morning; the fever has been going eleven weeks; the order was
signed in the third week and is up eight. So **days-in-city = morning ordinal less one.**

| Place | Printed | Correct | Why |
|---|---|---|---|
| `352:3` | *the second day of a fever in two low wards* | *the second day of his being in a city with a fever in two low wards* | As written, the fever was two days old. It was eleven weeks old. |
| `355:17` | *been in this city three days* (×2) | **four** | 355 is his fifth morning. |
| `355:85` | *you have now been in it three and I would like it to be four* | **four … five** | Same scene, same speaker, same count. |
| `357:7` | *on the ninth day of his time in this city* | **seventh** | 357 is his seventh morning. |
| `358:53` | *nine days* (×3, in one speech) | **seven** | 358 is his eighth morning. |
| `358:59` | *the thing he has carried for eight days* | **seven** | Consistency with the same morning. |
| `358:81` | *you have found that out in nine days* | **seven** | Same. |
| `360:21` | *a man who has been in a city three days* | **nine** | 360 is his tenth morning. |

**Two of these were not day phrases at all and were left alone**, and the distinction is the lesson:
*four days on a road* at `351:3`, `352:61`, `352:85`, `352:97`, `354:15` and `357:91` is the **road**,
and it is correct everywhere it appears; and *if he had come in here on the second morning* at
`358:61` is a **counterfactual** Fenna offers about a visit that did not happen, and it is correct
too. A band that had "fixed" those would have broken six correct sentences to repair seven wrong
ones.

**The finding underneath the finding.** The batch-0002 prompt told the next writer that *Batch 0001
had one back-reference to check and it was right.* The truth is that **the band had seven wrong day
phrases in ten chapters, and not one of them was a back-reference to an earlier volume — every one
was the band's own internal arithmetic.** The project's third question, *is the named day the day the
event happened on*, has found back-references thirty-three times across Volumes 05 and 06 and
twenty-four times in Volume 07. It has now found a band's own day count seven times in ten chapters,
which is the highest rate in the record. The prompt now carries the rule that catches it: **write the
day column down before the chapter, and put every day phrase in it beside the chapter's own day.**

---

## Finding 9 in full: three things the record asserted that are not in the chapters

1. **A healer of about sixty** is described in `state/continuity.md` §1 and `state/open-threads.md`
   item 12 as having named the fever in about nine words and been right. **The word *healer* is at
   zero over Chapters 351 to 360.** There is no such scene in Chapter 355 or anywhere else. Both
   entries now say he is one of the six people of this volume, is not in the band, and is still owed
   his nine words. `outline/volume-08.md` carried the same guess — *in Chapter 355 or thereabouts* —
   and is repaired to match.
2. **`outline/volume-08.md` prohibition 10** claimed the band's test is that *Chapter 353 says out
   loud that a man in that room was born in that street.* No such sentence is in Chapter 353 and
   never was. The chapter does the work by another route — the man gives his own name before there is
   a question in it at `353:35`, has been in the room six years, and the head of his house has been
   putting himself in the book twice a year for six years at `353:43` — and
   `state/current.md` §7 and `state/open-threads.md` part three item 7 both described **that**,
   correctly. The outline was the thing out of step and is repaired to the chapter, with the lines.
3. **A fraction that cannot stand with the band's own arithmetic.** *About a third of the people in
   this city do not sleep in a house* (`352:121`) and *about a third of the people in two wards are
   not in the roll* (`354:17`) cannot both be true alongside *three hundred names short across four
   wards* (`357:13`) and a Ninth Weir that is a mile of yards: a third of ninety thousand is thirty
   thousand. Now *a great many people in this city* and *a good many people in two wards* — the
   first is the phrase the woman at the standpipe already uses in her own mouth at `353:19`. The
   collision goes and the three hundred, which is Batch 0002's to find, is not given away early.

**And two more claims of the same kind, repaired in the same pass:** `outline/volume-08.md` described
Bess Carrow as *nine days better* when `359:51` says nine days **in the hall** and better for six of
them; and it said Ilyan notices the panel *four days later* and writes it *in a penny exercise book*
when `360:84` and `360:86` have him notice it the same afternoon and write one line on the back of a
candle bill. Three state files carried the delivered form and the outline carried the plan, and the
chapters are right.

---

## Finding 12, which is a trap rather than an error

`workspace/volume-08/batch-0002/PROMPT.md` listed **`CORRECT` in any case** among the patterns that
must come back clean. It is not zero in any case and is not supposed to be: it is zero in UPPERCASE,
which is what prohibition 15 is about and what `outline/volume-08.md` §15 actually says, and
`correct` in any case is **eleven**, all eleven the ordinary English word. `state/current.md` §3.7 had
this right from the moment the band was written. **A band that obeyed the prompt literally would have
cut eleven good uses of an ordinary word out of dialogue to satisfy a pattern that was never the
prohibition.** The prompt now measures uppercase and reads the eleven.

---

## What was deliberately not changed

- **No prose was restarted and no scene was rewritten.** Fifteen sentences, every one a figure or a
  count. The batch's findings, its structure, its climax at `360`, its one panel, its money and its
  refusals are untouched.
- **No archive block was edited in any of the six state files.** Only the top block of each, and
  every correction is marked in place with the reason and the measurement.
- **Nothing was pruned.** This phase wrote no prose, which is the only condition under which the
  standing recommendation to delete a superseded generation could be acted on, and it is still not a
  standing permission and is still a human's decision. The repair made the record 18,228 bytes
  larger and says so.
- **No phase prompt was created and no marker was written.** `workspace/volume-08/batch-0002/` was
  already on disk and correct, and this review left its structure alone.
- **No controller file was touched:** not `scripts/`, `.github/workflows/`, `.opencode/agent/`,
  `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json` or
  `state/phase-ledger.json`.
- **`bible/characters.md:45` is still wrong about Tarin Keel's age** — forty-six against fifty-two in
  the chapter files — and it was not this phase's to fix, and the chapter files win.
- **The barwoman's age split and the man of about seventy-four's two *since* dates** at `317:15` and
  `336:49` are both still open and neither is in this band.

## What the next phase must not inherit

Run every scan against the chapter files. The calibration in the batch-0002 prompt is now the one
that reproduces, and three of its four published figures are exact and the fourth misses by one
window and two occurrences, and the prompt says so rather than pretending otherwise. The word count
is 21,645 with the heading lines in, which is 21,655 as the band was delivered. The span scan at forty is 343/747. `correct` in any case is
eleven and that is correct. **The number of days he has been in the city is the morning ordinal less
one, and his four days on a road are the road.**
