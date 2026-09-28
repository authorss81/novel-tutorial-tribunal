#!/usr/bin/env python3
"""THE PUBLISHED INSTRUMENT, as code, because it used to be a sentence of prose.

    python3 reviews/volume-10/instrument.py 491 500

THE DEFINITION, which must not be re-typed from prose by anybody (finding
nineteen: read quickly, this reads as though the word count and the paragraph
count share a basis, and they do not, and a checker who assumes otherwise gets
25,697 where the certificate says 26,391 and files a drift report against a
certificate that has not moved by one word):

  WORDS       [A-Za-z0-9\u00a3$'\\u2019-]+ over the RAW FILE. The title, the
              '---' separators and the System panel lines are INCLUDED.
  SENTENCES   a sentence ends at '.', '!' or '?', plus up to two of '\u201d"*',
              followed by whitespace or end of text. Run on the RAW FILE.
  PARAGRAPHS  blank-line-separated blocks, MINUS the title, MINUS '---', MINUS
              any block whose every non-empty line begins with '**' (a System
              panel). ONLY THIS RULE SUBTRACTS. Nothing else does.

  The four refrain figures are counted over the raw text, all four of them, and
  never one of them. The '\\u201c*' figure has two legitimate denominators and
  this file prints both: every occurrence of the two characters (the certified
  one, 181 for 491-500) and occurrences that begin a line (129, and NOT the
  certified figure -- it can be reached by moving a line break, so it is the
  one that must never be substituted).
"""
import re
import statistics
import sys
import glob

WORD = re.compile(r"[A-Za-z0-9\u00a3$’'-]+")
SENT = re.compile(r'(?<=[.!?])(?:[”"*]{0,2})(?=\s|$)')
# The sixteen wordings of the silence beat, verbatim from state/batch-summary.md
# §0, which is where they were first written down. They are here in code because
# finding seventeen's related half is that a list of strings living only in prose
# gets rebuilt from memory by the next checker, and rebuilt wrongly. The two
# wordings a memory-rebuild habitually adds -- a bare 'silence' and a bare 'quiet'
# -- are NOT wordings of the beat and are printed separately so that the
# difference between 5 and 7 is visible rather than a mystery.
SILENCE = ['said anything for about a minute', 'did not make a sound',
           'said anything at all', 'Nobody said anything', 'nobody made a noise',
           'nobody in that room said', 'the room went quiet', 'went silent',
           'nobody said anything', 'the room was silent', 'made not a sound',
           'no one said anything', 'made a noise', 'said nothing', 'no sound']
LOOSE = ['silence', 'quiet']
CHORUS = ['nobody said anything', 'nobody in that room said', 'no one said anything',
          'the room went quiet', 'went silent', 'without a word']
TICS = ['do not make it a speech', 'arbiter', 'villain', 'upstairs', 'the volume',
        'in this volume', 'month', 'Nobody said anything', 'Sorry', 'grateful',
        'thanked', 'autumn', 'spring', 'summer', 'winter', 'the rail', 'First Witness']


def paragraphs(path):
    keep = []
    for b in re.split(r'\n\s*\n', open(path, encoding='utf-8').read()):
        b = b.strip()
        if not b or b == '---' or b.startswith('# '):
            continue
        if b.startswith('**') and b.count('**') >= 2 and all(
                ln.strip().startswith('**') or not ln.strip() for ln in b.split('\n')):
            continue                                    # a System panel
        keep.append(b)
    return keep


def chapters(lo, hi, vol='volume-10'):
    return [f'chapters/{vol}/chapter-{c:04d}.md' for c in range(lo, hi + 1)]


def run(lo, hi, vol='volume-10', verbose=True):
    files = chapters(lo, hi, vol)
    raw = '\n'.join(open(f, encoding='utf-8').read() for f in files)
    words = len(WORD.findall(raw))
    segs = [s for s in SENT.split(raw) if WORD.findall(s)]
    slen = [len(WORD.findall(s)) for s in segs]
    plen = [len(WORD.findall(' '.join(p.split())))
            for f in files for p in paragraphs(f)]
    per10k = lambda x: 10000.0 * x / words
    if verbose:
        print(f'BAND {lo}-{hi}: {words} words | {len(slen)} sentences | '
              f'median {statistics.median(slen):g} (gate <= 25) | '
              f'over-60 {100.0*sum(1 for x in slen if x > 60)/len(slen):.2f}% (gate <= 10%) | '
              f'max para {max(plen)} (gate ~ 120) | max sent {max(slen)}')
        for f in files:
            r = open(f, encoding='utf-8').read()
            rs = [len(WORD.findall(s)) for s in SENT.split(r) if WORD.findall(s)]
            rp = [len(WORD.findall(' '.join(p.split()))) for p in paragraphs(f)]
            print(f'   {f[-12:-3]}  {len(WORD.findall(r)):>5} words | {len(rs):>4} sent | '
                  f'{100.0*sum(1 for x in rs if x > 60)/len(rs):5.2f}% over-60 | '
                  f'max para {max(rp)} | “* {r.count("“*")}')
        print(f'   row sums to {sum(len(WORD.findall(open(f, encoding="utf-8").read())) for f in files)},'
              f' and the band total is {words}. Those must be equal.')
        print('   REFRAINS, all four:  “*Say %d (%.1f/10k) | “*Go on %d | '
              'say the rest %d | “* every occurrence %d (%.1f/10k) | “* at line start %d (%.1f/10k)'
              % (raw.count('“*Say'), per10k(raw.count('“*Say')), raw.count('“*Go on'),
                 raw.count('say the rest'), raw.count('“*'), per10k(raw.count('“*')),
                 sum(1 for L in raw.split('\n') if L.startswith('“*')),
                 per10k(sum(1 for L in raw.split('\n') if L.startswith('“*')))))
        print('   TICS:  ' + ' | '.join(f'{t} {raw.count(t)}' for t in TICS))
        print('   straight ASCII apostrophe: %d   do not stop family: %d'
              % (raw.count("'"), len(re.findall(r'do not stop', raw))))
        s14 = sum(raw.count(s) for s in SILENCE)
        loose = {s: raw.count(s) for s in LOOSE if raw.count(s)}
        print(f'   SILENCE: {s14} across the {len(SILENCE)} wordings above; CHORUS subset: '
              f'{sum(raw.count(s) for s in CHORUS)} (gate under 10 on either)')
        print(f'   the two loose wordings, examined and kept: {loose or "none"} '
              f'-- not wordings of the beat')
        print('   PANELS:  ' + (', '.join(f'{f[-8:-3]}={open(f, encoding="utf-8").read().count("**")}**'
                                         for f in files if '**' in open(f, encoding='utf-8').read())
                               or 'none'))
    return words


if __name__ == '__main__':
    if len(sys.argv) > 2:
        run(int(sys.argv[1]), int(sys.argv[2]))
    else:
        for lo, hi in [(451, 460), (461, 470), (471, 480), (481, 490), (491, 500)]:
            run(lo, hi, verbose=False)
            print(f'band {lo}-{hi}: {run(lo, hi, verbose=False)} words')
