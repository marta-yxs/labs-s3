import unittest
from bin_tree import gen_bin_tree


class TestBinaryTree(unittest.TestCase):

    def test_empty_tree(self):
        """Проверяет, что возвращается лист без потомков при height=0."""
        self.assertIsNone(gen_bin_tree(height=0, root=7))

    def test_default_values(self) -> None:
        """Проверяет значения левого и правого потомков."""
        tree = gen_bin_tree(2, 10)
        self.assertEqual(tree["left"]["value"], 31)
        self.assertEqual(tree["right"]["value"], 29)

    def test_positive_numbers(self) -> None:
        """Проверяет построение дерева с числами."""
        tree = gen_bin_tree(2, 4)
        self.assertEqual(tree["left"]["value"], 13)  # 4 * 3 + 1
        self.assertEqual(tree["right"]["value"], 11)

if __name__ == "__main__":
    unittest.main(verbosity=2)