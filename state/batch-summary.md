# Batch Summary — the measurements

**This file carries the instruments and their outputs. A figure here is only worth what the instrument printed with it.** This block supersedes everything below it. Chapters 1–430 are canon.

## 0. Why this block was rewritten

The delivered batch was reviewed (`logs/batch-0003.review.log`) and the review's verdict was that the prose was not publishable and the record was not readable. **The span-scan leader tables, the byte accounts, the calibration figures and the self-description of the process that filled this file have been deleted, because they were the largest part of it and none of them helped anybody write a chapter.** Everything below this line is history.

## 1. The instruments, printed so they can be re-run

**PROSE.** Split the file into sentences after a full stop, question mark or exclamation mark followed by up to two of `”` or `*` and a space, so that a closing quotation mark ends a sentence. Count words as `[A-Za-z’'-]+`. Paragraph cap counts every block between blank lines, excluding the chapter title, `---` breaks and the four System lines.

```python
import re
def w(t): return len(re.findall(r"[A-Za-z’'\-]+", t))
def sents(t): return [s for s in re.split(r'(?<=[.!?])[”"*]{0,2}\s+', t) if s.strip()]
L = [w(s) for n in range(421, 431) for s in sents(open(f'chapters/volume-09/chapter-{n:04d}.md').read())]
L.sort(); print(L[len(L)//2], L[int(len(L)*.9)], L[-1],
                 round(100*sum(1 for l in L if l > 60)/len(L), 1))
```

**THE BAND AS DELIVERED, AND THE SAME INSTRUMENT OVER THE OLD BAND AND THE CONTROL.**

| | Words | Sentences | Median | p90 | Max | Over 60 words |
|---|---|---|---|---|---|---|
| **421–430 as delivered** | 26,940 | 626 | 35 | 95 | 200 | 28.0% |
| 411–420 (control, unrepaired) | 22,946 | 644 | 23 | 82 | 157 | 22.0% |
| **421–430 after this repair** | 24,480 | 1,131 | **16** | **47** | **87** | **3.9%** |

Per chapter after the repair: 421 2,163 words, median 15, 0.0% over 60 · 422 2,002, 13, 1.9% · 423 2,618, 14, 4.5% · 424 2,517, 13, 4.4% · 425 2,284, 16, 5.0% · 426 2,615, 16, 4.3% · 427 2,488, 19, 3.7% · 428 2,490, 16, 3.5% · 429 2,480, 24, 1.0% · 430 2,827, 23, 11.1%.

**Longest paragraph in the band: 121 words, in 426. The System's EVIDENCE line in 425 is 196 words and is a fixed artifact, counted separately and not shortened.**

**TICS, per 10,000 words, against the control band 411–420.**

| | Band | Control |
|---|---|---|
| `Nobody said anything` | 0.8 (2 in the band) | 15.7 |
| `of fifty` | 2.0 | 17.0 |
| `of twenty` | 5.3 | — |
| `of thirty` | 2.0 | — |
| `in four hundred miles` | 0.4 (1 in the band) | 4.4 |
| `four hundred miles` (all uses) | 12.2 | 13.9 |
| `in this city` | 24.9 | 31.4 |
| `the fever was` | 4.5 | 8.3 |
| `and he said` | 1.2 | — |

**A word count is a number because of what it changed, and the four phrases above were cut because they were a habit, not because a number is printed beside them. The motif that survives is the one that is load-bearing: *a bar is a rule with no room in it*, and nobody being thanked.**

**PROTAGONIST.** `Ilyan` appears in 10 of 10 chapters, 96 times, against 0 in 10 and 2 in 10 in the two bands before it. He now has a want, a mistake and a cost in every chapter: `422:47` the divisor he does not say, `423` the divisor he does not say, `428` the sentence he does not say, `429:85` the third name he offers and is refused, `425:113` the panel he chooses nothing out of, `427:61` the price he names and it does not stop him.

**CAST.** Four labels became names in this repair — the ground-floor clerk, the door visitor, the man who counts halls and the boy — plus the carter, the woman who reads plates and the woman of sixty, whose ages were already in the prose. See `state/character-state.md` §1 and `outline/volume-09.md` §2.

**PANELS.** One, at `425:113`–`425:116`. The count of `**` across the ten chapters is eight and all eight are in it. One per band, three bands running.

**CALENDAR.** All four figures printed in all ten chapters, 10 of 10 agreeing, read from the files: shelf 296–305, morning 171–180, settlement 21–30, fever 19w5d–21w, rail 11–20 days. `chapter − 351` was not used. The anchor is chapter 400 and was not changed.

**ARITHMETIC, CHECKED AND PRINTED IN THE SENTENCES THAT USE IT.** 3,276 farthings = 819 pence = 68s 3d. 819 ÷ 48 = 17⅟₁₆. 819 ÷ 240 = 3 days and a little over 3. 4,004 days = nine rounds of 420 plus 224, ≈ 11 years, £4 4s. 9 × 49 = 441. Three hundred and sixty-four pounds is a year at one pound a day and is not converted into anything. **One figure is inherited and still wrong, and it is outside this phase: `405:43` says forty-eight pence over 364 days is a farthing a day and not quite, and it is a shade over half a farthing a day; `412:55` has it right.**

## 2. The records

The six state files were 5,894,680 bytes and are now bounded: `current.md` and `batch-summary.md` are the receipt and the measurements, `continuity.md` is the fact base and the documents, `character-state.md` is the people, `open-threads.md` is what is running, `chapter-summaries.md` is one paragraph per chapter for the band in progress. Every file is under the 60,000-byte ceiling this phase set, and every one of them is under 20,000. **A band may not leave a top block longer than about 12,000 bytes.** The pruned generations are in git at `1e8801a` and nowhere else.

---

## ARCHIVE

Pruned in the batch-0003 review repair; recoverable from git at `1e8801a`.
