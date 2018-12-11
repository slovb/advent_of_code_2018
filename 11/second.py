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

def power(x, y, serial):
    rack_id = x + 10
    p = rack_id * y
    p += serial
    p *= rack_id
    p = (p / 100) % 10
    p -= 5
    return p

def solve(serial):
    cache = {}
    def total(x, y, size):
        p = 0
        for j in range(size):
            for i in range(size):
                pos = (x + i, y + j)
                if pos not in cache:
                    cache[pos] = power(x + i, y + j, serial)
                p += cache[pos]
        return p
    best_x = 1
    best_y = 1
    best_s = 1
    best_t = total(best_x, best_y, best_s)
    for s in range(1, 300 + 1):
        print best_x, best_y, best_s, best_t
        x, y, t = calc(total, s)
        if t > best_t:
            best_x, best_y, best_s, best_t = x, y, s, t
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

