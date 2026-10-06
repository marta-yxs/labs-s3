import unittest
from Sum-Two import add

class TwoSumTestCase(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add([2, 7, 11, 15], 9), [0, 1])

    def test_numbers(self):
        self.assertEqual(add([3, 2, 4], 6), [1, 2])

    def test_similar(self):
        self.assertEqual(add([3, 3], 6), [0, 1])

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)