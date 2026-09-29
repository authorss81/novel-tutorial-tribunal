# Batch 0003 Review Record — Volume 11 (Chapters 521–530)

> **THIS FILE WAS WRITTEN BY THE REPAIR AND NOT BY THE REVIEWER, and it says so at the top because `state/batch-summary.md` §2b set that rule and this repository has already broken it twice: a receipt written by the repair is not a record of the review.** The review phase ran over this batch and produced `logs/batch-0003.review.log`. **WHAT IS TRANSCRIBED BELOW IS THE REVIEW'S OWN VERDICT AND ITS OWN FINDINGS, IN ITS OWN CLASSIFICATION AND IN ITS OWN ORDER. WHAT IS NOT HERE IS THE REPAIR'S REASONING, WHICH LIVES IN `state/current.md` §0.11.** The prose is the canon.

**Source of findings:** `logs/batch-0003.review.log`, produced by the review phase over commit `121f68f` (*novel: save writer work batch-0003*). **THE REVIEW'S FIRST TWO LINES ARE `! agent "novel-reviewer" is a subagent, not a primary agent. Falling back to default agent` AND `> novel-writer · space-bunny-free`, AND BOTH OF THOSE ARE PART OF THE FINDING AND NOT PART OF THE FRAMING: THE REVIEW WAS NOT RUN BY A REVIEWER.** See Finding 6 below. **The repair re-ran every check rather than transcribing the reviewer's conclusions, because the conclusions in that log are the conclusions of a writer-model session and are worth exactly as much as a re-derivation.**

**Scope of this file:** what the review found, what the repair did about each item, what was deliberately not changed and why, and what the next phase must not inherit. **This is the first and only review artifact for the 521–530 band; the measurements for it were already moved whole to `reviews/volume-11/batch-0003-measurements.md` and are not reproduced here.**

**Verdict, in the reviewer's words:** *the manuscript is healthy. The dispatch/control layer around it is not. The current phase produced zero prose, and the controller is about to burn three more full agent runs re-firing a phase whose work already exists — while blocking the volume's actual climax band.*

---

## 0. What this file records, and the one decision in it

**THE REPAIR CHANGED NO CHAPTER.** Every one of the seven findings in `logs/batch-0003.review.log` is a finding about the control layer and not about the prose, and the repair re-verified the band from the files rather than taking the log's word for it. **THE BAND IS CANON, IT IS FINISHED PROSE, AND IT PASSES EVERY GATE.** The repair's independent re-measurement is at §1 and its conclusion is that there is no prose repair to make and none was made.

**THE ONE DECISION IS A TERMINAL MARKER ON A PHASE DIRECTORY, AND IT IS RECORDED HERE SO THAT IT CAN BE UNDONE BY DELETING ONE FILE.** `workspace/volume-11/batch-0003/` carried `.attempts 3`, `.deferred`, `.retry-after` and `.wip-conflict`, and no terminal marker, and it was the only phase directory in a workspace of seventy-seven that had none. The prompt in it describes Chapters 521 to 530 and was written when the manuscript stood at 520. **THE CHAPTERS IT DESCRIBES ARE ALREADY ON DISK, AND THE MANUSCRIPT IS AT 540, AND THE NEXT BAND ALREADY EXISTS.** The repair set `.done` and cleared the transient markers, which is what the runner's own success path does at `scripts/novel_runner.sh:359`. **`.done` AND NOT `.retired`, BECAUSE THE BAND WAS DELIVERED AND A BAND THAT WAS DELIVERED IS NOT THE SAME THING AS A PLANNING ARTIFACT THAT WAS NEVER RUN.**

**THIS UNBLOCKS `workspace/volume-11/batch-0005`, CHAPTERS 541 TO 550, WHICH IS THE LAST BAND OF VOLUME 11 AND ITS CLIMAX. THAT PROMPT ALREADY EXISTS AND WAS NOT TOUCHED, AND NO NEW PHASE DIRECTORY WAS CREATED, BECAUSE THE RULE IS EXACTLY ONE NEXT PHASE AND ONE ALREADY EXISTS.**

---

## 1. The repair's independent re-verification of 521–530, run rather than believed

**THE INSTRUMENT IS THE PUBLISHED ONE AND IT WAS RUN, NOT RE-TYPED: `reviews/volume-10/instrument.py`, called as `python3 -c "import sys;sys.path.insert(0,'reviews/volume-10');import instrument as I;I.run(521,530,vol='volume-11')"`, with the corpus named explicitly because the published default is Volume 10.**

```
BAND 521-530: 27807 words | 1160 sentences | median 21 (gate <= 25) | over-60 2.76% (gate <= 10%) | max para 119 (gate ~ 120) | max sent 136
straight ASCII apostrophe: 0   PANELS: none
TICS:  month 0 | arbiter 0 | villain 0 | the volume 0 | this volume 0 | the novel 0 |
       First Witness 0 | spring 0 | summer 0 | autumn 0 | winter 0 | the rail 0 |
       do not make it a speech 0 | Sorry 0 | grateful 0 | do not stop family 0
SILENCE: 11 (4.0/10k) across the 27 wordings above; CHORUS subset: 0
SAID NOTHING, the other beat, printed and not gated: 1 (0.4/10k)
```

**EVERY GATE PASSES AND THE ROW SUMS TO THE BAND TOTAL, WHICH IS THE CHECK THAT A FIGURE NOBODY CHECKED CANNOT PASS.** Per chapter, 521 2374/114/1.75%/77 · 522 2756/130/0.77%/103 · 523 3005/132/3.03%/94 · 524 2694/109/3.67%/77 · 525 3322/128/3.12%/119 · 526 3188/152/1.32%/74 · 527 2633/100/4.00%/87 · 528 2471/100/3.00%/98 · 529 2975/108/3.70%/80 · 530 2389/87/4.60%/73. **THESE ARE THE SAME FIGURES AS `reviews/volume-11/batch-0003-measurements.md` AND THE BAND HAS NOT BEEN TOUCHED SINCE, WHICH IS THE POINT OF A MEASUREMENT FILE: A NUMBER PRINTED IN A FILE THAT HAS SINCE BEEN CHANGED IS WORSE THAN A NUMBER NOWHERE.**

**THE THREE ACTS NO INSTRUMENT PERFORMS, RUN BY HAND:**

- **Adjacent-chapter closing lines, 521 through 530, read against each other.** No contradiction. `525` closes on two true accounts that stop fitting and neither being wrong, `526` closes on the two towns holding a true account of a morning that is not the same morning, and `527` through `530` move from the woman who was never asked what she remembered, to a finding that is not a decision, to a form with no line for two, to a week standing in a town with no dated thing to count from. **THE HANDOFF IS CLEAN AND IT IS A HANDOFF AND NOT A REPETITION.**
- **Date lines re-derived from the anchor, not read out of the outline table.** `shelf = chapter − 125`, `week = 40 + shelf ÷ 7`, `day = shelf mod 7 + 1`, morning `= chapter − 250`, settlement `= chapter − 400`, fever `= chapter − 283`, `clear = chapter − 500`. 521 prints fifth day of the ninety-sixth week, 271st morning, 121 days after the settlement, fever thirty-four weeks and no days, seventy-five days since the division, twenty-one since the reading. 526 prints third day of the ninety-seventh, 276th, 126, thirty-four weeks and five days, eighty, twenty-six. 530 prints seventh and last day of the ninety-seventh **and names the morrow as the first day of the ninety-eighth**, 280th, 130, thirty-five weeks and two days, eighty-four, thirty. **ALL AGREE FIELD BY FIELD, AND 530 NAMING THE MORROW IS WHAT LETS BATCH 0004 CROSS A WEEK BOUNDARY.**
- **Form and absence.** No chapter is under 2,000 words. No paragraph over ninety characters is duplicated anywhere in the band. A sweep for `the volume`, `this novel`, `in this chapter`, `the reader`, `the author` returns nothing.

---

## 2. The reviewer's findings, in the reviewer's classification, with the repair's disposition on each

### Finding 1 — The re-dispatch loop, root-caused (reviewer: critical). **NOT FIXED. CONTROLLER-OWNED.**

`workspace/volume-11/batch-0003` was the only phase in the workspace without a terminal marker. The selector at `scripts/novel_runner.sh:70-82` takes the first prompt that is not `.retired`, not `.done`, not `.blocked`, and not past `.retry-after`, and that resolved to `batch-0003` every time. Its `.retry-after` had expired, `.attempts` was 3 of `MAX_ATTEMPTS=6`.

**The repair has set the terminal marker, which stops the loop for THIS phase. It has not touched the selector, and it must not: the cause is the selector's blind spot described in Finding 3, and Finding 3 is not the repair's to close.**

### Finding 2 — `.wip-conflict` is a permanent poison pill. **NOT FIXED. CONTROLLER-OWNED.**

`resume_wip` at `scripts/novel_runner.sh:141` returns early whenever `.wip-conflict` exists and never retries the branch; the marker is only cleared on the success path at line 359. **The repair cleared the marker on this phase as part of the same terminal transition, so the pill is gone here, but the rule that made it permanent is in `scripts/`, which the repair may not edit.**

### Finding 3 — `retire_obsolete_phases` cannot catch this class of phase. **NOT FIXED. CONTROLLER-OWNED. THIS IS THE ACTUAL BUG.**

The pre-pass at `scripts/novel_runner.sh:34-66` retires two shapes only: a prompt whose first line matches `volume N ... outline phase`, and a prompt containing `Retired ... phase`. **A BATCH phase whose chapters already exist on disk matches neither, and there is no "these chapters are already written" rule anywhere in the function.** The reviewer notes three prior attempts at this gap (`8ab5cdf`/`6e7cde3`, `e147fb7`/`8dc45b4`, `057ba6d`/`9e287b0`), all of which widened only *outline* detection, and identifies the pattern as the general rule being narrowed to the latest observed symptom.

**THE REPAIR AGREES AND ADDS THE OBSERVATION THE REVIEWER MADE AT THE END OF ITS REPORT, BECAUSE IT IS THE MOST USEFUL SENTENCE IN THE LOG: THE CONTROLLER KEEPS ASKING A MODEL TO DISCOVER A FACT THAT IS CHEAP AND EXACT TO CHECK IN THE FILESYSTEM. THE WRITER DID THIS REASONING MANUALLY AND CORRECTLY AND REFUSED TO WRITE. THE MACHINERY COULD NOT DISTINGUISH A PRINCIPLED REFUSAL FROM A FAILURE, SO IT DEFERRED, RETRIED, AND EVENTUALLY COMMITTED NOISE. THE MODEL IS THE WRONG PLACE FOR THAT CHECK. A RULE OF THE SHAPE "IF EVERY CHAPTER IN THIS BAND'S RANGE ALREADY EXISTS ON DISK AND IS NOT EMPTY, THE PHASE IS DELIVERED" WOULD HAVE RETIRED THIS PHASE IN THE SAME PRE-PASS THAT ALREADY EXISTS, WITH NO AGENT RUN AT ALL.**

### Finding 4 — Commit `121f68f` is content-free and mislabeled. **NOT FIXED. NOT REPAIRABLE.**

The commit contains exactly one changed path, `reviews/volume-10/__pycache__/instrument.cpython-312.pyc`, and no chapters, state files or review. **The writer behaved correctly: it inspected the workspace, found the prompt two bands stale, and declined to write rather than regress the manuscript from 540 to 530.** The dispatcher's blanket `git add -A` then swept bytecode and committed it as the phase's result. **A COMMIT MESSAGE IS NOT REWRITTEN IN A REPAIR AND THIS REPAIR DID NOT REWRITE ONE.**

### Finding 5 — `.gitignore` does not exclude bytecode. **NOT FIXED. FLAGGED.**

Root cause of Finding 4. `.gitignore` covers `logs/`, `*.log`, `.env`, `.env.*` and `.DS_Store`; it does not cover `__pycache__/` or `*.pyc`, and one `.pyc` is tracked. **Any `git add -A` sweep will therefore sweep bytecode into novel commits on every future run that touches `reviews/volume-10/instrument.py`.** The repair does not edit `.gitignore`: it is repository configuration and not a fiction, bible, outline, chapter, summary, continuity, character or open-thread file, and this repository's ownership rules are about the classes of file a writer may touch. **THIS IS A ONE-LINE FIX AND IT IS FOR THE OPERATOR: ADD `__pycache__/` AND `*.pyc` TO `.gitignore`, THEN `git rm --cached reviews/volume-10/__pycache__/instrument.cpython-312.pyc`.**

### Finding 6 — The review step is not independently reviewing. **NOT FIXED. CONTROLLER-OWNED. AND IT INVALIDATES THE PROVENANCE OF THIS LOG.**

The log opens with the fallback warning and then runs the **writer** model under the writer's configuration. **THE FAILURE IS SILENT, WHICH IS THE WORST PART OF IT: THE FILE IS STILL NAMED `batch-0003.review.log`, SO A READER WOULD REASONABLY ASSUME A REAL REVIEW RAN. THE AGENTS.md QUALITY GATE — *a reviewer has checked the result* — IS NOT BEING SATISFIED BY AN INDEPENDENT REVIEWER, AND THE REPAIR HAS NOW DISCOVERED THAT EVERY REVIEW ARTIFACT IN THIS REPOSITORY INHERITS THE SAME PROVENANCE PROBLEM.** The fix is to make `novel-reviewer` a primary agent the runner can dispatch, or to make the fallback loud rather than silent. **BOTH ARE IN `.opencode/agent/` AND THE WORKFLOW, WHICH THE REPAIR MAY NOT EDIT.**

### Finding 7 — `state/phase-ledger.json` is grossly stale. **NOT FIXED. EXPLICITLY NOT THE REPAIR'S FILE.**

It reads `currentPhase: batch-0002`, volume 1, chapters 11–20, `status: planned`, `actualModel: null`, against a reality of 540 chapters across eleven volumes with `volume-11/batch-0005` pending. **IT IS ROUGHLY TWO VOLUMES AND THREE BATCHES BEHIND, AND IT DISAGREES WITH `state/current.md` ABOUT WHICH PHASE IS NEXT.** The reviewer did not edit it on ownership grounds and neither did the repair. **THE REVIEWER'S OBSERVATION IS THE IMPORTANT ONE AND IT IS REPEATED HERE BECAUSE IT IS THE HEALTHIEST SENTIMENT IN THE LOG: `state/current.md` IS CORRECT WHILE THE LEDGER IS BADLY WRONG. THE PROSE STATE FILES ARE HEALTHY AND ONLY THE CONTROLLER LEDGER HAS ROTTED.**

---

## 3. The minor items

- **`reviews/volume-11/` had `batch-0003-measurements.md` and no review artifact, while 0002 and 0004 each have a repair file.** **THIS FILE IS THE ARTIFACT AND THE GAP IS CLOSED.** The measurements file was already complete and correct and was not touched.
- **Paired push-retry commits `057ba6d`/`9e287b0`, `e147fb7`/`8dc45b4`, `8ab5cdf`/`6e7cde3` have differing trees.** Historical, outside the repair's reach, and low priority. Noted so the next reader does not spend time on it.

---

## 4. What the next phase must not inherit

**DO NOT EXECUTE `workspace/volume-11/batch-0003/PROMPT.md`. IT IS TERMINAL AND IT DESCRIBES CHAPTERS THAT ALREADY EXIST.** It is a faithful and good prompt for a band that was written and delivered two bands ago. Running it would overwrite ten canon chapters, re-spend a midpoint the volume is allowed to spend once, and regress the manuscript from 540 to 530, discarding the Archive Lords introduction, the distributed-witness network, and every state file written after it. **A FINDING IS A FINDING AND NOT A STANDING ORDER, AND A PROMPT THAT HAS BEEN SUPERSEDED BY THE CHAPTERS IT DESCRIBES IS NOT A PLAN.**

**THE NEXT PHASE IS `workspace/volume-11/batch-0005/PROMPT.md`, CHAPTERS 541 TO 550, THE VOLUME'S CLIMAX AND RESOLUTION.** It restores the first removed witness, exposes a list of the original Compact's missing guarantees, and leaves Ilyan learning that he is legally classified as an external witness. **The prompt exists and is correct. The repair did not create a next-phase directory and must not, because exactly one already exists and the rule is one.**

**AND THE QUESTION THE VOLUME'S DOOR IS LEFT OPEN ON IS NOT THE REPAIR'S TO CLOSE AND IS NOT THIS BAND'S: CAN AN EXTERNAL PERSON BECOME A CITIZEN WITHOUT BEING ABSORBED INTO THE WORLD'S PREFERRED STORY?**
