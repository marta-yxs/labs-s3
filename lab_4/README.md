\# Лабораторная работа 4



\## Условие задачи

Написать на языке Python нерекурсивную функцию gen\_bin\_tree, которая будет строить бинарное дерево.

Алгоритм построения дерева должен учитывать параметры height, root, left\_leaf и right\_leaf, переданные в качестве аргументов функции.

Если для указанных параметров были переданы значения, то используются они.

В противном случае должны использоваться значения, указанные в варианте.

Базовый вариант решения задачи должен представлять результат в виде словаря с ключами value, left, right.



\## Решение

Построение бинарного дерева нерекурсивным методом обхода в ширину, с помощью очереди. При нулевой высоте возвращается None.



```

from collections import deque



def gen\_bin\_tree(height=5, root=10,

&#x20;                left\_leaf=lambda x: x \* 3 + 1,

&#x20;                right\_leaf=lambda x: 3 \* x - 1):

&#x20;   """

&#x20;   Строит бинарное дерево методом обхода в ширину.



&#x20;   Возвращает словарь с ключами value, left, right с описанием структуры дерева, или None, если высота меньше или равна нулю.

&#x20;   """

&#x20;   if height <= 0:

&#x20;       return None



&#x20;   tree = {'value': root, 'left': None, 'right': None}

&#x20;   queue = deque(\[tree])

&#x20;   current\_height = 1



&#x20;   while current\_height < height:

&#x20;       level\_size = len(queue)

&#x20;       for \_ in range(level\_size):

&#x20;           node = queue.popleft()

&#x20;           

&#x20;           left\_val = left\_leaf(node\['value'])

&#x20;           right\_val = right\_leaf(node\['value'])

&#x20;           

&#x20;           left\_node = {'value': left\_val, 'left': None, 'right': None}

&#x20;           right\_node = {'value': right\_val, 'left': None, 'right': None}

&#x20;           

&#x20;           node\['left'] = left\_node

&#x20;           node\['right'] = right\_node

&#x20;           

&#x20;           queue.append(left\_node)

&#x20;           queue.append(right\_node)

&#x20;           

&#x20;       current\_height += 1



&#x20;   return tree

```

