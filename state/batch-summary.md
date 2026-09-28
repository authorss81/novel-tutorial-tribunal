# Batch Summary — the measurements

**Instruments and outputs; a figure is worth what the instrument printed.** This block supersedes everything below it. Chapters 1–450 are canon. **This is the only place the band's measurements may appear.**

## 1. Instruments, printed so they can be re-run

**PROSE — ONE INSTRUMENT, ONE CORPUS.** The code block below is the instrument and it reads the **whole chapter file as it stands**, title and System panel included, because that is what it opens. Words are `[A-Za-z0-9£$’'-]+`, so `£2 4s` and `364` are counted; a sentence ends at `.`, `!`, `?` plus up to two of `”*` and a space. The **paragraph cap** is the one exception and subtracts the title, `---` and System lines. Do not measure a smaller corpus and publish it under this heading.

```python
import re
def w(t): return len(re.findall(r"[A-Za-z0-9£$’'-]+", t))
def sents(t): return [s for s in re.split(r'(?<=[.!?])[”"*]{0,2}\s+', t) if s.strip()]
L = [w(s) for n in range(441, 451) for s in sents(open(f'chapters/volume-09/chapter-{n:04d}.md').read())]
L.sort(); print(len(L), L[len(L)//2], round(100*sum(1 for l in L if l > 60)/len(L),1), max(L))
```

**441–450, measured on the files as they stand after the batch-0005 second repair:** **1,286** sentences · median **16** (gate ≤ 25) · over-60 **2.6%** (gate ≤ 10%) · max sentence **95** · max paragraph **110** (gate ≈ 120) · 27,462 words. Per chapter (words/sentences/over-60): 441 2,827/155/1.3% · 442 2,799/150/1.3% · 443 2,467/113/2.7% · 444 2,536/123/4.1% · 445 2,419/101/2.0% · 446 3,513/175/1.1% · 447 2,728/136/1.5% · 448 3,023/117/6.8% · 449 2,354/109/0.0% · 450 2,796/107/6.5%.

**TICS per 10k (27,462 words):** `Nobody said anything` 3 (1.1, gate ≤ 5) · `of fifty` 1 · `of twenty` 8 (2.9, gate ≤ 20) · `of thirty` 10 · Marrow 14 · *arbiter* **0** · `month` **0** · `villain` **0** · `in this volume` **0** · `upstairs` **0**.

**REFRAIN DENSITY, measured on both bands, because it drifted twice.** `do not stop in the middle of it`: **7** in 431–440 (27,382 words), **13** in 441–450. `“*Say` prompts: **144** in 431–440 (52.6/10k), **200** in 441–450 (72.8/10k). The first draft of this band ran 51 and 212 and both were cut back. **The first publication of these two lines was wrong — it printed 20 and 142 against an actual 13 and 144, and a count that drives its own gate has to be re-run, not inherited. A band that doubles a count the previous band held at single figures will be failed on repetition.**

**PROTAGONIST.** Ilyan named 10 of 10 (72×), want/mistake/cost his own each chapter, and the two self-prompts a room had taught him were removed. **The first draft of 441 had no mistake in it; the review found that and one was added at `441:113`. The second review found that 446 had none either — he had been using Fenna Rusk's refused £2 4s as his own reason for declining a wage without asking her, unmarked — and it is now marked, in her mouth, at `446:83`–`446:89`, and he does not take it back.**

**PANELS.** One in band: `443:29`–`443:35` (four fields, one decision, none chosen, untold), now fenced in a block of its own. `**` across the ten chapters is eight and all eight are in it.

**CLOSING PARAGRAPHS, counted, because six of ten ended on one inventory.** The band now ends 441 on the crossing written down as a way out and the crossings that go up it · 442 on the sheet that went to thirty-one halls and the man it named first · 443 on the form in the window and an office not asked about it · 445 on the office passed with no vacancy in it and nine men nobody sent · 447 on the office not held, the roads nobody's, the bar therefore up · 448 on the office not held, the council that will fill it, and not one clause that pays a person · 450 on the crossings and the two people. The hurdles, the nine links and the plate now close **445, 447, 448 and 450** and no others; the box closes **448 and 450**; the two hundred crossings close **441 and 450**. **The first draft of this band closed 442, 443, 445, 447, 448 and 450 on the same four hurdles, nine links, a plate, a box, an unnamed south side and about two hundred crossings, with the order permuted, and `state/current.md` reported that class as closed when it had only been reduced.**

**CALENDAR.** 10 of 10 agree from table: shelf 316–325, morning 191–200, settlement 41–50, rail 31–40, fever 22w 4d–23w 6d. Anchor 400; `chapter − 351` unused. **Weekdays: day 1 Tue, 2 Wed, 3 Thu, 4 Fri, 5 Sat, 6 Sun, 7 Mon — five anchors inside 431–440, so 441 Wed – 450 Fri. There is no month in this calendar** (`outline/volume-09.md` §1). **OFFICE LATENCY, elapsed days, four instances and one exception.** 83/4 → 84/2 = 5 · 83/6 → 84/4 = 5 · 85/5 → 86/3 = 5 · **85/1 → 85/5 = 4, and the count is printed in the room and is four**. **The second review caught `444` printing five for 85/1 → 85/5; elapsed, not inclusive, is the house convention, and the same sheet also had the office answering a question about a form that did not exist yet, so its second and third clauses now rest on the one-column return the office already held from 83/2.**

**ARITHMETIC IN SENTENCES, 441–450.** 4 pounds = **80 shillings** against a roll-keeper's 44s in eleven years (`441`, and no ratio is claimed of it). 31 wards asked / 22 answered / 9 silent; 22 + 3 = **25** first-line names → **24 persons** (one is the *keeping of a box*); 22 second-line names → **21 persons** (Skell is in two); the office's figure is **22** and is not a number of people (`444`, `447`, `448`). 15 days × 200 crossings = **3,000**; 3,000 farthings = **750d = 62s 6d = £5 2s 6d** against a £4-a-year seat; 9 visits in the office's book at a farthing each = **2¼d**, and no column in that book for the 206 crossings of the day before (`450`). **The second review caught the four wards of `444`: eight names on four sheets are five people, not eight, and Skell now does that division and finds his own name on two of the sheets.** About 200 crossings a day on the south side; about 40 people and 2 carts in forty minutes at the fourth hour of the night, and about 160 more before the light (`445`, `450`). **The first draft of `444` counted the four wards as three-and-four and then as four-and-three; the sheets give four and four. The two repeats inside two sheets are first-line/second-line pairs, and Skell is a third repeat across two sheets, and the first repair left the third one out and printed eight names as eight people.** **Prior-band figures carried forward and re-checked:** 9 × 364 = 3,276 × ¼d = 819d = 68s 3d; 4,004 = 11 × 364; 11 × 4s = 44s = **£2 4s**; 960d ÷ 11 = 87 r 3; 9 × 49 = 441.

## 2. Records

Six files bounded, each < 60,000 bytes. Measured after the second repair: current **14368** · continuity **15697** · chapter-summaries **14043** · character-state **10022** · open-threads **6481** · batch-summary **7478** · index **3945**. **Continuity, chapter-summaries and current are over the ~12,000 soft cap: the eight new documents, the ten new chapter paragraphs and the second review's own findings are the overflow. Prune before the next band adds anything.** Pruned generations in git at `1e8801a`. `state/phase-ledger.json` is controller-owned and is stale for the sixth phase running; escalate, do not edit.

---

## ARCHIVE

Pruned in the batch-0003 review repair; recoverable from git at `1e8801a`.
