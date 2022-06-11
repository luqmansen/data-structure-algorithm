class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def tree_sum_dfs_iter(root: Node) -> int:
    if root is None:
        return 0

    treesum = 0
    stack = [root]

    while len(stack) > 0:
        curr = stack.pop()
        treesum += curr.val

        if curr.left is not None:
            stack.append(curr.left)
        if curr.right is not None:
            stack.append(curr.right)

    return treesum


"""
        A
      /  \
      B  C
    /  \
    D  E
"""


def tree_sum_dfs_recursive(root: Node) -> bool:
    if root is None:
        return 0

    cnt = root.val
    cnt += tree_sum_dfs_recursive(root.left)
    cnt += tree_sum_dfs_recursive(root.right)

    return cnt


def tree_sum_bfs(root: Node) -> int:
    if root is None:
        return 0

    import queue
    queue = queue.Queue()
    queue.put(root)
    cnt = 0
    while queue.empty() is False:
        curr = queue.get()
        cnt += curr.val
        if curr.left is not None:
            queue.put(curr.left)
        if curr.right is not None:
            queue.put(curr.right)

    return cnt


if __name__ == '__main__':
    a = Node(2)
    b = Node(2)
    c = Node(1)
    d = Node(2)
    e = Node(4)

    a.right = c
    a.left = b
    b.left = d
    b.right = e

    # print(tree_sum_dfs_iter(root=a))
    # print(tree_sum_dfs_recursive(root=a))
    print(tree_sum_bfs(root=a   ))
