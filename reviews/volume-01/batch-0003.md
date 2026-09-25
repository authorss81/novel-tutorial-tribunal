# Batch 0003 Review — Volume 01, Chapters 21–30

Reviewed from `logs/batch-0003.review.log`; fix pass applied. Prose was preserved and no chapter was restarted. The plot of Chapters 21–30 and the plan for Batch 0004 are unchanged.

## Verdict

The batch is sound. The reviewer's independent checks found no blocking prose or continuity defect, and the fix pass confirmed it: all ten chapters exist as finished scenes that each end on a completed beat, with no duplicate paragraphs, no meta markers, and no software jargon. Four concrete defects were found and fixed, one reviewer note was applied, and three pipeline findings are controller-owned and were deliberately left alone.

## Fixed in this pass

- **Chapter 21, hours contradiction.** Ilsa read the board back as "At the load change, four hands" while the board two paragraphs above her says `6 AT EACH CHANGE`, Chapter 28 has her say "four before the first bell and six at each change," and `state/continuity.md` asserts the figure is consistent. Corrected to six. This is the batch's central number — a keeper's refusal is over hours — so the slip mattered more here than a stray digit usually would.
- **Chapter 27, shift phrasing.** Her named shift was given twice, once as "from the setup before the first bell to dusk" and once as "before the first bell to dusk." Aligned to the longer form, which now matches the Chapter 21 board exactly and makes the sentence quoted in `state/continuity.md` literally true.
- **Prose repetition, per `AGENTS.md`.** `wrote` reduced 8→6 in Chapter 23 (`did not put` / `The entry read` / `recorded`) and 7→5 in Chapter 28 (`marked it on the slate` / `put the distinction on the slate`). `counted` reduced 8→7 in Chapter 27 by giving the cart owner the lay word "going unwatched," which also stops her from echoing the clerk's technical sentence two paragraphs later. Every remaining instance is load-bearing: the guild's own term, Ilsa's deliberate repetition, or the `counting loads / counted against` chiasmus. None of the edits changed a fact, a beat, or a sentence's sense.
- **State accuracy.** The nine-slot recovery arrangement was recorded as "four guild hands, two ward hands, one road hand, one whistle" in both `state/batch-summary.md` and `state/chapter-summaries.md`, which sums to eight. Chapter 28 has four guild hands, three road-party hands of whom two cannot leave the road, and two ward hands, one of whom holds the whistle. Both files corrected.

## State corrections

- **Review-bell timing.** `state/open-threads.md` and `state/character-state.md` placed the seventh morning bell "on the morning after Chapter 30" / "on the day after the pre-review sitting." Chapter 29 is the evening before; Chapter 30 is the pre-review sitting morning and the bell rings at noon that same day. Both corrected, and the same error was fixed in the Batch 0004 prompt.
- **An identification the chapter refuses to make.** `state/character-state.md` and `state/continuity.md` stated that Ilsa's grandmother counted the plate's load-book edge and was paid off the book. Chapter 27 never says that. Ilsa's grandmother kept a book with load-book cuts down two edges; a *different*, unnamed woman had counted the west edge for six years and was paid off when the crew list was cut to one name; and Ilsa says in public that she cannot decide whether the levy ledger's cut-out name and the plate's cut are one hand, and asks the room to stop her deciding. Both files now preserve the uncertainty, because a later batch building on a collapsed identification would break the batch's own argument.
- **System panel accounting.** `state/current.md` claimed "five formal notices across ten chapters." The true count is six System-rendered entries across five chapters — Ch24, Ch25, Ch27, Ch29, and two in Ch30 — the last of them being the only chapter to use two, against `AGENTS.md`'s one-per-chapter guidance. The exact count, the chapters, and the list of bold in-world documents that are *not* panels (guild boards, the district summons, work slates, the count book, the print strip, the court slip, the assembly's own answer) are now recorded so the next batch has a real ceiling to hold.
- **Attribution.** The plate/index comparison in Chapter 30 is Sera's, on the sealed original rather than Oren's rubbing, with Neral arranging the lamp at the barred window. Recorded in `state/continuity.md`, where the result previously had no agent.
- **`state/continuity.md` hours note.** Expanded to state the Chapter 21 board text, Ilsa's correct reading of it, and the one phrase that reads like a contradiction and is not — the load changes begin at the second bell while the levy pays hands from before the first bell — so a later writer does not "correct" a non-problem.

## Controller-owned findings, flagged and not touched

These are real and two of them are urgent, but every file involved is off limits to an agent. Recorded here and in `state/current.md` rather than fixed.

1. **`workspace/volume-01/batch-0003/` has no `.done` marker.** The selector in `scripts/novel_runner.sh` picks the first `PROMPT.md` lacking `.done` or `.blocked` and does not consult the ledger or `.wip-conflict`, so the next tick re-dispatches Batch 0003 with instructions to write Chapters 21–30 in full. The previous run survived only because the writer audited instead of rewriting. `state/current.md` now opens with an explicit re-entry guard; the marker itself is the runner's to write.
2. **`state/phase-ledger.json` is stale and contradicts disk.** It reads `currentPhase: batch-0002` with status `planned`, has no `batch-0003` entry, and has not been meaningfully updated since Batch 0001 — while `PHASE_SYSTEM.md` describes the selector as reading it. Agents may not edit this file, and the discrepancy is exactly the kind of thing that would mislead the next writer.
3. **No review artifact was ever written.** The reviewer agent runs with `edit: deny` and nothing in the runner writes its output to `reviews/`, so findings existed only in `logs/`. This file closes the gap for Batch 0003; making the runner write it is controller work.

## Next-phase prompt corrections

`workspace/volume-01/batch-0004/PROMPT.md` was aligned without changing its ten cards or its plot.

- **Word count.** "Normally 2,000–3,000 words" contradicted `PHASE_SYSTEM.md`'s 2,200–3,200 plus its explicit permission for longer complete scenes, and actual output ran 2,859–4,133. Now aligned, with the batch's real range given as evidence and an explicit instruction not to pad or cut a scene to hit a number.
- **Bell timing** corrected, as above.
- **Panel ceiling** made concrete: five or fewer across the batch, at most one per chapter, with the scenery-not-panels distinction spelled out.
- **A false canon rule removed from the Chapter 0031 card.** It said asking the Bench to schedule the full hearing "would be the reopening he has been forbidden to ask for." The canon rule is narrower: *reopening a record* suspends the stay; scheduling a hearing is untested and is exactly what Chapter 0039 puts on the record. The card now stages the untested distinction as the district's objection instead of asserting a rule the manuscript has not established.
- **Volume-outline binding added.** `outline/volume-01.md` assigns Chapters 31–40 four things the cards did not all carry: an attempt by the Bench to close the hearing under an emergency continuity rule, Tarin's field action preserving evidence, Bram Orren's early route knowledge, and the missing refusal clause remaining only partially readable. A short section now binds all four to the existing cards without adding cards or restructuring the arc. Bram is canon in `state/continuity.md` and had not appeared in Chapters 21–30.

## Carried forward

The batch spends the four pressures the Batch 0002 review left unspent — the refused hold, acknowledgment inferred from continued use, the entering clerk, and the date order — and leaves the plate/index pairing as a result rather than a fresh clue. The next batch must not re-reveal it, must not collapse the plate cut, the ledger cut, and the grandmother into one person, and must not restore the pause clause by proclamation. No new final enemy has been introduced, and the planned ending is untouched.

## Observed, not changed

Chapters 3 and 5 repeat two sentences almost verbatim where Chapter 5 recapitulates Neris handing over her flood account. It reads as deliberate recall rather than an accident, and both chapters are canon from a closed batch, so nothing was edited. Worth a look whenever Chapters 1–20 are next opened for a substantive pass.
