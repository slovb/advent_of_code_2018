from sets import Set

def adjacent(x, y):
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

def better(pa, pb):
    return pa[1] < pb[1] or (pa[1] == pb[1] and pa[0] < pb[0])

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
                    if len(path) <= static['limit']:
                        paths.append(path)
        return paths
    paths = finder([], (unit.x, unit.y))
    # filter out long solutions
    shorts = []
    for p in paths:
        if len(p) <= static['limit']:
            shorts.append(p)
    if len(shorts) == 0:
        return None
    # filter out best end, and then return the first of those, in ordering
    best = shorts[0]
    for p in shorts[1:]:
        if better(p[-1], best[-1]):
            best = p
    return best


def solve(ground, units):
    def move(u, targets):
        p = u.position()
        # find adjacent
        adjacents = Set()
        for tp, t in targets.items():
            ta = t.adjacent()
            for a in ta:
                if a == p: # already adjacent
                    #print "{} ALREADY ADJACENT".format(p)
                    return # don't move
                if a not in units and a in ground:
                    adjacents.add(a)
        # find best shortest path
        path = find(u, ground, units, adjacents)
        if path is None: # can't move
            #print "{} CANT MOVE".format(p)
            return # don't move
        # move
        #print "{} MOVE {}".format(p, path[0])
        u.x, u.y = path[0]
        units[path[0]] = u
        del units[p]

    def attack(u, targets):
        best = None
        for a in u.adjacent():
            if a in targets:
                t = targets[a]
                if best is None or best.hp > t.hp:
                    best = t
        if best is not None:
            #print "{} ATTACK {}".format(u.position(), best.position())
            u.attack(best)
            if best.is_dead():
                del units[(best.x, best.y)]
        else:
            #print "{} NO ATTACK".format(u.position())
            pass

    #print render(ground, units)
    #print " "
    i = 0
    x_max = max([p[0] for p in ground])
    weight = lambda p: p[0] + p[1] * (x_max + 1)
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
                #print i, sum([v.hp for _, v in units.items()])
                #print render(ground, units)
                return i * sum([v.hp for _, v in units.items()])
            move(u, targets)
            attack(u, targets)
        i += 1
        #print i
        #print render(ground, units)
        #print " "

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

    def test_example_2(self):
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
        self.example(initial, 39514)

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
        self.example(initial, 27755)

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
        self.example(initial, 28944)

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
        self.example(initial, 18740)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        unittest.main()
    for a in sys.argv[1:]:
        print main(a)

