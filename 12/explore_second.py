from sets import Set

def simulate(state, ruleset):
    def get(x):
        local = []
        for i in range(-2, 3):
            if x + i in state:
                local.append(i)
        return tuple(local)
    llim = min(state)
    rlim = max(state)
    current = Set()
    for x in range(llim-3, rlim+4):
        if get(x) in ruleset:
            current.add(x)
    return current

def render(state, llim = None, rlim = None):
    if llim is None:
        llim = min(state)
    if rlim is None:
        rlim = max(state)
    out = []
    for x in range(llim, rlim+1):
        out.append('#' if x in state else '.')
    return "".join(out)

def calc(state, ruleset, steps=20):
    i = 0
    prev = sum(state)
    while i < steps:
        #print render(state)
        state = simulate(state, ruleset)
        i += 1
        val = sum(state)
        print i, val, val - prev
        prev = val
    return sum(state)

def process(initial, rules):
    state = Set()
    for k, c in enumerate(initial):
        if c == "#":
            state.add(k)
    # ..#.. => (0)
    # #.#.# => (-2, 0, 2)
    ruleset = Set()
    for rule, val in rules.items():
        if val == '#':
            r = []
            for k, c in enumerate(rule):
                if c == '#':
                    r.append(k - 2)
            ruleset.add(tuple(r))
    return state, ruleset

def read(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        initial = lines[0].split()[2]
        rules = {}
        for l in lines[2:]:
            parts = l.split()
            rules[parts[0]] = parts[2]
        return initial, rules

def main(filename):
    initial, rules = read(filename)
    state, ruleset = process(initial, rules)
    steps = 50000000000
    return calc(state, ruleset, steps)

import unittest
class Tester(unittest.TestCase):
    def test_example(self):
        initial = "#..#.#..##......###...###"
        rules = {
            "...##": "#",
            "..#..": "#",
            ".#...": "#",
            ".#.#.": "#",
            ".#.##": "#",
            ".##..": "#",
            ".####": "#",
            "#.#.#": "#",
            "#.###": "#",
            "##.#.": "#",
            "##.##": "#",
            "###..": "#",
            "###.#": "#",
            "####.": "#",
        }
        state, ruleset = process(initial, rules)
        results = [
            145, 91, 132, 102, 154,
            115, 174, 126, 213, 138,
            213, 136, 218, 133, 235,
            149, 226, 170, 280, 287,
            325
        ]
        for steps, result in enumerate(results):
            self.assertEqual(calc(state, ruleset, steps), result)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        unittest.main()
    for f in sys.argv[1:]:
        print main(f)

