import unittest
from memoization import (
    gen_bin_tree_recursive,
    gen_bin_tree_recursive_memo,
    gen_bin_tree_iterative
)

class GenBinTreeTestCase(unittest.TestCase):
    def test_zero_height(self):
        self.assertEqual(gen_bin_tree_recursive(0, 5), {'value': 5, 'left': None, 'right': None})

    def test__negative_height(self):
        self.assertIsNone(gen_bin_tree_recursive(-1, 5))

    def test_single_level(self):
        expected = {
            'value': 8,
            'left': {'value': 17, 'left': None, 'right': None},
            'right': {'value': 15, 'left': None, 'right': None}
        }
        self.assertEqual(gen_bin_tree_recursive(1, 8), expected)


    def test_cache_efficiency(self):
        gen_bin_tree_recursive_memo.cache_clear()
        gen_bin_tree_recursive_memo(2, 10)
        self.assertIn("misses=7", gen_bin_tree_recursive_memo.cache_info())
        gen_bin_tree_recursive_memo(2, 10)
        self.assertIn("hits=1", gen_bin_tree_recursive_memo.cache_info())

    def test_share_memory(self):
        left13 = lambda x: x + 1
        right13 = lambda x: x - 1
        
        gen_bin_tree_recursive_memo.cache_clear()
        tree = gen_bin_tree_recursive_memo(3, 10, left13, right13)
        
        node_lr = tree['left']['right']
        node_rl = tree['right']['left']
        
        self.assertTrue(node_lr is node_rl)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
