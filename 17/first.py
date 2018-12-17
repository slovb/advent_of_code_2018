class WaterNode:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.settle_left = False
        self.settle_right = False
        self.settle_bottom = False

    def settled(self):
        return self.settle_left and self.settle_right and self.settle_bottom

    def above(self):
        return (self.x, self.y - 1)

    def left(self):
        return (self.x - 1, self.y)

    def below(self):
        return (self.x, self.y + 1)

    def right(self):
        return (self.x + 1, self.y)

    def position(self):
        return (self.x, self.y)

def render(limits, spring, claymap, water):
    out = []
    for y in range(limits['min_y'], limits['max_y'] + 1):
        line = []
        for x in range(limits['min_x'], limits['max_x'] + 1):
            p = (x, y)
            if p == spring:
                line.append('+')
            elif p in claymap:
                line.append('#')
            elif p in water:
                w = water[p]
                if w.settled():
                    line.append('~')
                else:
                    line.append('|')
            else:
                line.append('.')
        out.append(''.join(line))
    return '\n'.join(out)


def map_clay(clay):
    lval = lambda z: z if not isinstance(z, tuple) else z[0]
    rval = lambda z: z if not isinstance(z, tuple) else z[1]
    from sets import Set
    claymap = Set()
    min_x = lval(clay[0]['x'])
    max_x = rval(clay[0]['x'])
    min_y = lval(clay[0]['y'])
    max_y = rval(clay[0]['y'])
    for c in clay:
        lval_x, rval_x = lval(c['x']), rval(c['x'])
        lval_y, rval_y = lval(c['y']), rval(c['y'])
        min_x = min(lval_x, min_x)
        max_x = max(rval_x, max_x)
        min_y = min(lval_y, min_y)
        max_y = max(rval_y, max_y)
        for y in range(lval_y, rval_y + 1):
            for x in range(lval_x, rval_x + 1):
                claymap.add((x, y))
    limits = {
        'min_x': min_x,
        'max_x': max_x,
        'min_y': min_y,
        'max_y': max_y,
    }
    return claymap, limits

def solve(spring, clay):
    claymap, limits = map_clay(clay)
    water = {
        (spring): WaterNode(spring)
    }
    def spread(w):
        p = w.position()
        if w.settled():
            if w.above() in claymap:
                pass
            elif w.above() in water: # if water is falling from above, make
                                     # sure it spreads
                above = water[w.above()]
                above.settle_bottom = True
                spread(above)
        elif w.settle_bottom:
            if not w.settle_left:
                if w.left() in claymap:
                    w.settle_left = True
                    spread(w)
                elif w.left() in water:
                    left = water[w.left()]
                    if left.settle_left:
                        w.settle_left = True
                        spread(w)
                else:
                    left = WaterNode(w.left())
                    water[w.left()] = left
                    spread(left)
            else: # propagate settling
                if w.right() in water:
                    right = water[w.right()]
                    if not right.settle_left:
                        right.settle_left = True
                        spread(right)

            if not w.settle_right:
                if w.right() in claymap:
                    w.settle_right = True
                    spread(w)
                elif w.right() in water:
                    right = water[w.right()]
                    if right.settle_right:
                        w.settle_right = True
                        spread(w)
                else:
                    right = WaterNode(w.right())
                    water[w.right()] = right
                    spread(right)
            else: # propagate settling
                if w.left() in water:
                    left = water[w.left()]
                    if not left.settle_right:
                        left.settle_right = True
                        spread(left)
        else:
            if w.below() in claymap:
                w.settle_bottom = True
                spread(w)
            elif w.below() in water:
                below = water[w.below()]
                spread(below)
            else:
                below = WaterNode(w.below())
                if below.y <= limits['max_y']:
                    water[below.position()] = below
                    spread(below)
    spread(water[spring])
    print render(limits, spring, claymap, water)
    count = len(water)
    for position in water:
        if position[1] < limits['min_y']:
            count -= 1
    return count

def process(line):
    import re
    extract = lambda l: map(int, re.findall(r'\d+', l))
    i = extract(line)
    entry = {}
    if line[0] == 'x':
        entry['x'] = i[0]
        entry['y'] = (i[1], i[2])
    else:
        entry['x'] = (i[1], i[2])
        entry['y'] = i[0]
    return entry

def read(filename):
    with open(filename, 'r') as f:
        clay = []
        for line in f.readlines():
            clay.append(process(line))
        return clay

def main(filename):
    spring = (500, 0)
    clay = read(filename)
    return solve(spring, clay)

import unittest
class Tester(unittest.TestCase):
    def test_example_input(self):
        data = """x=495, y=2..7
            	  y=7, x=495..501
            	  x=501, y=3..7
            	  x=498, y=2..4
                  x=506, y=1..2
            	  x=498, y=10..13
                  x=504, y=10..13
                  y=13, x=498..504"""
        clay = [process(l.strip()) for l in data.split('\n')]
    	spring = (500, 0)
        self.assertEqual(solve(spring, clay), 57)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        unittest.main()
    for a in sys.argv[1:]:
        print main(a)

