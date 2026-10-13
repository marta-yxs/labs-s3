\# Условие задачи



Написать рекурсивную функцию, которая строит бинарное дерево. Функция должна принимать параметры height, root, left\_leaf и right\_leaf. Если значения переданы пользователем — используются они, иначе — значения по умолчанию из варианта.



\# Решение



```python

def gen\_bin\_tree(height=6, root=9,

&#x20;                left\_leaf=lambda x: x \* 2 + 1,

&#x20;                right\_leaf=lambda x: 2 \* x - 1):

&#x20;   if height <= 0:

&#x20;       return None

&#x20;   return {

&#x20;       'value': root,

&#x20;       'left': gen\_bin\_tree(height - 1, left\_leaf(root), left\_leaf, right\_leaf),

&#x20;       'right': gen\_bin\_tree(height - 1, right\_leaf(root), left\_leaf, right\_leaf)

&#x20;   }

```

