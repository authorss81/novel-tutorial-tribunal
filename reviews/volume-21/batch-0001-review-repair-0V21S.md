# 0V21S — Review repair of Volume 21 Band 0001, chapters `1001`–`1010`

Findings came from `logs/batch-0001.review.log`. Eight were raised. **Six are repaired here, two are recorded
and deliberately not repaired, and none of them is a defect in the planned plot.** Nothing was restarted, no chapter
was rewritten, no scene was moved, no thread advanced and none closed, no band was re-planned and no volume was
re-scoped.

**This record was read a second time after it was written, because a repair that prints figures has to survive
being checked against disk. That reading found nine things wrong in this file and in the state blocks this pass
wrote: a `chapter:line` reference pointing four lines off a date line, a speech attributed to the wrong man, and
seven figures that were true when they were printed and stale by the end of the pass. All nine are repaired here
and in the state files, and `§0V21E` in each of the **six** files that carry one is corrected with them — `current.md`,
`continuity.md`, `index.md`, `batch-summary.md`, `chapter-summaries.md` and `character-state.md`. **`state/open-threads.md`
carries no `§0V21E` and holds these findings at `§1AZ`**, and it is the seventh file and the only one of the seven this
repair did not add a block to. Every figure below is one that survived that reading.**

Authoritative over `chapters/volume-21/chapter-1001.md` … `chapter-1010.md`, over `outline/volume-21.md` §4.4, over
`workspace/volume-21/batch-0001/PROMPT.md`, over `workspace/volume-21/batch-0002/PROMPT.md`, and over the blocks
this pass added to the seven state files. It is superseded by nothing and supersedes nothing but its own blocks.

**The figure of chapters rewritten is ZERO. The figure of chapter lines added, removed, split, joined or
reordered is ZERO — and that is the figure that protects every `chapter:line` reference in every state file and
every receipt in this repository. All ten files still hold the same line counts they held on arrival:
88 · 82 · 80 · 74 · 84 · 84 · 100 · 80 · 96 · 90.**

**The counting basis, printed because a reader's tool will disagree with it: `wc -l` counts newline bytes, and
none of these ten files ends in one.** A tool that reports the trailing partial line as a line gives 89 · 83 · 81 ·
75 · 85 · 85 · 101 · 81 · 97 · 91, one higher in every case, and both figures are correct about different things.
**Every `chapter:line` reference in these files is a `wc -l` line number, and the highest one in use is `1007:101`,
which is the last real line of that file.** Nothing in this pass added, removed or reordered a line, and the ten
counts above are identical to the ten in `git show HEAD:` for the same files, which is the only comparison that
means anything here.**

---

## 1 — BLOCKING. Two counters were crossed with each other, in the plan and in both prompts

**Where it was.** `outline/volume-21.md` §4.4 carried two rows, *since the division* and *since a page was read
out with the door shut*, and each row held the other one's figures and the other one's formula. As written, the
division row read **501** at `1001` on `ch − 500`, and the door-shut row read **555** on `ch − 446`.

**What the chapters say.** They are right and the plan was wrong. `1001:9` reads *Five hundred and fifty-five days
since the division* and *Five hundred and one days since a page was read out in a room with the door shut*;
`1002:5` reads **556** and **502**; `1007:3` reads **561** and **507**; `1010:5` reads **564** and **510**. So
**since the division = `ch − 446`** and **since a page was read out with the door shut = `ch − 500`** — which is what
§4's own formula line has always said under the short names *hall* and *clear*, and what `state/continuity.md` §0AZ
and §0V21A and `state/batch-summary.md` §0V21C have always carried. The chapters were never wrong, and no date
line was touched.

**Why no instrument caught it.** The table's numeric columns were internally consistent: `501`→`550` is `ch − 500`
at `1001` and `1050`, and `555`→`604` is `ch − 446` at `1001` and `1050`. A sweep that checks a table against its
own formula column finds nothing, because the formula column travels with the numbers. The defect is in the label,
and the only test that catches a label is to read one row out loud against a chapter.

**Repaired in three places.**
- `outline/volume-21.md:184-185` — each row keeps the figures and the formula it always had and takes the label it
  belongs to. Recorded in the plan at its own §13.13.
- `workspace/volume-21/batch-0002/PROMPT.md:50` — the two labels crossed. The figures were always right.
- `workspace/volume-21/batch-0001/PROMPT.md:59` — the same cross, in the prompt that produced the ten chapters,
  which came out right anyway. Repaired so nobody derives from it a second time.

**What it would have cost.** Band 2's prompt is the sole instruction for `1011`–`1020`. Unrepaired, it would have
instructed a writer to contradict `1001`–`1010` on ten date lines and call that a correction.

## 2 — BLOCKING. A figure in `state/batch-summary.md` §0V21C was three and said eight

Item 8 claimed *A THING NAMED FOR A PERSON IS NOT THAT PERSON'S* is **on the page eight times in eight mouths**,
and a second block claimed the ordinary form is **in eight mouths across these ten**.

Both were wrong and both were checked against disk, not argued. The form in the same words is on the page
**three** times, in three mouths: `1004:15` a man with a broom, `1006:63` a man of thirty-one with his face to the
wall, and `1007:37` **a man of thirty-eight with a board inside his coat**, who is Garrin Tolley and not the man
who cannot see well. The external review attributed that third one to the wrong man and the error was nearly
copied into canon; it is named here because a state file had it for a moment. It is also on the page in four
further mouths in other words — `1001:55` the boy of thirteen about a cup, `1002:45` a woman who saws lengths
about her own bench and her own saw, `1005:31` a woman who reads for a living naming the shape while turning it
against the people who would have been comforted by it, and `1009:39` the same woman again, knowing and not saying.

Repaired in both places in the open, with the three line references printed and the loose figure refused: **the
figure of how many people are carrying it about is not printed, and neither is zero.** The third place, in
`state/current.md`, said the same eight and now prints no figure at all.

## 3 — MEDIUM. Three of the three hundred and seventeen `reviews/` pointers read on arrival named a file that is not on disk

| Cited | What is actually there |
|---|---|
| `reviews/volume-17/batch-0004-current-records-0B.md` | `…volume-17/batch-0005-current-records-0B.md` — the **directory** was wrong; the block that holds §0B says itself it moved at volume 17 band 0005 |
| `reviews/volume-18/batch-0002-continuity-block-0AG.md` | named as the *predecessor* of the block it sits in; the real predecessor is `…volume-18/batch-0001-record.md` §7, and the block's own file is `…batch-0002-repair-continuity-block-0AG.md` |
| `reviews/volume-20/batch-0003-review-repair-0V20D.md` | **no such file anywhere.** The volume 20 band 2 review-repair record does not exist and never did |

The first two are corrected in place, and each correction says what was wrong, because a pointer that names the
right file and the wrong place is worse than one that names nothing: it is checked, and it passes.

The third is **not** satisfied, and it could not be. That pass left its whole record in the §0V20E block that is
already in five state files, deliberately duplicated; writing the file now would be a record of a pass that did not
write it. The heading is corrected in all five files to say so — the record is the block below the heading, it is
not under `reviews/`, and the band receipt that *is* on disk is `reviews/volume-20/batch-0003-receipt-0V20C.md`.

**Re-measured after the repair, and taken again after the last edit to any state file: 332 references that parse
as a path, 332 targets on disk, 0 missing.** It was 317 references with 3 missing before. The one path that is
named anywhere in these files and does not exist is named here and in `state/current.md` **split in two**, so that
it does not parse as a path, because naming it whole would put the broken pointer straight back into the record
the repair exists to remove.

## 4 — MEDIUM. Chapter `1010`'s title claimed an offer its body denies

The title read *A Man Of Thirty-One **Gave An Offer** At Three Hundred And Ten Days Out Loud With The
Subtraction And Nobody Answered It*. The body at `1010:53` says the standing offer **asked at the
seven-hundred-and-sixtieth** is three hundred and ten days old, that it **is unanswered**, and that **he has not
asked it on any morning this week**. He reports the age of an old offer. He does not make a new one, and the
volume's whole refrain turns on the offer still being unanswered at `1050`, so a title that says he gave one is a
title that contradicts the spine of the book.

Retitled in place, inside the line, keeping every other clause of the title and its length:
**…Gave The Figure Of An Offer At Three Hundred And Ten Days Out Loud With The Subtraction And Said Out Loud That He
Had Not Asked It And Nobody Answered It And Nobody Was Relieved…**

## 5 — MEDIUM. The three state files were 6, 12 and 36 bytes from the cap they police themselves

`state/current.md` at 59,994, `state/index.md` at 59,988, `state/chapter-summaries.md` at 59,964, against a hard
cap of 60,000 that `AGENTS.md` does not define and that stands behind 121 whole-block extractions already. Band 1
added about fifty-five lines and moved no block out, so the next band had three files it could not add a receipt
to without evicting something mid-pass and inventing a reason to.

**The policy is settled here rather than discovered by Band 2, and it is the one this file has always used: a
receipt that will not fit goes out whole, not one word of it is cut, and a pointer is left in its place.**

**Four** blocks went out at this pass, all of them whole, all of them superseded, all of them still canon:

| Moved from | Block | Body | Now in |
|---|---|---|---|
| `state/current.md` | `§0K` volume 18 band 0003, `871`–`880` | 13 lines, 6,717 bytes | `reviews/volume-21/batch-0001-current-moved-block-0K.md` |
| `state/chapter-summaries.md` | `§0V20G` the ten summaries and ten-row table for `981`–`990` | 16 lines, 15,018 bytes | `reviews/volume-21/batch-0001-chapter-summaries-moved-block-0V20G.md` |
| `state/index.md` | `§0V20G` the volume 20 band 4 index block | 5 lines, 5,711 bytes | `reviews/volume-21/batch-0001-index-moved-block-0V20G.md` |
| `state/open-threads.md` | `§1AR` the carried threads after `951`–`960` | 15 lines, 7,912 bytes | `reviews/volume-21/batch-0001-open-threads-moved-block-1AR.md` |

The one index block moved **named itself the live block for band 4** when it was written, which was true then and
is not now. Its pointer says so rather than repeating a stale claim, which is the difference between a moved block
and a buried one.

**The figure of headroom gained across the four files a block came out of is 21,710 bytes.**

**The seven files, as `stat` counts them after the last edit to any of them, largest first:** `continuity.md` 59,783 · `current.md` 58,958 · `index.md` 58,061 · `character-state.md` 56,586 · `open-threads.md` 53,527 · `chapter-summaries.md` 47,087 · `batch-summary.md` 44,548. **And the headroom under the cap, in the same order: 217 · 1,042 · 1,939 · 3,414 · 6,473 · 12,913 · 15,452.**md` 59,502 · `current.md` 58,955 · `index.md` 57,406 · `character-state.md` 56,586 · `open-threads.md` 53,392 · `chapter-summaries.md` 47,087 · `batch-summary.md` 44,323.

**And the standing recommendation, which is not ours to make:** the cap is enforced by nothing outside itself. It
has moved canon out of the exact files `AGENTS.md` tells a writer to read before writing. It goes to the owner of
the controller documents with the same standing as the 60,000 figure already recorded at `outline/volume-21.md`
§13.12, and **this pass did not raise it, did not lower it, and did not treat it as permission to summarise.**

## 6 — LOW. Four byte-identical lines in the band, three of them the plan's own and one of them not

At 40 characters and over, the band carried **4** duplicated lines. One is mandated by `outline/volume-21.md` §10
item 9 — the not-pulled list and *nobody laid a hand on that wood in order to take anything off it*, in the same
words in all ten — and **the list is still in the same words in all ten, in nine chapters of it byte for byte and in
`1010` with one further sentence after it, because the plan requires the list and the sentence is the last morning
saying it a last time.** The other three were the writer's and are repaired.

- *Nobody said anything to him about either of those.* — 7 occurrences. All seven were the same refusal to answer
  two figures, standing between the man of thirty-one's whole figure of mistakes and the next thing he says. Each
  of the seven now says what was actually not done on that morning, in its own words, and keeps its line.
- *Nobody said he was relieved and nobody said he was unrelieved.* — 3 occurrences. Each now says which of the two
  halves nobody took up.
- The three-line sweep paragraph — 3 occurrences. `1008` and `1009` now carry their own: different passes over the
  flight, different handling of the iron in the fortieth step, and the wood described from where each man was
  standing. `1007` is left as it stands.

**After the repair: 1 duplicated line of 40 characters and over in the whole band, and it is the mandated one.**
`1008` and `1009` also had the antecedent of the wood description cut with the sentence that introduced it; both
were put back in their own words inside the same line.

## 7 — NOT REPAIRED. Chapter titles run 64–96 words

The reviewer is right that titles of that length are run-on and close to unusable as headings, and Volume 20's ran
26–83 with a median near 47. **Measured on disk: 64 · 85 · 84 · 87 · 79 · 86 · 94 · 72 · 89 · 96 — the range is 64 to 96, and
the figure was 64 to 94 until finding 4's retitle put **seventeen** words onto `1010`, measured on the old clause and the new one, which is how a figure in a receipt
goes stale inside the receipt that is correcting it.** It is not repaired here, for two reasons that are about this repository and not about
the prose.

The first is that the long title is **load-bearing** in this house: `outline/volume-21.md` §4.3 requires that a
figure carried in a title is carried in the body as well, and Volume 20's off-morning ordinals were caught only
because they were in the titles. Nine of these ten titles carry a date, a weekday, a water figure or an event that
a reader is owed before the first line of prose.

The second is that **shortening ten titles in one band does not make the book readable.** A thousand chapters of
this manuscript carry titles of this length. Fixing Band 1 alone would make the table of contents inconsistent at
exactly the seam where a reader notices, and it would remove figures from titles on the strength of a reviewer's
preference rather than a plan rule.

**It is carried forward as an open question for the volume-21 close and it is recorded, not silently dropped.**
The one title that asserted something the body denies was fixed on its own merits, as finding 4.

## 8 — NOT REPAIRED. The water and the steps run the wrong way round — in the plan, not in the chapters

`1003` four inches and about ninety of the ninety steps under, `1004` eight and about eighty, `1005` twelve and
about seventy, `1006` sixteen and about sixty. **More water submerges fewer steps.** The ten chapters are
internally consistent and `outline/volume-21.md` §4.1, whose ladder table runs lines 115 to 122, specifies the pairing exactly as written, so this is a plan
defect faithfully executed.

It is not repaired, and the reason is arithmetic rather than taste. The ladder is the volume's clock. Reversing it
would move every full bank, every off-morning and every figure of days of the coming back in **four bands that are
not written yet**, and would make `1001`–`1010` the only chapters in the volume where more water means more steps.
Ten finished chapters are not worth a broken clock, and the volume does not close until `1050`.

**Recorded in `outline/volume-21.md` §13.13 as a live finding against the plan, and carried in
`state/open-threads.md`. It is a decision for the volume 21 close, and it is a decision that must be taken before
Band 3 opens, not after Band 5 is written.**

---

## Nine things this record got wrong the first time, and what they were

A repair that prints figures has to survive being checked against disk. This one was checked twice, and the
second reading found nine faults in it and in the state blocks this pass wrote. All nine are fixed. They are
listed here because a receipt that hides its own errors cannot be trusted about the chapters.

1. **`1001:5` was cited as the chapter-1001 date line in four places.** It is the opening image — the landing and
   the two pieces of wood. The date line is **`1001:9`**, and `1007`'s is **`1007:3`**. Repaired in this record, in
   `state/current.md`, in `state/continuity.md`, in `outline/volume-21.md` §13.13, and in `state/batch-summary.md`
   §0V21C item 2, which had carried the wrong line since the band was written.
2. **`1007:37` was attributed to the man who cannot see well.** It is spoken by **Garrin Tolley, thirty-eight,
   with a board inside his coat**. Simon Rook is not in chapter `1007` at all. The external review made this
   attribution and it was nearly copied into canon state. Repaired in this record and in `state/batch-summary.md`.
3. **`1002:37` was cited as a mouth using the shape in other words.** `1002:37` is the descriptor line for the
   woman who saws lengths; she speaks it at **`1002:45`**. Repaired in this record and in `state/batch-summary.md`.
4. **The seven-file size table was a snapshot of four different moments**, three of them before the last edit, and
   it put the files in the wrong order. Re-measured after the last edit and printed largest first.
5. **The pointer count said 317 after the repair.** 317 was the figure *before* it; the pass's own last
   measurement is **332**, and 332 is what the state files now print. The count moves whenever a file names the
   record, which is why it is printed with the measurement and not carried.
6. **The title range said 64 to 94** and the retitle in finding 4 had already made it 64 to 96.
7. **The number of blocks moved out was printed as three in three places** and as three-and-a-fourth in a fourth,
   while the fourth file's own arithmetic already included it. It is **four**.
8. **The headroom figure was 22,041** and was computed from two sizes that the pass then changed. It is
   **21,710**, taken from the sizes on disk now.
9. **Three new blocks pointed upward at a block below them**, and one of them, in `state/character-state.md`,
   pointed at a block that is not above it at all because it was the first line of the file. They name their
   section numbers now.

---

## What did not change

- The planned plot. No scene moved, no band boundary moved, no figure of the planned plot changed.
- All ten chapters keep their line counts, so every `chapter:line` reference in every state file and receipt holds.
- Threads advanced **zero** and closed **zero**, in words and not as two figures.
- No chapter was rewritten. Nine of the ten were touched; `1004` was not touched at all.
- No new name is put on anything in this band, and the figure of how many are is not printed.
- The right of refusal is not restored in any wording, and the offer is still unanswered at three hundred and ten days.
- No marker was written and `state/phase-ledger.json` was not touched; it is controller-owned.
- `System` remains absent, at **0** hits across the band, as Volume 21's plan requires.
- Exactly one next phase exists on disk: `workspace/volume-21/batch-0002/PROMPT.md`, chapters `1011`–`1020`, which
  carries the midpoint. This pass wrote no phase and created no directory.
