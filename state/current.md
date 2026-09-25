# Current State

## Re-entry guard for Batch 0003

**Batch 0003 is finished. Chapters 21–30 exist as complete prose and are canon.** If this phase is dispatched again, do not write, rewrite, replace, or "improve" Chapters 21–30. Audit them, correct only concrete defects, update state, and stop. A re-dispatch of this phase is a controller bookkeeping artifact, not an instruction to redo the batch.

## Controller note (fix pass, not a manuscript change)

`state/phase-ledger.json` still reads `currentPhase: batch-0002` with status `planned` and has no `batch-0003` entry, and `workspace/volume-01/batch-0003/` has no `.done` marker. Both are controller-owned: `state/phase-ledger.json` is off limits to agents, and the phase selector in `scripts/novel_runner.sh` scans for `PROMPT.md` without a `.done` or `.blocked` file. Neither was edited here. Until the controller marks `batch-0003` done, the selector will re-dispatch it, and the guard above is the only protection the finished chapters have. This is flagged, not fixed, deliberately.

## Progress

Current phase: Volume 01 Batch 0003 complete; next phase is Batch 0004

Current volume: 1 (series, ending, and Volume 01 outlines complete)

Current batch: 0004 (queued; Batch 0003 complete)

Last completed batch: 0003 (10 of 10 chapters complete)

Last completed chapter: 0030

Last batch summary: `state/batch-summary.md`

Active threats: The ninth bridge's west joint drifts two fingers on every load and returns; the brace holds and the joint does not. The clause that once let a named keeper pause a span is missing from the current charter, so the guild can see a failure and cannot stop a load. The bridge's provisional stay expires at the seventh-morning-bell review at noon, the charter is unamended, and appeal, enforceable exit, and durable housing and work protection are named in the record as unresolved. The Saltwheel petition is still a mounted precedent witness and the district's common register still carries *acknowledgment inferred from continued use*. Meridith Vale has performed four lawful acts in a row, and the printed form that carried the Ro household's position came from public print run 114, distributed to a plate office six days before the ninth-bridge notice, under an authorization page that was cut and replaced.

Active promises: Ilyan must prove he is not Veyra's author; the ninth bridge's missing maintenance-review condition; the keeper's power to pause a load; the historical right of refusal; the identity and purpose of the First Witness; the Shale Mirror's connection to Earth and Nadia Kestrel's independent witness work; the nine anchor positions and their missing functions.

Current relationship pressure: Ilyan and Sera work under a stricter boundary than before. She stopped him in a public hall, refused to let him reopen the bridge record, and accepted him only as a record-checker with a written division of labor. Ilyan has lost the lowland conservancy's citation and the assembly has made his name uncitable as a permit, so he has no constituency and one small granted request. Ilyan and Tarin are working allies with a real disagreement about worker refusal and load safety. Tamsin and Neris have twice refused to strengthen the case at their own expense; Tamsin has asked that the record state she is not a reason for the bridge. Sel Harrow has not appeared in person this batch. No romance beat has occurred.

Current power state: Early Stage 1, Case Opener. He can document a sequence, request one narrow provisional exception, and file an attached observation. He holds one granted request: a paid, finite west-joint inspection ending at the review bell. He cannot assign another's burden, force a witness, rewrite a plate, choose a local remedy, or use a new perception. His local language is a bounded guild work vocabulary of roughly two hundred terms, taught by the guild during this batch because a man who cannot take a count cannot be a second pair of eyes; it covers load talk, board notices, and employment register, and it does not cover a clerk's sentence, a foreman's letter, or a legal instrument. Keep that ceiling visible. The System translates formal records, notices, and the visible boundary of a hearing field entered into his open case; the Bench preserves records and issues binding rulings. Panels stayed rare, with an exact count so the next batch can hold the line: **six System-rendered entries across five of the ten chapters** — Ch24 (the assembly's single question), Ch25 (the close of the public account), Ch27 (the granted inspection), Ch29 (the C—2 index, and only after Moot read it aloud and entered the page as an exhibit), and two in Ch30 (the arrangement as recorded, and the witness-index line). Ch30 is the only chapter that used two, and `AGENTS.md` asks for at most one per chapter. Bold in-world documents — the guild's board, the district summons, the work slates, the guild count book, the print strip, the court slip, the assembly's own answer — are physical objects in the fiction, not System panels; do not count them as panels and do not let them multiply.

Next active phase: `batch-0004`, write Chapters 31–40 from `workspace/volume-01/batch-0004/PROMPT.md`.
