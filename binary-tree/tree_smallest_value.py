import math
from typing import Union, Any


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def smallest_value_dfs(node: Node) -> int:
    if node is None:
        return math.inf

    min_val = min(node.val, smallest_value_dfs(node.left), smallest_value_dfs(node.right))

    return min_val


def smallest_value_bfs(root: Node) -> Union[Union[float], Any]:
    if root is None:
        return math.inf
    import queue
    queue = queue.Queue()

    queue.put(root)
    minval = root.val
    while queue.empty() is False:
        curr = queue.get()
        minval = min(minval, curr.val)

        queue.put(curr.left) if curr.left is not None else None
        queue.put(curr.right) if curr.right is not None else None

    return minval


if __name__ == '__main__':
    a = Node(100)
    b = Node(2)
    c = Node(1)
    d = Node(5)
    e = Node(7)

    a.right = c
    a.left = b
    b.left = d
    b.right = e

    # print(tree_sum_dfs_iter(root=a))
    # print(tree_sum_dfs_recursive(root=a))
    # print(smallest_value_dfs(node=a))
    print(smallest_value_bfs(root=a))
