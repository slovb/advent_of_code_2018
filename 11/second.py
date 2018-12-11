"""
def calc(total, size):
    best_x = 0
    best_y = 0
    best_t = float('-Inf')
    side = 300 - size + 2
    for y in range(1, side):
        for x in range(1, side):
            t = total(x, y, size)
            if t > best_t:
                best_x, best_y, best_t = x, y, t
    return best_x, best_y, best_t
    """

def power(x, y, serial):
    rack_id = x + 10
    p = rack_id * y
    p += serial
    p *= rack_id
    p = (p / 100) % 10
    p -= 5
    return p

def build_value_function(serial, limit):
    cache = {}
    for y in range(1, limit + 1):
        for x in range(1, limit + 1):
            cache[(x, y)] = power(x, y, serial)
    def value(x, y):
        return cache[(x, y)]
    return value

def build_total_function(value, previous, size):
    if size == 1:
        return value
    rows = {}
    cols = {}
    def total(x, y):
        p = 0
        if (x, y) in previous:
            p = previous[(x, y)]
        xmax = x + size - 1
        ymax = y + size - 1
        # sum row
        r = 0
        if (x - 1, y) in rows:
            r = rows[(x - 1, y)]
            r -= value(x - 1, ymax)
            r += value(xmax - 1, ymax)
        else:
            for i in range(size - 1):
                r += value(x + i, ymax)
        rows[(x, y)] = r
        # sum col
        c = 0
        if (x, y - 1) in cols:
            c = cols[(x, y - 1)]
            c -= value(xmax, y - 1)
            c += value(xmax, ymax - 1)
        else:
            for i in range(size - 1):
                c += value(xmax, y + i)
        cols[(x, y)] = c
        # sum total
        return p + r + c + value(x + size - 1, y + size - 1)
    return total

def solve(serial, limit = 300):
    value = build_value_function(serial, limit)
    best_x = 1
    best_y = 1
    best_s = 1
    best_t = -5
    previous = {}
    for s in range(1, limit + 1):
        current = {}
        total = build_total_function(value, previous, s)
        for y in range(1, limit + 1 - s + 1):
            for x in range(1, limit + 1 - s + 1):
                t = total(x, y)
                current[(x, y)] = t
                if t > best_t:
                    best_x, best_y, best_s, best_t = x, y, s, t
        previous = current
    return best_x, best_y, best_s

def main(serial):
    return solve(int(serial))

import unittest
class Tester(unittest.TestCase):
    def test_example(self):
        self.assertEqual(power(3, 5, 8), 4)
        self.assertEqual(power(122, 79, 57), -5)
        self.assertEqual(power(217, 196, 39), 0)
        self.assertEqual(power(101, 153, 71), 4)

    def test_example_2(self):
        self.assertEqual(solve(18), (90, 269, 16))
        self.assertEqual(solve(42), (232, 251, 12))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        unittest.main()
    for serial in sys.argv[1:]:
        print(main(serial))

