#!/usr/bin/env python3
"""THE STANDING ACT, Volume 16 Band 0001.

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


def VOLOF(ch):
    """WHICH VOLUME A CHAPTER IS IN, FROM THE CHAPTER NUMBER ALONE. THE SIXTEEN
    VOLUMES ARE FIFTY CHAPTERS EACH AND THE ANCHOR IS CHAPTER 1, SO THE TEST IS
    EXACT AND IT IS THE SAME TEST `outline/` USES."""
    return 'volume-%02d' % ((ch - 1) // 50 + 1)


def last_block(ch, vol=None):
    # VOLUME 16. THE VOLUME IS DERIVED FROM THE CHAPTER NUMBER WHEN IT IS NOT
    # GIVEN, BECAUSE THE BAND OPENS AT 751 AND ITS BOUNDARY PAIR 750/751 HAS ONE
    # CHAPTER IN EACH OF TWO VOLUMES, AND A SCRIPT THAT CARRIES ONE VOLUME FOR A
    # PAIR CANNOT MEASURE THE FIRST PAIR OF A VOLUME AT ALL.
    vol = vol or VOLOF(ch)
    b = I.blocks(f'chapters/{vol}/chapter-{ch:04d}.md')
    return b[-1] if b else ''


def sim(ca, cb, vol=None):
    # EACH END OF A PAIR IS RESOLVED FROM ITS OWN CHAPTER NUMBER. THE 750/751
    # PAIR HAS ONE CHAPTER IN EACH OF TWO VOLUMES AND CARRYING ONE VOLUME FOR A
    # PAIR MEASURES A FILE THAT IS NOT THERE.
    a = ' '.join(I.WORD.findall(last_block(ca))).lower()
    b = ' '.join(I.WORD.findall(last_block(cb))).lower()
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
# VOLUME 16. THE VOLUME BOUNDARY PAIR 750/751 CROSSES TWO DIRECTORIES, SO THE
# PAIR LIST CARRIES THE VOLUME OF EACH CHAPTER RATHER THAN ONE VOLUME FOR THE
# WHOLE LIST, WHICH IS THE FIRST TIME IN THIS SCRIPT THAT THE TWO ENDS OF A PAIR
# HAVE LIVED IN DIFFERENT PLACES.
if len(sys.argv) >= 3:
    lo, hi = int(sys.argv[1]), int(sys.argv[2])

    def v(ch):
        return 'volume-15' if ch <= 750 else 'volume-16'

    pairs = [(lo - 1, lo, v(lo))] + [(c, c + 1, v(c + 1)) for c in range(lo, hi)]
else:
    # REPAIRED AGAIN AT THE REVIEW OF VOLUME 16 BAND 0001. THE DEFAULT LIST RAN
    # 751/752 THROUGH 760/761 AND `761` DOES NOT EXIST YET, SO THE SCRIPT PRINTED
    # NINE PAIRS AND THEN DIED ON A FileNotFoundError, AND THE TAIL OF ITS OWN
    # OUTPUT WAS THE TRACEBACK RATHER THAN THE BAND MAXIMUM. A BAND IS N CHAPTERS
    # AND IT HAS N MINUS ONE INSIDE PAIRS. THE LIST IS NOW CLIPPED TO THE LAST
    # CHAPTER THAT IS ON DISK, AND IT SAYS SO WHEN IT CLIPS.
    import os
    pairs = []
    for c in range(751, 761):
        if os.path.exists('chapters/volume-16/chapter-%04d.md' % (c + 1)):
            pairs.append((c, c + 1, 'volume-16'))
        else:
            print('CLIPPED: chapter-%04d.md is not on disk, so %d/%d is not '
                  'measured. THE LAST INSIDE PAIR IS %d/%d. THE VOLUME BOUNDARY '
                  'PAIR 750/751 IS ONLY REACHED BY PASSING 750 751 EXPLICITLY.'
                  % (c + 1, c, c + 1, pairs[-1][0], pairs[-1][1]), flush=True)
            break
    print('NO RANGE GIVEN. THIS IS RUNNING ITS OWN HISTORICAL BAND, 751/752 TO '
          '%d/%d, GIVE IT TWO CHAPTER NUMBERS TO MEASURE ANOTHER TEN.'
          % (pairs[-1][0], pairs[-1][1]), flush=True)
print(f'THE VOLUME BOUNDARY AND EVERY PAIR INSIDE THE BAND, '
      f'{pairs[0][0]}/{pairs[0][1]} THROUGH {pairs[-1][0]}/{pairs[-1][1]}:')
band = []
for x, y, vol in pairs:
    r = sim(x, y)
    band.append(r)
    print(f'  {x}/{y}  {r:.3f}' + ('   ** OVER 0.45 **' if r > 0.45 else ''))
print(f'  band maximum {max(band):.3f}, flag at 0.45, calibration worst drift {worst:.4f}')
