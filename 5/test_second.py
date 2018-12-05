import unittest
import second as solver

class Tester(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solver.solve("aA"), 0)
        self.assertEqual(solver.solve("abBA"), 0)
        self.assertEqual(solver.solve("abAB"), 0)
        self.assertEqual(solver.solve("aabAAB"), 0)
        self.assertEqual(solver.solve("dabAcCaCBAcCcaDA"), 4)

if __name__ == '__main__':
    unittest.main()


