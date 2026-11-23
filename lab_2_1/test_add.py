import unittest
from add import add

class TestAdd(unittest.TestCase):
    def test_first_and_last_elements(self):
        result = add([10, 20, 30, 40], 50)
        self.assertIn(result, ([0, 3], [3, 0]))

    def test_middle_elements(self):
        result = add([3, 2, 4], 6)
        self.assertIn(result, ([1, 2], [2, 1]))

    def test_multiple_valid_pairs(self):
        result = add([1, 2, 3, 4, 5], 5)
        self.assertIn(result, ([0, 3], [3, 0], [1, 2], [2, 1]))

    def test_positive_and_negative(self):
        result = add([-10, -20, 5, 15], -5)
        self.assertIn(result, ([0, 2], [2, 0]))

    def test_negative_all(self):
        result = add([-5, -2, -8, -3], -10)
        self.assertIn(result, ([1, 2], [2, 1]))

    def test_large_array(self):
        nums = [1] * 500 + [100]
        result = add(nums, 101)
        self.assertIsNotNone(result)
        idx1, idx2 = result
        self.assertEqual(nums[idx1] + nums[idx2], 101)
        self.assertNotEqual(idx1, idx2)
	
    def test_negative(self):
        result = add([-1, -2, -3], 0)
        self.assertIsNone(result)
	
    def test_single_and_empty(self):
        self.assertIsNone(add([], 0))
        self.assertIsNone(add([1], 1))
        self.assertIsNone(add([0], 0))

if __name__ == "__main__":
    unittest.main()