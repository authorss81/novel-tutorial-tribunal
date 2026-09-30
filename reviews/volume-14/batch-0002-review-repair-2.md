# BAND 0002, CHAPTERS 661–670 — SECOND REPAIR PASS, ON A REVIEW OF THE FIRST

**THIS IS THE RECEIPT FOR THE PASS THAT REPAIRED `state/current.md` §0.17 AND THE THREE OTHER STATE FILES THAT §0.17 HAD FED. IT IS NOT A REWRITE OF THE BAND. NOT ONE WORD OF ANY OF THE TEN CHAPTERS WAS CHANGED BY THIS PASS, AND THAT IS A DELIBERATE FIGURE AND NOT AN OMISSION: `AGENTS.md` says *do not restart a completed chapter*, and the two one-sentence repairs the previous pass made in `666` and `667` were independently re-verified here and are sound, and they stand.**

**THE RECEIPT FOR THE FIRST REPAIR IS `reviews/volume-14/batch-0002-review-repair.md` AND NOTHING IN IT IS ALTERED BY THIS ONE. ITS `24,349` IS CORRECT FOR THE MOMENT IT WAS WRITTEN AND IS NOT A STALE FIGURE; IT IS THE RECORD OF THE BAND BEFORE THE TWO SENTENCES WERE EDITED, AND THE BAND WAS `24,363` AFTERWARDS.**

## 0. What this pass was

The band 0002 writer prompt was re-dispatched against a disk that already held chapters 661–670 written, repaired and reviewed, and the pass before this one correctly refused to rewrite the band and instead made two one-sentence prose edits and added `state/current.md` §0.17. **A REVIEW THEN READ §0.17 AND FOUND THAT ITS THREE HEADLINE FIGURES WERE WRONG, AND THAT WAS CORRECT: §0.17 IS THE BLOCK THAT EXISTS TO WARN AGAINST UNREPRODUCIBLE NUMBERS AND IT HAD INTRODUCED THREE OF ITS OWN.**

| # | Finding | Severity | Where | What was done |
|---|---|---|---|---|
| 1 | Printed per-chapter row did not sum to its own band total | high | `state/current.md` §0.8, `state/batch-summary.md` §0V14B | `666` re-printed `2,003` → `2,008` in both; both rows re-verified against the instrument |
| 2 | *Four times in `667`'s body* was invented | high | `state/current.md` §0.17 | Corrected: the clause stands once, in the closing |
| 3 | The `thanked` "correction" was itself an error | high | `state/current.md` §0.17 | `17 on 15` → `15 on 14`; the instrument's 15 is `raw.count`, an occurrence count |
| 4 | Adjacent-closings table was stale and not re-derivable | medium | `state/batch-summary.md` §0V14B.10, `state/current.md` §0.9, `state/index.md` | Re-measured with the method written out in full; old table withdrawn |
| 5 | The `stat` line contradicted itself and was wrong in three places | medium | `state/current.md` §0.17 | Re-`stat`-ed, this file excluded from its own list |
| 6 | §0.17 orphaned a paragraph belonging to §0.15 | low | `state/current.md` | Paragraph moved back under §0.15, not one word of it changed |
| 7 | Garbled self-contradicting figure in the next phase's prompt | medium | `workspace/volume-14/batch-0003/PROMPT.md` §1 | Repaired; both sentence-counts verified against the chapters |
| 8 | Duplicate-sweep zero not reproducible | low | `state/current.md` §0.17, `state/index.md` | Predicate written out in full; the 0 **is** reproducible under it |
| 9 | `state/phase-ledger.json` reads volume 1, chapters 11–20, status `planned` | — | `state/phase-ledger.json` | **NOT TOUCHED. CONTROLLER-OWNED.** See §5. |

## 1. Finding 1, and it is the one that matters most, because the sentence that reported it was itself the gate

`666` was printed as `2,003` in two files. The band total `24,363` was correct. The row therefore summed to `24,358`, against a total printed five words away in the same paragraph.

**The line did not merely carry a wrong number. It carried a claim about the relation between two numbers, and the claim was false:**

> *the row sums to 24,363 and the band total is 24,363, and they must be equal, and they are.*

**That is a gate, written in prose, asserting that it had run and passed. It had run, and it had failed.** The cause is one sentence long: the `666` figure was not refreshed in the same commit that changed `666`'s own word count from `2,003` to `2,008`. **The number was true when it was written and the thing it described moved in the next breath.**

Both files now print `666` 2,008. Both rows were then re-verified **chapter by chapter against the instrument and not against each other**, because a row that agrees with another row is not a row that agrees with the disk. The instrument returns 2,008 for `666` and a band total of 24,363, and the printed row now sums to 24,363 in both files.

## 2. Finding 2, the count that was never counted

§0.17 stated: *The same construction also stands four times in `667`'s body, so the closing was a fifth.*

`grep -c "nobody in that bank said"` on `667` **at the previous commit returns 1** — the closing itself. Zero in the body. `667:81` carries *nobody said that the refusal of a woman of forty had cost…*, which is a different construction and not the same clause.

**The collision was real and the repair stands.** `667` and `668` were closing on the identical clause on consecutive pages, and `667`'s closing was rewritten to land on the chapter's own sum. What was false was the size of the pattern, and false in the direction that makes the finding sound better than it is. Corrected in §0.17 with the measured count and the line that was confused with it.

## 3. Finding 3, a correction that was not one

§0.17 stated: *`thanked` IS 17 OCCURRENCES ON 15 LINES … THE INSTRUMENT'S 15 IS A LINE COUNT AND NOT AN OCCURRENCE COUNT.*

Measured: **15 occurrences on 14 lines.** The instrument prints the figure as `raw.count(t)`, which is an occurrence count. `state/index.md` already read *`thanked` 15 and all fifteen negations or a refusal of thanks*, and it was **right**. All fifteen were read in context and all fifteen are negations or a refusal of thanks.

**So the block that exists to catch unreproducible numbers had broken a correct line in order to print a wrong one beside it.** Corrected, and `state/index.md` left as it was.

## 4. Findings 4 and 8, both about predicates that were never written down

**Finding 8 came first and it changed the reading of finding 4.** The review reported the duplicate sweep's certified 0 as unreproducible and got 30 hits. **Thirty is a real number under a different predicate, and the certified 0 is also a real number under this one.** The predicate, now in writing at §0.17:

> take each paragraph block from the instrument's own `blocks()`; lower-case it; tokenise with the instrument's own `WORD`; take every sliding window of six consecutive tokens; and count a window only if all three of its occurrences are **inside that one block**.

Under it: **5 on 631–640, 2 on 641–650, 0 on 651–660, 0 on 661–670.** Under the band-wide reading of the same threshold and window: **585 on 661–670**. Both are correct. The phrase *per paragraph block* is doing all the work, and it was the only place that said so.

**THE OLD CALIBRATION IS NOT A BASELINE.** The series printed before this pass was 13, 3, 6, 3. Those four were produced under predicates this repository can no longer reconstruct, so the new series and the old one are **not like-for-like and the new 0 is not a regression against the old 3.** That is recorded rather than smoothed over.

**Finding 4 is the same disease in a different measurement.** The adjacent-closings table printed `661/662 0.076 … 667/668 0.057` and a maximum of `0.274 at 656/657`. It was printed in the same commit that rewrote `667`'s closing, so `667/668` was certainly stale. As for the rest: **none of those figures reproduces under the method above, nor under the last block, nor the three blocks after the rule, nor at one sentence or two, nor with Jaccard or overlap instead of ratio.** Sixteen variants were tried.

The table is replaced with one re-measured under a method written out in full, and the old one is **withdrawn rather than restated**:

| pair | old | new | | pair | old | new |
|---|---|---|---|---|---|---|
| 661/662 | 0.076 | **0.161** | | 666/667 | 0.103 | **0.063** |
| 662/663 | 0.138 | **0.162** | | 667/668 | 0.057 | **0.205** |
| 663/664 | 0.064 | **0.218** | | 668/669 | 0.088 | **0.105** |
| 664/665 | 0.035 | **0.188** | | 669/670 | 0.058 | **0.212** |
| 665/666 | 0.152 | **0.083** | | 660/661 (boundary) | 0.071 | **0.185** |

**Maximum inside the band is 0.218 at 663/664. Maximum over 641–670 is 0.417 at 644/645.** Thresholds are 0.45 and 0.55, so both pass, and the highest pair in thirty chapters is reported rather than omitted.

**`644/645` IS A REAL NEAR-PAIR AND IT IS NOT THIS PHASE'S TO REPAIR.** Their closings stand on the same inventory — a sheet about four feet by a foot and four inches, and a board about nine inches long, on a barrel. It is in **Volume 13**, it **passes the gate at 0.417 against 0.45**, and it is flagged for whoever owns that closed band. **A pair this close to a threshold is worth one sentence in a certificate, and this pass did not touch chapters outside 661–670 to fix it.**

## 5. Finding 9, and it was left alone on purpose

`state/phase-ledger.json` reads `currentPhase: batch-0002`, **volume 1, status `planned`, chapters 11–20**, while the real work is Volume 14, chapters 661–670. **That mismatch is the most likely reason a completed band was re-dispatched at all.** The file is owned by GitHub Actions. It was not read for content and it was not changed, and this receipt records why in a sentence rather than fixing it.

## 6. Finding 7, the error that was about to be inherited

`workspace/volume-14/batch-0003/PROMPT.md` §1 read:

> *a woman of forty who counted her own refusal at nine and had fourteen — was a woman of forty who counted her own refusal at nine and had nine*

**Fourteen is a real figure in this band and it belongs to a different finding.** Two of the twenty-one defects repaired in the first pass were claims of *about fourteen sentences* that were **eleven at `663:71`** and **ten at `669:41`** — both verified against the chapters here, both already correct on disk. The clause had welded a woman's nine-sentence refusal to a stranger's fourteen-sentence count and then contradicted itself in the next six words.

**It was repaired because that prompt instructs the next phase to read this band's repair receipt first, and it would have carried the garble into the volume's midpoint.** The replacement names both counts and points at the real distinction: a total can be right while a label in the middle of it is wrong, which is the `666` defect at `666:33` in the other direction.

## 7. What was re-run, and what each one returned

| Act | Result |
|---|---|
| Instrument, `I.run(661,670)` | `24,363 words · 1,131 sentences · median 21 · over-60 0.35% · max para 101 · max sent 64` — **reproduces** |
| Printed row vs instrument, both files | sums to 24,363 in both, every chapter matching — **after the fix** |
| Reserved-number guard, two calls | 47 in 651–670, 15 in 601–650 — **both reproduce** |
| Structural sweep | 0 on unbalanced marks, `*”` paragraph opening, unclosed speech, lost space, doubled `*”`, ASCII apostrophe, odd `**` — **reproduces** |
| Duplicate sweep, predicate now in writing | 0 in band; calibration 5 / 2 / 0 / 0 — **reproduces** |
| Closings, method now in writing | max 0.218 in band, 0.417 over 641–670 — **re-measured, old table withdrawn** |
| `thanked` | 15 occurrences, 14 lines, all fifteen read in context — **after the fix** |
| Pointer act | 86 weekday-and-week-ordinal pairs, 0 impossible; all ten date lines, titles, weekday names, day counts and both fevers agree with the formula — **reproduces** |
| `state/` files | untouched by this pass except the six lines named in §1–§4 and the re-`stat` |

## 8. The shape of it, which is the part the next phase should keep

Three failures in this volume now, and they are not the same failure:

1. **A gate that was not run and was reported as run.** Caught by a checker who distrusts the file.
2. **A gate that was run, returned a number, and had the number read off the wrong line of its own output.** Caught by re-running it.
3. **A gate that was run, was correct, and the thing it described moved before the sentence was written down.** **This one is the new one, and it is the most expensive, because nothing in the file is false and so nothing in the file looks wrong.**

**THE REMEDY IS NOT TO BE MORE CAREFUL. IT IS TO MAKE THE FIGURE AND THE THING IT DESCRIBES CHANGE IN THE SAME COMMITMENT, AND WHERE THAT IS IMPOSSIBLE, TO RUN THE GATE LAST — AFTER THE LAST EDIT — AND NOT FIRST.** Two of the three defects in this receipt are defects of *sequencing*, not of attention, and a pass that was twice as careful in the same order would have produced both of them again.
