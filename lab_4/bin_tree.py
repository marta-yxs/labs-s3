from collections import deque

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

if __name__ == "__main__":
    print(gen_bin_tree(5, 10))