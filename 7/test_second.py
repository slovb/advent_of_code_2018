import unittest
import second as solver

class Tester(unittest.TestCase):
    def test_example(self):
        data = [
            ('C', 'A'),
            ('C', 'F'),
            ('A', 'B'),
            ('A', 'D'),
            ('B', 'E'),
            ('D', 'E'),
            ('F', 'E'),
        ]
        self.assertEqual(solver.solve(data, 2, 0), 15)

if __name__ == '__main__':
    unittest.main()

