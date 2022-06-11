class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def tree_includes_dfs_iter(root: Node, target: str) -> bool:
    if root is None:
        return False
    if root.val == target:
        return True

    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        if curr.val == target:
            return True

        if curr.left is not None:
            stack.append(curr.left)
        if curr.right is not None:
            stack.append(curr.right)

    return False


"""
        A
      /  \
      B  C
    /  \
    D  E
"""
def tree_includes_dfs_recursive(root: Node, target: str) -> bool:
    if root is None:
        return False
    if root.val == target:
        return True

    return tree_includes_dfs_recursive(root.left, target) or tree_includes_dfs_recursive(root.right, target)


def tree_includes_bfs(root: Node, val: str) -> bool:
    if root is None:
        return False
    if root.val == val:
        return True

    import queue
    queue = queue.Queue()
    queue.put(root)
    while queue.empty() is False:
        curr = queue.get()
        if curr.val == val:
            return True

        if curr.left is not None:
            queue.put(curr.left)
        if curr.right is not None:
            queue.put(curr.right)

    return False


if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")

    a.right = c
    a.left = b
    b.left = d
    b.right = e

    # print(tree_includes_dfs_iter(root=a, val="e"))
    # print(tree_includes_dfs_iter(root=a, val="e"))
    # print(tree_includes_bfs(root=a, val="c"))
    # print(tree_includes_bfs(root=a, val="L"))
    print(tree_includes_dfs_recursive(root=a, target="c"))
    print(tree_includes_dfs_recursive(root=a, target="L"))
