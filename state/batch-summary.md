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

**441–450, measured on the files as they stand after the batch-0005 review repair:** **1,271** sentences · median **16** (gate ≤ 25) · over-60 **2.0%** (gate ≤ 10%) · max sentence **91** · max paragraph **110** (gate ≈ 120) · 26,734 words. Per chapter (words/sentences/over-60): 441 2,807/157/1.3% · 442 2,790/150/1.3% · 443 2,463/113/2.7% · 444 2,460/122/2.5% · 445 2,375/102/0.0% · 446 3,316/167/1.2% · 447 2,603/130/0.8% · 448 2,815/114/5.3% · 449 2,351/109/0.0% · 450 2,754/107/5.6%.

**TICS per 10k (26,734 words):** `Nobody said anything` 3 (1.1, gate ≤ 5) · `of fifty` 1 · `of twenty` 8 (3.0, gate ≤ 20) · `of thirty` 10 · Marrow 14 · *arbiter* **0** · `month` **0** · `villain` **0** · `in this volume` **0** · `upstairs` **0**.

**REFRAIN DENSITY, measured on both bands, because it drifted once.** `do not stop in the middle of it`: 7 in 431–440, **20** in 441–450. `“*Say` prompts: 142 in 431–440 (51.9/10k), **197** in 441–450 (73.7/10k). The first draft of this band ran 51 and 212 and both were cut back. **A band that doubles a count the previous band held at single figures will be failed on repetition; measure, do not inherit.**

**PROTAGONIST.** Ilyan named 10 of 10 (72×), want/mistake/cost his own each chapter, and the two self-prompts a room had taught him were removed. **The first draft of 441 had no mistake in it; the review found that and one was added at `441:113`.**

**PANELS.** One in band: `443:29`–`443:35` (four fields, one decision, none chosen, untold). `**` across the ten chapters is eight and all eight are in it.

**CALENDAR.** 10 of 10 agree from table: shelf 316–325, morning 191–200, settlement 41–50, rail 31–40, fever 22w 4d–23w 6d. Anchor 400; `chapter − 351` unused. **Weekdays: day 1 Tue, 2 Wed, 3 Thu, 4 Fri, 5 Sat, 6 Sun, 7 Mon — five anchors inside 431–440, so 441 Wed – 450 Fri. There is no month in this calendar** (`outline/volume-09.md` §1).

**ARITHMETIC IN SENTENCES, 441–450.** 4 pounds = **80 shillings** against a roll-keeper's 44s in eleven years (`441`, and no ratio is claimed of it). 31 wards asked / 22 answered / 9 silent; 22 + 3 = **25** first-line names → **24 persons** (one is the *keeping of a box*); 22 second-line names → **21 persons** (Skell is in two); the office's figure is **22** and is not a number of people (`444`, `447`, `448`). 15 days × 200 crossings = **3,000**; 3,000 farthings = **750d = 62s 6d = £5 2s 6d** against a £4-a-year seat; 9 visits in the office's book (`450`). About 200 crossings a day on the south side; about 40 people and 2 carts in forty minutes at the fourth hour of the night, and about 160 more before the light (`445`, `450`). **The first draft of `444` counted the four wards as three-and-four and then as four-and-three; the sheets give four and four, and the two repeats are first-line/second-line pairs inside two sheets, not duplicates among the second lines. The review caught the second error and the first repair introduced it.** **Prior-band figures carried forward and re-checked:** 9 × 364 = 3,276 × ¼d = 819d = 68s 3d; 4,004 = 11 × 364; 11 × 4s = 44s = **£2 4s**; 960d ÷ 11 = 87 r 3; 9 × 49 = 441.

## 2. Records

Six files bounded, each < 60,000 bytes. Top blocks: current 11,921 · batch-summary 4,318 · continuity 13,900 · chapter-summaries 12,599 · character-state 8,851 · open-threads 5,996 · index 3,520. **Continuity and chapter-summaries are over the ~12,000 soft cap because of the eight new documents and the ten new chapter paragraphs; the index says so, and the next band prunes rather than adds.** Pruned generations in git at `1e8801a`. `state/phase-ledger.json` is controller-owned and is stale for the sixth phase running; escalate, do not edit.

---

## ARCHIVE

Pruned in the batch-0003 review repair; recoverable from git at `1e8801a`.
