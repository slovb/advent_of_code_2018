import unittest
import first as solver

class Tester(unittest.TestCase):
    def test_example(self):
        data = [
            "abcdef",
            "bababc",
            "abbcde",
            "abcccd",
            "aabcdd",
            "abcdee",
            "ababab"
        ]
        self.assertEqual(solver.solve(data), 12)

    def test_check_2(self):
        data = {
            "abcdef": 0,
            "bababc": 1,
            "abbcde": 1,
            "abcccd": 0,
            "aabcdd": 1,
            "abcdee": 1,
            "ababab": 0
        }
        for k, v in data.items():
            self.assertEqual(solver.check(k, 2), v)

    def test_check_3(self):
        data = {
            "abcdef": 0,
            "bababc": 1,
            "abbcde": 0,
            "abcccd": 1,
            "aabcdd": 0,
            "abcdee": 0,
            "ababab": 1
        }
        for k, v in data.items():
            self.assertEqual(solver.check(k, 3), v)

if __name__ == '__main__':
    unittest.main()

