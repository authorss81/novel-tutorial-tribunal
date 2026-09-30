#!/usr/bin/env python3
"""THE STANDING ACT, Volume 15 Band 0004.

Method, exactly as named at state/batch-summary.md 0V15C.3 and as it has been
run for three bands running:

  * the instrument's own blocks()
  * the LAST BLOCK, WHOLE, every line of it
  * that block put through the instrument's own WORD
  * tokens joined by single spaces
  * lower-cased
  * difflib.SequenceMatcher(None, a, b).ratio()

THE CALIBRATION RUNS FIRST AND IS PRINTED WHATEVER IT COMES BACK AS, AND IT
MUST REPRODUCE THESE SEVEN:
    675/676 0.460   694/695 0.448   656/657 0.337   687/688 0.377
    662/663 0.142   685/686 0.051   682/683 0.041
A METHOD THAT DOES NOT REPRODUCE ON ITS OWN CALIBRATION IS NOT A METHOD YET.
"""
import difflib
import sys

sys.path.insert(0, 'reviews/volume-10')
import instrument as I


def last_block(ch, vol):
    b = I.blocks(f'chapters/{vol}/chapter-{ch:04d}.md')
    return b[-1] if b else ''


def sim(ca, cb, vol='volume-15'):
    a = ' '.join(I.WORD.findall(last_block(ca, vol))).lower()
    b = ' '.join(I.WORD.findall(last_block(cb, vol))).lower()
    return difflib.SequenceMatcher(None, a, b).ratio()


CAL = [(675, 676, 0.460), (694, 695, 0.448), (656, 657, 0.337), (687, 688, 0.377),
       (662, 663, 0.142), (685, 686, 0.051), (682, 683, 0.041)]

print('THE CALIBRATION, VOLUME 14, PRINTED WHATEVER IT COMES BACK AS')
worst = 0.0
for x, y, claimed in CAL:
    got = sim(x, y, 'volume-14')
    flag = 'OK' if abs(got - claimed) < 0.0006 else '** DOES NOT REPRODUCE **'
    print(f'  {x}/{y}  claimed {claimed:.3f}  got {got:.3f}  {flag}')
    worst = max(worst, abs(got - claimed))

print()
# REPAIRED AT THE REVIEW OF VOLUME 15 BAND 0005. THE PAIR LIST BELOW USED TO BE
# A LITERAL OF 730/731 ... 739/740 AND THE SCRIPT TOOK NO ARGUMENTS, SO
# `batch-0004-closing.py 741 750` RE-MEASURED THE PREVIOUS BAND AND PRINTED A
# CLEAN TABLE FOR THE WRONG TEN CHAPTERS. THE 0.284 BAND MAXIMUM THAT
# `state/index.md` AND `state/batch-summary.md` PRINT FOR 741-750 WAS THEREFORE
# NOT THE FIGURE THIS SCRIPT PRODUCED; IT CAME FROM AN AD-HOC RUN OF THE SAME
# METHOD, AND IT REPRODUCES. A PAIR LIST IS NOW AN ARGUMENT, THE HISTORICAL LIST
# IS THE DEFAULT, AND THE BAND IS ANNOUNCED BEFORE THE TABLE.
if len(sys.argv) >= 3:
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    pairs = [(lo - 1, lo, 'volume-15')] + [(c, c + 1, 'volume-15') for c in range(lo, hi)]
else:
    pairs = [(730, 731, 'volume-15'), (731, 732, 'volume-15'), (732, 733, 'volume-15'),
             (733, 734, 'volume-15'), (734, 735, 'volume-15'), (735, 736, 'volume-15'),
             (736, 737, 'volume-15'), (737, 738, 'volume-15'), (738, 739, 'volume-15'),
             (739, 740, 'volume-15')]
    print('NO RANGE GIVEN. THIS IS RUNNING ITS OWN HISTORICAL BAND, 730/731 TO '
          '739/740, GIVE IT TWO CHAPTER NUMBERS TO MEASURE ANOTHER TEN.',
          flush=True)
print(f'THE VOLUME BOUNDARY AND EVERY PAIR INSIDE THE BAND, '
      f'{pairs[0][0]}/{pairs[0][1]} THROUGH {pairs[-1][0]}/{pairs[-1][1]}:')
band = []
for x, y, vol in pairs:
    r = sim(x, y, vol)
    band.append(r)
    print(f'  {x}/{y}  {r:.3f}' + ('   ** OVER 0.45 **' if r > 0.45 else ''))
print(f'  band maximum {max(band):.3f}, flag at 0.45, calibration worst drift {worst:.4f}')
