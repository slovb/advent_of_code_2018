from sets import Set

def adjacent(x, y):
    return [
        (x, y + 1),
        (x - 1, y),
        (x, y + 1),
        (x + 1, y),
    ]

class Unit():
    def __init__(self, team, x, y):
        self.damage = 3
        self.hp = 200
        self.team = team
        self.x = x
        self.y = y

    def adjacent(self):
        return adjacent(self.x, self.y)

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

def find(unit, ground, units, targets):
    static = {
        'limit': float('Inf')
    }
    def finder(mem, p):
        if len(mem) > static['limit']:
            return []
        paths = []
        adjacents = adjacent(p[0], p[1])
        for a in adjacents:
            if a not in ground or a in units or a in mem:
                continue
            elif a in targets:
                paths.append(mem + [a])
                static['limit'] = min(1 + len(mem), static['limit'])
            else:
                for path in finder(mem + [a], a):
                    paths.append(path)
        return paths
    return finder([], (unit.x, unit.y))

def solve(ground, units):
    def move(u, targets):
        p = u.position()
        # find adjacent
        adjacents = Set()
        for tp, t in targets.items():
            ta = t.adjacent()
            for a in ta:
                if a == p: # already adjacent
                    print "{} ALREADY ADJACENT".format(p)
                    return # don't move
                if a not in units and a in ground:
                    adjacents.add(a)
        # find shortest paths
        paths = find(u, ground, units, targets)
        if len(paths) == 0: # can't move
            print "{} CANT MOVE".format(p)
            return # don't move
        best = paths[0]
        for path in paths[1:]:
            # they are both of shortest length, thus sam length
            for k in range(len(path)):
                if best[k] != path[k]:
                    if best[k] > path[k]:
                        best = path
                    break
        # move
        print "{} MOVE {}".format(p, best[0])
        u.x, u.y = best[0]
        units[best[0]] = u
        del units[p]

    def attack(u, targets):
        for a in u.adjacent():
            if a in targets:
                t = targets[a]
                print "{} ATTACK {}".format(u.position(), t.position())
                u.attack(t)
                if t.is_dead():
                    del units[a]
                return
        print "{} NO ATTACK".format(u.position())
    print render(ground, units)
    i = 0
    while True:
        order = units.keys()
        order.sort()
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
                return i * sum([v.hp for v in units])
            move(u, targets)
            attack(u, targets)
        print " "
        print render(ground, units)
        return -1
        i += 1

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
        self.example(initial, 27730)

    def _test_example_2(self):
        initial = """
            #######
            #G..#E#
            #E#E.E#
            #G.##.#
            #...#E#
            #...E.#
            #######
        """
        self.example(initial, 36334)

    def _test_example_3(self):
        initial = """
            #######
            #E..EG#
            #.#G.E#
            #E.##E#
            #G..#.#
            #..E#.#
            #######
        """
        self.example(initial, 39514)

    def _test_example_4(self):
        initial = """
            #######
            #E.G#.#
            #.#G..#
            #G.#.G#
            #G..#.#
            #...E.#
            #######
        """
        self.example(initial, 27755)

    def _test_example_5(self):
        initial = """
            #######
            #.E...#
            #.#..G#
            #.###.#
            #E#G#G#
            #...#G#
            #######
        """
        self.example(initial, 28944)

    def _test_example_6(self):
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
        self.example(initial, 18740)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        unittest.main()
    for a in sys.argv[1:]:
        print main(a)

