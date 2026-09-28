# Batch Summary — the measurements

**Instruments and outputs; a figure is worth what the instrument printed.** This block supersedes everything below it. Chapters 1–440 are canon.

## 1. Instruments, printed so they can be re-run

**PROSE — ONE INSTRUMENT, ONE CORPUS.** The code block below is the instrument and it reads the **whole chapter file as it stands**, title and System panel included, because that is what it opens. Words are `[A-Za-z0-9£$’'-]+`, so `£2 4s` and `364` are counted; a sentence ends at `.`, `!`, `?` plus up to two of `”*` and a space. The **paragraph cap** is the one exception and subtracts the title, `---` and System lines. Do not measure a smaller corpus and publish it under this heading.

```python
import re
def w(t): return len(re.findall(r"[A-Za-z0-9£$’'-]+", t))
def sents(t): return [s for s in re.split(r'(?<=[.!?])[”"*]{0,2}\s+', t) if s.strip()]
L = [w(s) for n in range(431, 441) for s in sents(open(f'chapters/volume-09/chapter-{n:04d}.md').read())]
L.sort(); print(len(L), L[len(L)//2], round(100*sum(1 for l in L if l > 60)/len(L),1), max(L))
```

**431–440, re-measured after the batch-0004 review repair:** **1,133** sentences · median **18** (gate ≤ 25) · over-60 **7.2%** (gate ≤ 10%) · max sentence **85** · max paragraph **120** (gate ≈ 120) · 27,382 words. Per chapter (words/sentences/over-60): 431 3,190/139/5.8% · 432 2,401/95/5.3% · 433 2,386/108/2.8% · 434 2,381/88/12.5% · 435 2,976/124/7.3% · 436 2,795/113/9.7% · 437 2,506/108/6.5% · 438 2,856/105/8.6% · 439 2,636/109/9.2% · 440 3,255/144/6.2%.

**TICS per 10k (27,382 words):** `Nobody said anything` 1 (0.4, gate ≤ 5) · `of fifty` 0 · `of twenty` 11 (4.0) · `of thirty` 5 · Marrow 0 · *arbiter* 0.

**PROTAGONIST.** Ilyan named 10 of 10 (103×), want/mistake/cost his own each chapter.

**PANELS.** One in band: `435:45`–`435:51` (four fields, one decision, none chosen, untold). `**` count across ten is eight, all there.

**CALENDAR.** 10 of 10 agree from table: shelf 306–315, morning 181–190, settlement 31–40, rail 21–30, fever 21w 1d–22w 3d. Anchor 400; `chapter − 351` unused. **Weekdays: day 1 Tue, 2 Wed, 3 Thu, 4 Fri, 5 Sat, 6 Sun, 7 Mon — five anchors inside the band, so 431 Sat – 440 Tue. There is no month in this calendar** (`outline/volume-09.md` §1).

**ARITHMETIC IN SENTENCES.** 9 × 364 = 3,276 visits × ¼d = 819d = 68s 3d (`435`); 819 ÷ 48 = 17 + 1/16 (`424`); 819 ÷ 240 = 3 days + over 3 (`424`); 4,004 = 11 × 364; 11 × 4s = 44s = **£2 4s** (`436`, correcting £4 4s = 84s = 21 years); 4 lb = 960d; 960 ÷ 11 = 87 rem 3 (`439`); 9 × 49 = 441 (`422`). `405:43` still overstates first row (outside phase; `412:55` right).

## 2. Records

Six files bounded, each < 60,000 bytes, top blocks ≤ ~12,000. Pruned generations in git at `1e8801a`.

---

## ARCHIVE

Pruned in the batch-0003 review repair; recoverable from git at `1e8801a`.
