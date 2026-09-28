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
              followed by whitespace or end of text. COUNTED PER PARAGRAPH
              BLOCK AND NEVER ACROSS A BLANK LINE. This is the rule that was
              missing and it is why the instrument used to print 132 where the
              certificates said 126: a title carries no terminal punctuation, so
              a whole-file split swallowed a title and the first sentence of
              the date line under it and reported the sum as one sentence. A
              title is a sentence, is measured as one, and is not repairable.
              NOTE FOR THE NEXT CHECKER: the two remedies that read as obvious
              are both wrong. Splitting per FILE instead of per block returns
              the same 132, because the merge is inside one file, not across
              two. Stripping the title before splitting returns 73 and throws
              away the 126 the certificates print. Only the per-block rule
              reproduces both certified figures, 126 and 115.
  PARAGRAPHS  blank-line-separated blocks, MINUS the title, MINUS '---', MINUS
              any block whose every non-empty line begins with '**' (a System
              panel). ONLY THIS RULE SUBTRACTS. Nothing else does.

  The four refrain figures are counted over the raw text, all four of them, and
  never one of them. The '\u201c*' figure has two legitimate denominators and
  this file prints both: every occurrence of the two characters (the certified
  one, 181 for 491-500) and occurrences that begin a line (129, and NOT the
  certified figure -- it can be reached by moving a line break, so it is the
  one that must never be substituted).

  THE RESERVED-NUMBER GUARD IS SWEPT ACROSS EVERY CHAPTER OF THE VOLUME BY
  'guards', never across the band that was just repaired (finding eighteen). It
  is CASE-INSENSITIVE, which the hand sweep that found the first nine was not,
  and that is how a title came to say Four Hundred People for a whole phase.
  The tool flags; it does not judge. Every hit is printed with its line number
  and the noun in front of it, and a human reads the list.
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


def blocks(path):
    """Every non-empty blank-line-separated block, title and System panels
    INCLUDED. This is the unit the sentence rule is defined on."""
    return [b.strip() for b in re.split(r'\n\s*\n', open(path, encoding='utf-8').read())
            if b.strip() and b.strip() != '---']


def sentences(path):
    segs = [s for b in blocks(path) for s in SENT.split(b) if WORD.findall(s)]
    return [len(WORD.findall(s)) for s in segs]


def paragraphs(path):
    keep = []
    for b in blocks(path):
        if b.startswith('# '):
            continue
        if b.startswith('**') and b.count('**') >= 2 and all(
                ln.strip().startswith('**') or not ln.strip() for ln in b.split('\n')):
            continue                                    # a System panel
        keep.append(b)
    return keep


def chapters(lo, hi, vol='volume-10'):
    return [f'chapters/{vol}/chapter-{c:04d}.md' for c in range(lo, hi + 1)]


# The noun a reader judges a reserved-number hit by. This does not decide the
# hit -- a human does -- it only sorts the list so the reading is one pass.
CROWD = ('people', 'persons', 'men', 'women', 'households', 'families', 'heads',
         'children', 'boys', 'girls', 'crowd', 'souls', 'neighbours')
UNIT = ('years', 'miles', 'yards', 'acres', 'times', 'lines', 'words', 'forms',
        'pence', 'days', 'weeks', 'feet', 'pounds', 'shillings', 'inches')
NOUN = re.compile(r'\b(' + '|'.join(CROWD) + r')\b', re.I)


def guards(lo=451, hi=500, vol='volume-10'):
    """Finding eighteen, as code. A guard swept over the band you just repaired
    is a guard that will be reported as holding while the rest of the volume
    fails it, so this sweeps every chapter of the volume and prints every hit.
    Case-insensitive: a title capitalises, and a case-sensitive sweep misses
    every title in the volume."""
    total = hits = 0
    print(f'RESERVED-NUMBER GUARD, {lo}-{hi}, every chapter, case-insensitive:')
    for f in chapters(lo, hi, vol):
        for n, line in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
            for m in re.finditer(r'four hundred', line, re.I):
                total += 1
                after = line[m.end():m.end() + 24].lstrip()
                noun = NOUN.search(line[max(0, m.start() - 40):m.end() + 24])
                if noun and noun.group(1).lower() in CROWD:
                    hits += 1
                    flag = 'crowd noun near'
                elif after.split(' ')[0].rstrip(',.').lower() in UNIT:
                    flag = 'count of a unit'
                else:
                    flag = 'read it        '
                ctx = line[max(0, m.start() - 46):m.end() + 46].strip()
                print(f'   {f[-13:-3]}:{n:<4} {flag}  ...{ctx}...')
    print(f'   {total} occurrences of the number in {hi - lo + 1} chapters, '
          f'{hits} of them with a crowd noun within forty characters.')
    print('   The flag is a READING AID AND IT HAS FALSE POSITIVES. Forty characters '
          'is a wide window, so a permitted "four hundred yards" beside a crowd noun '
          'is flagged, and "a building of four hundred people" -- the one crowd the '
          'number is allowed to govern -- is flagged too. Do not certify a guard by '
          'the count on this line. Certify it by reading all '
          f'{total} of them, which is the only part of this file that is a gate.')


def run(lo, hi, vol='volume-10', verbose=True):
    files = chapters(lo, hi, vol)
    raw = '\n'.join(open(f, encoding='utf-8').read() for f in files)
    words = len(WORD.findall(raw))
    per = {f: sentences(f) for f in files}
    slen = [n for f in files for n in per[f]]
    plen = [len(WORD.findall(' '.join(p.split())))
            for f in files for p in paragraphs(f)]
    per10k = lambda x: 10000.0 * x / words
    if verbose:
        print(f'BAND {lo}-{hi}: {words} words | {len(slen)} sentences | '
              f'median {statistics.median(slen):g} (gate <= 25) | '
              f'over-60 {100.0*sum(1 for x in slen if x > 60)/len(slen):.2f}% (gate <= 10%) | '
              f'max para {max(plen)} (gate ~ 120) | max sent {max(slen)}')
        for f in files:
            rs = per[f]
            rp = [len(WORD.findall(' '.join(p.split()))) for p in paragraphs(f)]
            print(f'   {f[-12:-3]}  {len(WORD.findall(open(f, encoding="utf-8").read())):>5} words | '
                  f'{len(rs):>4} sent | '
                  f'{100.0*sum(1 for x in rs if x > 60)/len(rs):5.2f}% over-60 | '
                  f'max para {max(rp)} | max sent {max(rs)} | “* {open(f, encoding="utf-8").read().count("“*")}')

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
    if len(sys.argv) > 1 and sys.argv[1] == 'guards':
        guards()
    elif len(sys.argv) > 2:
        run(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print('ALL FIVE BANDS.  python3 instrument.py 491 500   for one band.   '
              'python3 instrument.py guards   for the volume-wide guard sweep.')
        for lo, hi in [(451, 460), (461, 470), (471, 480), (481, 490), (491, 500)]:
            run(lo, hi, verbose=False)
            print(f'band {lo}-{hi}: {run(lo, hi, verbose=False)} words')
