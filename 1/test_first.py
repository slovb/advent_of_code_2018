import unittest
import first as target

class Tester(unittest.TestCase):
    def testExample(self):
        self.assertEqual(target.solve([1, -2, 3, 1]), 3)
        self.assertEqual(target.solve([1, 1, 1]), 3)
        self.assertEqual(target.solve([1, 1, -2]), 0)
        self.assertEqual(target.solve([-1, -2, -3]), -6)

if __name__ == '__main__':
    unittest.main()
