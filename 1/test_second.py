import unittest
import second as solver

class Tester(unittest.TestCase):
    def test_example(self):
        method = solver.solve
        self.assertEqual(method([1, -2, 3, 1]), 2)
        self.assertEqual(method([1, -1]), 0)
        self.assertEqual(method([3, 3, 4, -2, -4]), 10)
        self.assertEqual(method([-6, 3, 8, 5, -6]), 5)
        self.assertEqual(method([7, 7, -2, -7, -4]), 14)

if __name__ == '__main__':
    unittest.main()
