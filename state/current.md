# current

Where the project stands at the end of volume 21 band 4. This file holds the live
record only. Anything that belongs to a finished band lives in
`state/batch-summary.md`; anything long-form lives in `state/continuity.md`.

## Status

- **Novel:** *The Tutorial Tribunal* — Ilyan Vester, a legal fantasy in which every
  adventure is a bounded case about a real conflict, a real burden, and a remedy
  people have to live with afterward.
- **Current volume:** 21, *The Name Already On It*, chapters 1001–1050.
- **Bands written:** 1001–1010, 1011–1020, 1021–1030, **1031–1040 (band 4, complete).**
- **Next phase:** `workspace/volume-21/batch-0005/PROMPT.md` — chapters 1041–1050,
  the volume's climax band and its last ten chapters.
- **Chapters on disk:** 1040, in 21 directories of 50, 50, … 50, 40.

## Two decisions that are not the writer's

These are recorded here because every band so far has re-reported them and nobody
has answered them. They are **not resolved in this file**, and no band may resolve
them by writing more chapters.

1. **The book is 190 chapters past the ending its own outline specifies.**
   `outline/series.md` gives "approximately 850 chapters" in 17 volumes;
   `outline/ending.md` ends at chapter 850, *The visible rule*, and that chapter is
   finished on disk at `chapters/volume-17/chapter-0850.md`. Volumes 18–21
   (`851`–`1040`) rest on no authority but repetition. `outline/volume-21.md` §0
   states the disagreement in its own opening section and marks the owner as
   "nobody written down". Either the outline is rewritten and the book continues, or
   the book stops and 190 chapters need an explicit, recorded decision. **A writer
   cannot make this call and must not pretend to have made it.**
2. **State files were reset on the review of band 4.** The seven state files had
   grown to 373 KB between them against a self-declared 60 KB cap for each, with
   most of that content given to self-measurement, pointer bookkeeping and
   prohibition counts instead of story. They now stand at 54 KB between them. The
   pre-reset blocks are not deleted: everything that had already been moved out is
   whole under `reviews/volume-*/`, and material that was live in `state/*.md` at the
   moment of the reset is whole in that reset's commit. See `reviews/volume-21/
   batch-0005-review-repair.md`.

## The live record at chapter 1040

- **Landing:** a bank of cut stone with about ninety steps, a fortieth step with
  iron in its seam, a chair nobody owns, a lane, a drain, a cart road, a wall at the
  bottom of the cart road, and a dry strip at the top end carrying two pieces of ash.
- **Water on the top step:** 16 inches and holding; about sixty of the ninety steps
  under; two days of the coming back.
- **Ilyan's figures, all read off the page:** 790 mornings; 640 days after the
  settlement; 486 days in the county of Kell (`ch − 554`); the cut across his palm
  355 days old (`ch − 685`); the standing offer 340 days old and unanswered
  (`ch − 700`); his own count of wrong things 180, and a whole figure.
- **The offer:** asked on no morning of the band, answered on none, withdrawn on
  none. The subtraction is spoken aloud every morning by him.
- **Barnaby Crove's count:** three hundred and nineteenth morning of asking.
- **Unchanged and still true:** the name on the second piece of ash is still wrong;
  the account is incomplete and in use; the right of refusal is not restored in any
  wording; nobody has been relieved, forgiven or thanked for anything.

## What band 4 added

- A name got off that landing **without a carrier**, and the woman it reached is the
  one person there who knows what that wood is, and will not say it.
- A man with a broom said out loud that the name is for somebody on that landing,
  that he does not know which, and gave the working for not finding out.
- He offered the landing a sentence to say every morning, and took it back inside
  the same week, because a man who says a thing every morning becomes a thing that
  is said.
- A man who cannot see well held his hand out past the end of the wall, in the air
  over that strip, and brought it back without touching anything, and nobody put it
  there.
- A man who cannot read said he would rather be owed nothing he cannot check than be
  lied to about in a year.
- The ordinary form — a thing cut for a use is not the user's — was said out loud in
  four trades on three mornings and was given no name.
- A woman who keeps twenty-nine chairs was refused her one question and went back to
  her wall. A man of thirty-eight was told there is no job and said so himself.

## Quality repairs applied to band 4 after review

Recorded so the next band does not reintroduce them:

- The paragraph beginning "Nothing on that landing was pulled…" was byte-identical
  in nine chapters. Each of the ten now says it in its own words, and no two
  chapters repeat a paragraph. See `reviews/volume-21/batch-0005-review-repair.md`.
- The lead was named only in a descriptor line on each of the ten mornings.
  `outline/volume-21.md` §7 requires him named in every chapter; he is now named in
  the prose of all ten (3–5 times each).
- Three chapters had a speaker addressing Ilyan before he had arrived, and one had
  him arrive twice. Visit order and arrivals were corrected in 1032, 1033, 1035.
- Chapter titles ran 125–159 words. All ten are now short, name nothing, and print no
  figure, per §7. The titles of bands 1–3 have not been touched and are owed to the
  volume 21 close; see `state/open-threads.md`.
- Descriptor paragraphs were trimmed where they restated the speech beneath them, and
  the two long prose runs that every chapter repeated word for word — the description
  of the two pieces of ash and the account of the sweep — were rewritten in each of
  the ten. Eighteen paragraphs ran over a thousand characters; all of them were split,
  and the longest in the band is now 986.

## Archive

Pre-reset state blocks, review receipts and verification scripts are under
`reviews/volume-01/` … `reviews/volume-21/`. They are evidence, not live state.