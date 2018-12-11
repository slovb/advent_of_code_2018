def power(x, y, serial):
    rack_id = x + 10
    p = rack_id * y
    p += serial
    p *= rack_id
    p = (p / 100) % 10
    p -= 5
    return p

def solve(serial):
    best_x = 0
    best_y = 0
    best = -45
    cache = {}
    def total(x, y):
        p = 0
        for j in range(3):
            for i in range(3):
                pos = (x + i, y + j)
                if pos not in cache:
                    cache[pos] = power(x + i, y + j, serial)
                p += cache[pos]
        return p
    for y in range(1, 299):
        for x in range(1, 299):
            t = total(x, y)
            if t > best:
                best = t
                best_x = x
                best_y = y
    return best, best_x, best_y

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
        self.assertEqual(solve(18), (29, 33, 45))
        self.assertEqual(solve(42), (30, 21, 61))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        unittest.main()
    for serial in sys.argv[1:]:
        print(main(serial))

