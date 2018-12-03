import unittest
import first as solver

class Tester(unittest.TestCase):
    def test_example(self):
        data = solver.process([
            "#1 @ 1,3: 4x4",
            "#2 @ 3,1: 4x4",
            "#3 @ 5,5: 2x2",
        ])
        self.assertEqual(solver.solve(data), 4)

    def test_multiple(self):
        data = solver.process([
            "#1 @ 1,3: 4x4",
            "#2 @ 3,1: 4x4",
            "#3 @ 5,5: 2x2",
            "#4 @ 3,3: 2x2",
            "#5 @ 3,3: 2x2",
            "#6 @ 3,3: 2x2",
            "#7 @ 3,3: 2x2",
        ])
        self.assertEqual(solver.solve(data), 4)

if __name__ == '__main__':
    unittest.main()


