import functools
import timeit
import matplotlib.pyplot as plt
from collections import deque
from typing import Callable, Optional, Dict, Any, Tuple, Set, List

TreeNode = Dict[str, Any]
LeafFunc = Callable[[int], int]


def gen_bin_tree_recursive(
    height: int = 6, 
    root: int = 9,
    left_leaf: LeafFunc = lambda x: x * 2 + 1,
    right_leaf: LeafFunc = lambda x: 2 * x - 1
) -> Optional[TreeNode]:
    """
    Рекурсивно строит бинарное дерево.

    height (int): Количество ребер от корня до листьев. Если 0, возвращается только корень. Если < 0, возвращается None.
    root (int): Значение корневого узла.
    left_leaf (LeafFunc): Функция вычисления значения левого потомка.
    right_leaf (LeafFunc): Функция вычисления значения правого потомка.
    Словарь с ключами value, left, right или None, если высота < 0.
    """
    if height < 0:
        return None
    
    node: TreeNode = {'value': root, 'left': None, 'right': None}
    
    if height > 0:
        node['left'] = gen_bin_tree_recursive(height - 1, left_leaf(root), left_leaf, right_leaf)
        node['right'] = gen_bin_tree_recursive(height - 1, right_leaf(root), left_leaf, right_leaf)
        
    return node


def gen_bin_tree_iterative(
    height: int = 6, 
    root: int = 9,
    left_leaf: LeafFunc = lambda x: x * 2 + 1,
    right_leaf: LeafFunc = lambda x: 2 * x - 1
) -> Optional[TreeNode]:
    """
    Нерекурсивно (методом BFS) строит бинарное дерево.

    height (int): Количество ребер от корня до листьев.
    root (int): Значение корневого узла.
    left_leaf (LeafFunc): Функция вычисления левого потомка.
    right_leaf (LeafFunc): Функция вычисления правого потомка.
    Корневой узел дерева или None, если высота < 0.
    """
    if height < 0:
        return None

    tree: TreeNode = {'value': root, 'left': None, 'right': None}
    queue: deque = deque([(tree, height)])

    while queue:
        node, h = queue.popleft()
        
        if h > 0:
            left_val = left_leaf(node['value'])
            right_val = right_leaf(node['value'])
            
            left_node = {'value': left_val, 'left': None, 'right': None}
            right_node = {'value': right_val, 'left': None, 'right': None}
            
            node['left'] = left_node
            node['right'] = right_node
            
            queue.append((left_node, h - 1))
            queue.append((right_node, h - 1))
            
    return tree

def memoize(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор для кэширования результатов функции.

    Args:
        func (Callable): Функция для кэширования.

    Returns:
        Callable: Обёрнутая функция с методами cache_clear и cache_info.
    """
    cache: Dict[Tuple[Any, ...], Any] = {}
    hits: int = 0
    misses: int = 0

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        nonlocal hits, misses
        key = (args, tuple(sorted(kwargs.items())))
        
        if key in cache:
            hits += 1
            return cache[key]
        
        misses += 1
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    def cache_clear() -> None:
        """Очищает кэш и сбрасывает статистику."""
        nonlocal hits, misses
        cache.clear()
        hits = 0
        misses = 0

    def cache_info() -> str:
        """Возвращает статистику попаданий и промахов."""
        return f"CacheInfo(hits={hits}, misses={misses})"

    setattr(wrapper, 'cache_clear', cache_clear)
    setattr(wrapper, 'cache_info', cache_info)
    return wrapper

@memoize
def gen_bin_tree_recursive_memo(
    height: int = 6, 
    root: int = 9,
    left_leaf: LeafFunc = lambda x: x * 2 + 1,
    right_leaf: LeafFunc = lambda x: 2 * x - 1
) -> Optional[TreeNode]:
    """
    Рекурсивная функция с кэшированием через декоратор @memoize.

    Args:
        height (int): Количество ребер от корня до листьев.
        root (int): Значение корневого узла.
        left_leaf (LeafFunc): Функция левого потомка.
        right_leaf (LeafFunc): Функция правого потомка.

    Returns:
        Optional[TreeNode]: Корневой узел дерева.
    """
    if height < 0: 
        return None
    
    node: TreeNode = {'value': root, 'left': None, 'right': None}
    
    if height > 0:
        node['left'] = gen_bin_tree_recursive_memo(height - 1, left_leaf(root), left_leaf, right_leaf)
        node['right'] = gen_bin_tree_recursive_memo(height - 1, right_leaf(root), left_leaf, right_leaf)
        
    return node


def gen_bin_tree_iterative_memo(
    height: int = 6, 
    root: int = 9,
    left_leaf: LeafFunc = lambda x: x * 2 + 1,
    right_leaf: LeafFunc = lambda x: 2 * x - 1
) -> Optional[TreeNode]:
    """
    Нерекурсивная функция с внутренним кэшем.

    Args:
        height (int): Количество ребер от корня до листьев.
        root (int): Значение корневого узла.
        left_leaf (LeafFunc): Функция левого потомка.
        right_leaf (LeafFunc): Функция правого потомка.

    Returns:
        Optional[TreeNode]: Корневой узел дерева.
    """
    if height < 0: 
        return None

    if not hasattr(gen_bin_tree_iterative_memo, "cache"):
        setattr(gen_bin_tree_iterative_memo, "cache", {})
    cache: Dict[Tuple[int, int], TreeNode] = getattr(gen_bin_tree_iterative_memo, "cache")

    if (root, height) in cache:
        return cache[(root, height)]

    expanded: Set[Tuple[int, int]] = set()
    root_node: TreeNode = {'value': root, 'left': None, 'right': None}
    cache[(root, height)] = root_node
    queue: deque = deque([(root_node, height)])

    while queue:
        node, h = queue.popleft()
        val = node['value']

        if h > 0 and (val, h) not in expanded:
            expanded.add((val, h))

            l_val = left_leaf(val)
            l_key = (l_val, h - 1)
            if l_key not in cache:
                cache[l_key] = {'value': l_val, 'left': None, 'right': None}
                queue.append((cache[l_key], h - 1))
            node['left'] = cache[l_key]

            r_val = right_leaf(val)
            r_key = (r_val, h - 1)
            if r_key not in cache:
                cache[r_key] = {'value': r_val, 'left': None, 'right': None}
                queue.append((cache[r_key], h - 1))
            node['right'] = cache[r_key]
            
    return root_node


def _iter_cache_clear() -> None:
    """Очищает кэш итеративной функции."""
    setattr(gen_bin_tree_iterative_memo, "cache", {})

setattr(gen_bin_tree_iterative_memo, "cache_clear", _iter_cache_clear)


@functools.lru_cache(maxsize=None)
def gen_bin_tree_lru(
    height: int = 6, 
    root: int = 9,
    left_leaf: LeafFunc = lambda x: x * 2 + 1,
    right_leaf: LeafFunc = lambda x: 2 * x - 1
) -> Optional[TreeNode]:
    """
    Рекурсивная функция с кэшированием через functools.lru_cache.

    Args:
        height (int): Количество ребер от корня до листьев.
        root (int): Значение корневого узла.
        left_leaf (LeafFunc): Функция левого потомка.
        right_leaf (LeafFunc): Функция правого потомка.

    Returns:
        Optional[TreeNode]: Корневой узел дерева.
    """
    if height < 0: 
        return None
        
    node: TreeNode = {'value': root, 'left': None, 'right': None}
    
    if height > 0:
        node['left'] = gen_bin_tree_lru(height - 1, left_leaf(root), left_leaf, right_leaf)
        node['right'] = gen_bin_tree_lru(height - 1, right_leaf(root), left_leaf, right_leaf)
        
    return node

class CountedLeaf:
    """Класс-обёртка для подсчета вызовов функций веток."""
    def __init__(self, func: LeafFunc) -> None:
        self.func = func
        self.count = 0
    def __call__(self, x: int) -> int:
        self.count += 1
        return self.func(x)

if __name__ == '__main__':
    root_9 = 9
    left_9 = lambda x: x * 2 + 1
    right_9 = lambda x: 2 * x - 1

    root_13 = 13
    left_13 = lambda x: x + 1
    right_13 = lambda x: x - 1

    heights = list(range(1, 13))

    times_rec = []
    times_rec_memo = []
    times_iter = []
    times_iter_memo = []
    times_lru = []

    print("Запуск замеров времени для Варианта 9...")

    for h in heights:
        gen_bin_tree_recursive_memo.cache_clear()
        gen_bin_tree_iterative_memo.cache_clear()
        gen_bin_tree_lru.cache_clear()

        t_rec = timeit.timeit(lambda: gen_bin_tree_recursive(h, root_9, left_9, right_9), number=1)
        t_rec_memo = timeit.timeit(lambda: gen_bin_tree_recursive_memo(h, root_9, left_9, right_9), number=1)
        t_iter = timeit.timeit(lambda: gen_bin_tree_iterative(h, root_9, left_9, right_9), number=1)
        t_iter_memo = timeit.timeit(lambda: gen_bin_tree_iterative_memo(h, root_9, left_9, right_9), number=1)
        t_lru = timeit.timeit(lambda: gen_bin_tree_lru(h, root_9, left_9, right_9), number=1)

        times_rec.append(t_rec)
        times_rec_memo.append(t_rec_memo)
        times_iter.append(t_iter)
        times_iter_memo.append(t_iter_memo)
        times_lru.append(t_lru)

    plt.figure(figsize=(10, 6))
    
    plt.plot(heights, times_rec, label='Рекурсия (без кэша)', marker='o', linestyle='-')
    plt.plot(heights, times_iter, label='Итеративный BFS (без кэша)', marker='x', linestyle='-')
    plt.plot(heights, times_rec_memo, label='Рекурсия + @memoize', marker='s', linestyle='--')
    plt.plot(heights, times_iter_memo, label='Итеративный BFS + кэш', marker='^', linestyle='--')
    plt.plot(heights, times_lru, label='Рекурсия + @lru_cache', marker='d', linestyle=':')

    plt.title('Сравнение скорости построения дерева (Вариант 9)')
    plt.xlabel('Высота дерева (height)')
    plt.ylabel('Время выполнения (секунды)')
    
    plt.yscale('log') 
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.5)

    plt.savefig('tree_performance_chart.png', dpi=300)
    print("График сохранен в файл 'tree_performance_chart.png'")
