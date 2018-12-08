import unittest
import second as solver

class Tester(unittest.TestCase):
    def test_example(self):
        data = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
        self.assertEqual(solver.solve(data), 66)

if __name__ == '__main__':
    unittest.main()

