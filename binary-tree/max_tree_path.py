import math


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __str__(self):
        return self.val


def max_tree_path(node: Node) -> int:
    if node is None:
        return -math.inf

    maxleftright = max(max_tree_path(node.right), max_tree_path(node.left))

    if maxleftright != -math.inf:
        return node.val + maxleftright
    return node.val


if __name__ == '__main__':
    """
            2
          /  \
          4  5
        /  \
        1  9
    """
    a = Node(2)
    b = Node(4)
    c = Node(5)
    d = Node(1)
    e = Node(9)

    a.right = c
    a.left = b
    b.left = d
    b.right = e

    print(max_tree_path(a))
