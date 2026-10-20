# Лабораторная работа 4



## Условие задачи

Написать на языке Python нерекурсивную функцию gen\_bin\_tree, которая будет строить бинарное дерево.
Алгоритм построения дерева должен учитывать параметры height, root, left\_leaf и right\_leaf, переданные в качестве аргументов функции.
Если для указанных параметров были переданы значения, то используются они.
В противном случае должны использоваться значения, указанные в варианте.
Базовый вариант решения задачи должен представлять результат в виде словаря с ключами value, left, right.

## Решение

Построение бинарного дерева нерекурсивным методом обхода в ширину, с помощью очереди. При высоте, равной нулю, возвращается None.

```
def gen_bin_tree(height=5, root=10,
                 left_leaf=lambda x: x * 3 + 1,
                 right_leaf=lambda x: 3 * x - 1):
    """
    Строит бинарное дерево методом обхода в ширину.

    Возвращает словарь с ключами value, left, right с описанием структуры дерева, или None, если высота меньше или равна нулю.
    """
    if height <= 0:
        return None

    tree = {'value': root, 'left': None, 'right': None}
    queue = deque([tree])
    current_height = 1

    while current_height < height:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            
            left_val = left_leaf(node['value'])
            right_val = right_leaf(node['value'])
            
            left_node = {'value': left_val, 'left': None, 'right': None}
            right_node = {'value': right_val, 'left': None, 'right': None}
            
            node['left'] = left_node
            node['right'] = right_node
            
            queue.append(left_node)
            queue.append(right_node)
            
        current_height += 1

    return tree
```
