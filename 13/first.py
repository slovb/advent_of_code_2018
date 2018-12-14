def render(track, carts, crashes):
    directions = ['^', '>', 'v', '<']
    out = []
    max_x = 0
    max_y = 0
    for p in track:
        x, y = p
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    for y in range(max_y + 1):
        line = []
        for x in range(max_x + 1):
            p = (x, y)
            if p not in track:
                line.append(' ')
            elif p in crashes:
                line.append('X')
            elif p in carts:
                line.append(directions[carts[p]['direction']])
            else:
                line.append(track[p])
        out.append("".join(line))
    return "\n".join(out)

def simulate(track, carts):
    directions = {
        0: (0, -1), # ^
        1: (1, 0),  # >
        2: (0, 1),  # v
        3: (-1, 0), # <
    }
    crashes = []
    updated = {}
    positions = carts.keys()
    positions.sort() # requirement
    for k, position in enumerate(positions):
        if position in updated:
            crashes.append(position)
        cart = carts[position]
        counter = cart['counter']
        d = cart['direction']
        increment = directions[d]
        p = (position[0] + increment[0], position[1] + increment[1])
        t = track[p]
        if t in ['|', '-']:
            pass
        elif t == '+':
            d = (d + counter - 1) % 4
            counter = (counter + 1) % 3
        elif t == '/':
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2
        else: # \
            if d == 0:
                d = 3
            elif d == 1:
                d = 2
            elif d == 2:
                d = 1
            elif d == 3:
                d = 0
        if p in updated:
            crashes.append(p)
        updated[p] = {
            'counter': counter,
            'direction': d,
        }
    return updated, crashes

def solve(track, carts):
    #print render(track, carts, {})
    while True:
        carts, crashes = simulate(track, carts)
        #print render(track, carts, crashes)
        if len(crashes) > 0:
            return crashes[0]

def process(lines):
    # assume nice input until prove otherwise (no cart start on turn)
    track = {}
    carts = {}
    directions = ['^', '>', 'v', '<']
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ' ':
                continue
            if c in directions:
                d = directions.index(c)
                if d % 2 == 0:
                    track[(x, y)] = '|'
                else:
                    track[(x, y)] = '-'
                carts[(x, y)] = {
                    'counter': 0,
                    'direction': d,
                }
            else:
                track[(x, y)] = c
    return track, carts

def read(filename):
    with open(filename, 'r') as f:
        lines = [l.strip('\n') for l in f.readlines()]
        track, carts = process(lines)
        return track, carts

def main(filename):
    track, carts = read(filename)
    return solve(track, carts)

import unittest
class Tester(unittest.TestCase):
    def test_example(self):
        lines = [
            "/->-\         ",
            "|   |  /----\ ",
            "| /-+--+-\  | ",
            "| | |  | v  | ",
            "\-+-/  \-+--/ ",
            "  \------/    ",
        ]
        track, carts = process(lines)
        self.assertEqual(solve(track, carts), (7, 3))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        unittest.main()
    for f in sys.argv[1:]:
        print main(f)

