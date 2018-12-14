def match(scoreboard, target):
    l = len(target)
    for i in range(l):
        if target[-i-1] != scoreboard[-i-1]:
            return False
    return True

def separate(n):
    if n > 9:
        return separate(n / 10) + [n % 10]
    return [n]

def render(scoreboard):
    return "".join([str(s) for s in scoreboard])

def solve(initial, target):
    scoreboard = [i for i in initial] # hard copy
    i, j = 0, 1
    while True:
        v = separate(scoreboard[i] + scoreboard[j])
        for u in v:
            scoreboard += [u]
            if match(scoreboard, target):
                return len(scoreboard) - len(target)
        i = (i + 1 + scoreboard[i]) % len(scoreboard)
        j = (j + 1 + scoreboard[j]) % len(scoreboard)


def main(target):
    initial = [3, 7]
    return solve(initial, [int(c) for c in target])

import unittest
class Tester(unittest.TestCase):
    def test_match(self):
        self.assertTrue(match(separate(37101012451589), separate(51589)))
        self.assertFalse(match(separate(3710101245158), separate(51589)))
        self.assertFalse(match(separate(371010124515891), separate(51589)))

    def test_example(self):
        initial = [3, 7]
        self.assertEqual(solve(initial, [5, 1, 5, 8, 9]), 9)
        self.assertEqual(solve(initial, [0, 1, 2, 4, 5]), 5)
        self.assertEqual(solve(initial, [9, 2, 5, 1, 0]), 18)
        self.assertEqual(solve(initial, [5, 9, 4, 1, 4]), 2018)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        unittest.main()
    for a in sys.argv[1:]:
        print main(a)

