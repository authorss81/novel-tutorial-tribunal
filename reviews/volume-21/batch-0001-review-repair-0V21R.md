# 0V21R — Review repair of the volume 21 planning phase `next-0012`

Authoritative over `outline/volume-21.md` and over
`workspace/volume-21/batch-0001/PROMPT.md`, which are the two files this phase wrote.

Findings came from `logs/next-0012.review.log`. Nine defects were raised. **Six are repaired here,
one is repaired in the outline rather than here, and two are not ours and were not touched.**

This repair wrote no chapter prose, changed no plot, moved no band boundary, and changed no figure of
the manuscript. The ten band-1 chapter cards in the prompt are unaltered apart from three words of
casing.

---

## Repaired here

### 1 — A file size that was wrong in both directions

`PROMPT.md` said `state/current.md` "IS AT SIXTY-ONE THOUSAND BYTES AGAINST A CAP OF SIXTY
THOUSAND", and used it to justify moving a whole block out of that file. `stat` says **57,888** —
under the cap, with 2,112 bytes of room. It was over by about three thousand and it was over in the
direction that makes a file sound fuller than it is.

The figure is now stated as measured. It is also now *derived* rather than carried: the prompt prints
all seven state-file sizes measured on 2026-10-03, and says outright that a size read in any state
file, including the prompt's own, is not to be trusted and must be run again.

### 2 — The wrong file named for a move-out, and the wrong one missed

The prompt ordered a whole-block move out of `state/batch-summary.md` on the strength of "THIS FILE
IS AT ITS CAP". It is at 32,850 bytes, with **27,150** bytes of room — the roomiest of the seven.

The file that will actually break is `state/open-threads.md`, at **59,696** bytes: **304** bytes of
room, of which this planning phase spent 1,391. And the prompt is what orders a block into it. So the
instruction moved canon out of the file with the most space and would have overflowed the file with
the least.

Both corrected. **No state file is owed a whole-block move by this band**, because all seven have
room, and the prompt now says that instead of implying otherwise. `state/open-threads.md` is named as
the one to write short, and its block is told to `stat` before starting.

### 3 — Three words of wrong casing in bold table cells

`YOURS` and `OWING` were sentence-case inside bold capitals at `PROMPT.md:107` and `:108`;
`THE man of fifty-four` at `:110`. Fixed. Nothing else in those ten cards was touched — they are the
strongest work of the phase and they stand.

### 4 — Glyph bloat in the outline

`outline/volume-21.md` carried **13,296** decorative glyphs, about nine per cent of the file,
including one unbroken run of **3,933** at line 263.

These were not noise. They were carrying the clause breaks in text that is otherwise solid capitals
with its spaces stripped. Deleting them outright collided the bold span ending on AND with the one opening on
BUT, so the paragraph read AND BUT with the break gone. So every run was collapsed to a single separator
instead:

| | before | after |
|---|---|---|
| bytes | 146,667 | 113,636, collapse only |

The outline is larger than that figure now, because §13.12 and the §13.9 paragraph were added after the
collapse ran. No live size of the outline is printed in it, deliberately: a file cannot state its own
size, and quoting one while still writing it is the same mistake defect 1 is about.
| glyphs | 13,296 | 1,908 |
| longest run | 3,933 | 2 |
| bold markers | 2442 | 2488 |
| headings / table rows | 30 / 82 | 30 / 82 |

Verified by word-level diff against `HEAD`: the two differ in exactly **ten** hunks, every one of them
an intended repair. Nothing was summarised. No word was cut.

**The capitals were left alone, deliberately.** This file quotes chapters by line — `995:45` reads
*THE FIRST PIECE OF ASH HAS A GIVER IN IT* — and it carries Ilyan, Vester, Orison, Kell, Sera, Tarin,
Bram and Sena Dorr. Folding case mechanically would corrupt canon to improve typography. Recorded at
§13.12 rather than done.

### 5 — A stale README

`reviews/README.md` said "Review files will be created after the first batch." There are **534** files
under `reviews/` and **121** of them are whole-block extractions. Rewritten to say what the directory
holds, how moved blocks are named, that a moved block is still canon, and that provenance lines can be
older than the truth.

---

## Repaired in the outline, and recorded there

### 6 — A provenance claim that was false, and a finding that upgraded it

§0 claimed the file "WAS WRITTEN BY THE PHASE DISPATCHED INTO `workspace/volume-21/plan-0001/`".
That directory does not exist and was never created. `workspace/volume-18/plan-0001/`,
`volume-19/plan-0001/` and `volume-20/plan-0001/` all do exist, so the sentence was carried over from a
convention that did not hold in volume 21. §16 carried the same claim.

Worse, §13.9 did not catch it — it quoted the false sentence and answered **"AND IT WAS"**, turning a
carried-over error into a verified finding. The first write of the block that exists to find seams in
this file produced one.

Three sites repaired: §0 now names `workspace/continuation/next-0012/` and states the slots this volume
will actually run from; §13.9 now says *that is true* and says what it used to say; §16 now names
`batch-0001/` as this phase. The §13.9 paragraph records both wordings and points at §0. Written in
plain sentence case, because a finding about a file being hard to read is not well served by the style
the finding is about.

---

### 6b — One citation the review passed, checked anyway

The review reported `993:47` as verified. It is the wrong line. The quotation attributed to it — *there
is not one person on this landing going to lay a hand on it, including the man who put it down,
including me, and I put it down* — is at **`993:59`**. Line 47 is the *It is a barrow haft. That is
the name on it* speech, a different statement by the same man, and it is cited correctly at §2 and left
alone.

Corrected in four places, all of which carried the quotation: `outline/volume-21.md` §13 item 1,
`state/continuity.md` §0V21A, `state/open-threads.md`, and the prompt. `outline/volume-21.md` §2's
separate use of `993:47`, which supports a different claim and is right, was not touched. `993:43` and
`1000:41` were re-read and are correct.

A quotation cited to a line must be checked against that line, not against the chapter.

---

## Not ours, and not touched

### 7 — The review step is not running the reviewer

`scripts/novel_runner.sh:452` calls `opencode run --agent novel-reviewer`. That agent declares
`mode: subagent`, and a subagent cannot be selected by `--agent` on a primary run. opencode falls back
to the default agent, which is the writer, with `edit: allow` and `bash: allow`. Line 1 of the review
log records it verbatim: `agent "novel-reviewer" is a subagent, not a primary agent. Falling back to
default agent`.

**The phase was reviewed by the agent that wrote it, with write access.** The AGENTS.md gate "A
reviewer has checked the result" was not met and nothing in git history says so. Compounding it, the
reviewer declares `bash: deny`, so even on correct dispatch it could not `stat` a state file — which
is why defects 1 and 2 survived into the prompt.

Both files are controller-owned: `scripts/` and `.opencode/agent/`. **Not edited.** This needs an owner
of the dispatcher, and it is the highest-value item on this list.

### 8 — The phase ledger is far behind

`state/phase-ledger.json` reads `currentPhase: batch-0002`, volume 1, chapters 11–20, while the
manuscript is at volume 20 complete and `1000`. Controller-owned. **Not edited.** It will misreport
position to any reader who trusts it.

### 9 — The 60,000-byte cap is self-imposed and is fragmenting canon

The cap appears in no controller document — not `AGENTS.md`, not `PHASE_SYSTEM.md`, not `REPO_PLAN.md`,
not the series outline, not the ending. It is enforced by nothing outside itself. It stands behind
**121** whole-block extractions under `reviews/`, **99** of them from volume 20 alone, and it has moved
canon out of the exact files `AGENTS.md` tells a writer to read before writing. The seven state files
now hold **358,599** bytes of house voice, against an instruction to keep summaries compact.

Not settled, because it is not a writer's to settle: removing it would leave a hundred and twenty-one
provenance pointers claiming a reason that no longer governs anything. Recorded at
`outline/volume-21.md` §13.12 and reported. Goes to the controller owner with the same standing as the
hundred-and-fifty-chapter disagreement.

What *was* done, which is the only thing a writer may do: the prompt no longer moves anything out of
`state/` on the strength of an inherited number, and defect 2 above is this finding showing up as a
concrete instruction that would have broken a file.

---

## What this repair did not touch

The nine open threads the plan forbids a writer from settling, including the disagreement between
`991:99`, `993:47` and `995:45`/`995:49` about whether the ash has a giver in it. `outline/ending.md`
still governs, and volume 21 is still not its ending. No chapter prose was written and none was
restarted.