# Лабораторная работа 2

## Условие задачи
Написать рекурсивную функцию, которая строит бинарное дерево. Функция должна принимать параметры height, root, left\_leaf и right\_leaf. Если значения переданы пользователем — используются они, иначе — значения по умолчанию из варианта.

## Решение
```
def gen_bin_tree(height=6, root=9,
                 left_leaf=lambda x: x * 2 + 1,
                 right_leaf=lambda x: 2 * x - 1):
    """
    Рекурсивно строит бинарное дерево.

    Возвращает словарь с ключами 'value', 'left', 'right'.
    """
    if height <= 0:
        return None
    return {
        'value': root,
        'left': gen_bin_tree(height - 1, left_leaf(root), left_leaf, right_leaf),
        'right': gen_bin_tree(height - 1, right_leaf(root), left_leaf, right_leaf)
    }

```
