import unittest
import second as solver

class Tester(unittest.TestCase):
    def test_example(self):
        data = solver.process([
            "#1 @ 1,3: 4x4",
            "#2 @ 3,1: 4x4",
            "#3 @ 5,5: 2x2",
        ])
        self.assertEqual(solver.solve(data), 3)

    def test_permutation_1(self):
        data = solver.process([
            "#1 @ 5,5: 2x2",
            "#2 @ 1,3: 4x4",
            "#3 @ 3,1: 4x4",
        ])
        self.assertEqual(solver.solve(data), 1)

    def test_permutation_2(self):
        data = solver.process([
            "#1 @ 3,1: 4x4",
            "#2 @ 5,5: 2x2",
            "#3 @ 1,3: 4x4",
        ])
        self.assertEqual(solver.solve(data), 2)

if __name__ == '__main__':
    unittest.main()


