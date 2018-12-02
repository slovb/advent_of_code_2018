import unittest
import second as solver

class Tester(unittest.TestCase):
    def test_example(self):
        data = [
            "abcde",
            "fghij",
            "klmno",
            "pqrst",
            "fguij",
            "axcye",
            "wvxyz"
        ]
        self.assertEqual(solver.solve(data), "fgij")

if __name__ == '__main__':
    unittest.main()

