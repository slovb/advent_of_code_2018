import unittest
import first as solver

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
        self.assertEqual(solver.solve(data), 'CABDFE')

if __name__ == '__main__':
    unittest.main()

