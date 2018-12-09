import unittest
import solution as solver

class Tester(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solver.solve(9, 25), 32)
        self.assertEqual(solver.solve(10, 1618), 8317)
        self.assertEqual(solver.solve(13, 7999), 146373)
        self.assertEqual(solver.solve(17, 1104), 2764)
        self.assertEqual(solver.solve(21, 6111), 54718)
        self.assertEqual(solver.solve(30, 5807), 37305)

if __name__ == '__main__':
    unittest.main()

