import unittest
from bin_tree import gen_bin_tree
class TestGenBinTree(unittest.TestCase):
    def test_two_numbers(self):
        """Проверяет значения левого и правого потомков."""
        tree = gen_bin_tree(1, 8)
        self.assertEqual(tree["left"]["value"], 12)
        self.assertEqual(tree["right"]["value"], 64)

    def test_zero_height(self):
        """Проверяет, что при высоте 0 функция возвращает None."""
        self.assertEqual(gen_bin_tree(0, 5), None)

    def test_default_root(self):
        """Проверяет построение дерева с высотой 1."""
        tree = gen_bin_tree(1)
        self.assertEqual(tree["value"], 9)
        self.assertEqual(tree["left"]["value"], 19)
        self.assertEqual(tree["right"]["value"], 17)