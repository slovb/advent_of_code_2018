import unittest
import second as solver

class Tester(unittest.TestCase):
    def test_example(self):
        data = [
            (1, 1),
            (1, 6),
            (8, 3),
            (3, 4),
            (5, 5),
            (8, 9),
        ]
        self.assertEqual(solver.solve(data, 32), 16)

if __name__ == '__main__':
    unittest.main()

