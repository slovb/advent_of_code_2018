import unittest
import first as solver

class Tester(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solver.solve([1, -2, 3, 1]), 3)
        self.assertEqual(solver.solve([1, 1, 1]), 3)
        self.assertEqual(solver.solve([1, 1, -2]), 0)
        self.assertEqual(solver.solve([-1, -2, -3]), -6)

if __name__ == '__main__':
    unittest.main()
