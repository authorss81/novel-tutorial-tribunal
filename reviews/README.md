# reviews/

Review receipts, repair records, and whole blocks of canon moved out of the `state/` files by a
60,000-byte cap those files are held to. Nothing here is a summary of a batch; the summaries live
in `state/`. A file named `*-moved-block-*` is a block that used to sit inside a `state/` file and
was relocated here whole, with a pointer left behind in the file it left.

Naming: `<volume>/<batch>-<state-file>-moved-block-<id>.md`, and `<volume>/<batch>-receipt-<id>.md`
for a batch's receipt. The `<id>` is the section number the block carried in the file it left, so
every pointer elsewhere resolves.

One volume here is a close rather than a batch — `volume-20/batch-0007-close-0V20K.md` — and a close
owes no chapter.

Two things a reader should know before trusting anything in here:

- **A moved block is still canon.** It was moved, never summarised. Nothing in it was cut.
- **Provenance lines can be older than the truth.** Where a receipt and this directory disagree with
  each other, the later file wins, and both are meant to say so. `outline/volume-21.md` §13 is the
  current example: it records a repair that its own first write got wrong.