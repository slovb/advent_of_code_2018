from sets import Set

def adjacent(p):
    x, y = p
    return [
        (x, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x, y + 1),
    ]

class Unit():
    def __init__(self, team, x, y):
        self.damage = 3
        self.hp = 200
        self.team = team
        self.x = x
        self.y = y

    def adjacent(self):
        return adjacent((self.x, self.y))

    def attack(self, unit):
        unit.hp -= self.damage
    
    def enemy(self, unit):
        return self.team != unit.team

    def is_dead(self):
        return self.hp <= 0

    def position(self):
        return (self.x, self.y)

    def render(self):
        return '{} ({})'.format(self.team, self.hp)

def render(ground, units):
    x_max = max([p[0] for p in ground])
    y_max = max([p[1] for p in ground])
    out = []
    for y in range(y_max + 2):
        line = []
        endline = []
        for x in range(x_max + 2):
            p = (x, y)
            if p in units:
                line.append(units[p].team)
                endline.append(units[p].render())
            elif p in ground:
                line.append('.')
            else:
                line.append('#')
        out.append("".join(line) + " " + " ".join(endline))
    return '\n'.join(out)

def better(pa, pb):
    return pa[1] < pb[1] or (pa[1] == pb[1] and pa[0] < pb[0])

def find(unit, ground, units, goals):
    x_max = max([p[0] for p in ground])
    weight = lambda p: p[0] + p[1] * (x_max + 1)
    # BFS
    best = {}
    def search(candidates, l = 1, previous=None):
        for c in candidates:
            if c not in ground or c in units:
                continue
            if c not in best or (c in best and l < best[c]['length']):
                    best[c] = {
                        'length': l,
                        'previous': previous,
                    }
                    search(adjacent(c), l + 1, c)
    search(unit.adjacent())
    # find the nearest, reachable
    length = float('Inf')
    goal = None
    for g in goals:
        if g in best and best[g]['length'] < length:
            length = best[g]['length']
            goal = g
    if goal is None:
        return None
    while best[goal]['previous'] != None:
        goal = best[goal]['previous']
    return goal

def simulate(ground, units):
    x_max = max([p[0] for p in ground])
    weight = lambda p: p[0] + p[1] * (x_max + 1)
    def move(u, targets):
        p = u.position()
        # find adjacent
        adjacents = []
        for tp, t in targets.items():
            ta = t.adjacent()
            for a in ta:
                if a == p: # already adjacent
                    return # don't move
                if a not in adjacents and a not in units and a in ground:
                    adjacents.append(a)
        adjacents.sort(key=weight)
        # find best shortest path
        next_p = find(u, ground, units, adjacents)
        if next_p is None: # can't move
            return # don't move
        # move
        u.x, u.y = next_p
        units[next_p] = u
        del units[p]

    def attack(u, targets):
        best = None
        for a in u.adjacent():
            if a in targets:
                t = targets[a]
                if best is None or best.hp > t.hp:
                    best = t
        if best is not None:
            u.attack(best)
            if best.is_dead():
                if best.team == 'E':
                    return False
                del units[(best.x, best.y)]
        return True

    i = 0
    while True:
        order = units.keys()
        order.sort(key=weight)

        for p in order:
            if p not in units: # dead
                continue
            u = units[p]
            # find targets
            targets = {}
            for tp, t in units.items():
                if u.enemy(t):
                    targets[tp] = t
            if len(targets) == 0:
                # Done!
                return i * sum([v.hp for _, v in units.items()])
            move(u, targets)
            elf_survived = attack(u, targets)
            if not elf_survived:
                return None
        i += 1

def solve(ground, units):
    elf_power = 3
    val = None
    while val is None:
        units_copy = {}
        for p, u in units.items():
            v = Unit(u.team, u.x, u.y)
            if v.team == 'E':
                v.damage = elf_power
            units_copy[p] = v
        val = simulate(ground, units_copy)
        elf_power += 1
    return val

def process(lines):
    ground = Set()
    units = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '.':
                ground.add((x, y))
            if c == 'G' or c == 'E':
                ground.add((x, y))
                units[(x, y)] = Unit(c, x, y)
    return ground, units

def read(filename):
    with open(filename, 'r') as f:
        ground, units = process(f.readlines())
        return ground, units

def main(filename):
    ground, units = read(filename)
    return solve(ground, units)

import unittest
class Tester(unittest.TestCase):
    def example(self, initial, outcome):
        m = filter(len, [s.strip(' ') for s in initial.split("\n")])
        ground, units = process(m)
        self.assertEqual(solve(ground, units), outcome)

    def test_example_1(self):
        initial = """
            #######
            #.G...#
            #...EG#
            #.#.#G#
            #..G#E#
            #.....#
            #######
        """
        self.example(initial, 4988)

    def test_example_3(self):
        initial = """
            #######
            #E..EG#
            #.#G.E#
            #E.##E#
            #G..#.#
            #..E#.#
            #######
        """
        self.example(initial, 31284)

    def test_example_4(self):
        initial = """
            #######
            #E.G#.#
            #.#G..#
            #G.#.G#
            #G..#.#
            #...E.#
            #######
        """
        self.example(initial, 3478)

    def test_example_5(self):
        initial = """
            #######
            #.E...#
            #.#..G#
            #.###.#
            #E#G#G#
            #...#G#
            #######
        """
        self.example(initial, 6474)

    def test_example_6(self):
        initial = """
            #########
            #G......#
            #.E.#...#
            #..##..G#
            #...##..#
            #...#...#
            #.G...G.#
            #.....G.#
            #########
        """
        self.example(initial, 1140)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        unittest.main()
    for a in sys.argv[1:]:
        print main(a)

