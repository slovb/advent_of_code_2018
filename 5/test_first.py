import unittest
import first as solver

class Tester(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solver.solve("aA"), 0)
        self.assertEqual(solver.solve("abBA"), 0)
        self.assertEqual(solver.solve("abAB"), 4)
        self.assertEqual(solver.solve("aabAAB"), 6)
        self.assertEqual(solver.solve("dabAcCaCBAcCcaDA"), 10)

if __name__ == '__main__':
    unittest.main()


