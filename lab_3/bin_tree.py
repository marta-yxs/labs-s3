def gen_bin_tree(height=6, root=9,
                 left_leaf=lambda x: x * 2 + 1,
                 right_leaf=lambda x: 2 * x - 1):
    """
    Рекурсивно построить бинарное дерево.

    Вернуть словарь с ключами 'value', 'left', 'right'.
    """
    if height <= 0:
        return None
    return {
        'value': root,
        'left': gen_bin_tree(height - 1, left_leaf(root), left_leaf, right_leaf),
        'right': gen_bin_tree(height - 1, right_leaf(root), left_leaf, right_leaf)
    }