def parse(s):
    count = []
    counts = []
    i = 0
    depth = 0
    j = None
    while i < len(s):
        if s[i] == '^' or s[i] == '$':
            pass
        elif s[i] == '(':
            if depth == 0:
                j = i
            depth += 1
        elif s[i] == ')':
            depth -= 1
            if depth == 0:
                count += parse(s[j+1:i])
        elif depth > 0:
            pass
        elif s[i] == '|':
            counts.append(count)
            count = []
        else:
            count.append(s[i])
        i += 1
    # if skippable return empty
    if count == []:
        #print s + " = []"
        return []
    # if not skippable, return max
    counts.append(count)
    best = max(counts, key=len)
    #print s + " = " + "".join(best)
    return best

def solve(data):
    return len(parse(data))

def read(filename):
    with open(filename, 'r') as f:
        return f.readline().strip()

def main(filename):
    rows = read(filename)
    return solve(rows)

import unittest
class Tester(unittest.TestCase):
    def test_example_input(self):
        t = lambda d, e: self.assertEqual(solve(d), e)
        t('(^WNE$)', 3)
        t('(^ENWWW(NEEE|SSE(EE|N))$)', 10)
        t('(^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$)',18)
        t('^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$',23)
        t('^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$',31)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        unittest.main()
    for a in sys.argv[1:]:
        print main(a)

