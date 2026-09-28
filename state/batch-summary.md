# Batch Summary — the measurements

**Instruments and outputs; a figure is worth what the instrument printed.** This block supersedes everything below it. Chapters 1–440 are canon.

## 1. Instruments, printed so they can be re-run

**PROSE.** Sentences split after `.`/`?`/`!` plus up to two of `”*` and a space. Words `[A-Za-z’'-]+`. Paragraph cap counts blocks between blanks, minus title, `---`, System lines.

```python
import re
def w(t): return len(re.findall(r"[A-Za-z’'\-]+", t))
def sents(t): return [s for s in re.split(r'(?<=[.!?])[”"*]{0,2}\s+', t) if s.strip()]
L = [w(s) for n in range(431, 441) for s in sents(open(f'chapters/volume-09/chapter-{n:04d}.md').read())]
L.sort(); print(L[len(L)//2], round(100*sum(1 for l in L if l > 60)/len(L),1), max(L))
```

**431–440 NOW:** 27,364 words; 1,132 sentences; median **17** (gate ≤ 25); over-60 **7.1%** (gate ≤ 10%); max sentence **84**; max paragraph **120** (gate ≈ 120). Per chapter: 431 3,184/14/6.5% · 432 2,402/21/5.3% · 433 2,375/16/2.8% · 434 2,378/20/12.5% · 435 2,980/19/6.5% · 436 2,792/18/9.7% · 437 2,508/13/6.5% · 438 2,859/21/7.5% · 439 2,642/16/9.2% · 440 3,258/16/5.6%. Control 421–430 repaired: 24,480 words, median 16, 3.9%.

**TICS per 10k (27,364 words):** `Nobody said anything` 1 (0.4, gate ≤ 5) · `of fifty` 0 · `of twenty` 11 (4.0) · `of thirty` 5 · Marrow 0 · *arbiter* 0. Openings varied, all ten with calendar figures.

**PROTAGONIST.** Ilyan named 10 of 10 (103×), want/mistake/cost his own each chapter.

**PANELS.** One in band: `435:45`–`435:51` (four fields, one decision, none chosen, untold). `**` count across ten is eight, all there.

**CALENDAR.** 10 of 10 agree from table: shelf 306–315, morning 181–190, settlement 31–40, rail 21–30, fever 21w 1d–22w 3d. Anchor 400; `chapter − 351` unused.

**ARITHMETIC IN SENTENCES.** 9 × 364 = 3,276 visits × ¼d = 819d = 68s 3d (`435`); 819 ÷ 48 = 17 + 1/16 (`424`); 819 ÷ 240 = 3 days + over 3 (`424`); 4,004 = 11 × 364; 11 × 4s = 44s = **£2 4s** (`436`, correcting £4 4s = 84s = 21 years); 4 lb = 960d; 960 ÷ 11 = 87 rem 3 (`439`); 9 × 49 = 441 (`422`). `405:43` still overstates first row (outside phase; `412:55` right).

## 2. Records

Six files bounded, each < 60,000 bytes, top blocks ≤ ~12,000. Pruned generations in git at `1e8801a`.

---

## ARCHIVE

Pruned in the batch-0003 review repair; recoverable from git at `1e8801a`.
