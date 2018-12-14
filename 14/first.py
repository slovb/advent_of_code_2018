def separate(n):
    if n > 9:
        return separate(n / 10) + [n % 10]
    return [n]

def render(scoreboard, i, j):
    out = []
    for k, s in enumerate(scoreboard):
        if k == i:
            out.append("({})".format(str(s)))
        elif k == j:
            out.append("[{}]".format(str(s)))
        else:
            out.append(" {} ".format(str(s)))
    return "".join(out)

def solve(initial, recipes):
    scoreboard = [i for i in initial] # hard copy
    i, j = 0, 1
    #print render(scoreboard, i, j)
    while len(scoreboard) < recipes + 10:
        scoreboard += separate(scoreboard[i] + scoreboard[j])
        i = (i + 1 + scoreboard[i]) % len(scoreboard)
        j = (j + 1 + scoreboard[j]) % len(scoreboard)
        #print render(scoreboard, i, j)
    return "".join([str(i) for i in scoreboard[recipes:recipes+10]])

def main(recipes):
    initial = [3, 7]
    return solve(initial, int(recipes))

import unittest
class Tester(unittest.TestCase):
    def test_example(self):
        initial = [3, 7]
        self.assertEqual(solve(initial, 9), "5158916779")
        self.assertEqual(solve(initial, 5), "0124515891")
        self.assertEqual(solve(initial, 18), "9251071085")
        self.assertEqual(solve(initial, 2018), "5941429882")

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        unittest.main()
    for a in sys.argv[1:]:
        print main(a)

