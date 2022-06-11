class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __str__(self):
        return self.val


def dfs_iter(root: Node):
    stack = [root]

    while len(stack) > 0:
        curr = stack.pop()
        print(curr)

        if curr.right is not None:
            stack.append(curr.right)

        if curr.left is not None:
            stack.append(curr.left)


from queue import Queue


def bfs(root: Node):
    queue = Queue()
    queue.put(root)

    while queue.empty() is False:
        curr = queue.get()
        print(curr.val)

        if curr.left is not None:
            queue.put(curr.left)
        if curr.right is not None:
            queue.put(curr.right)


def dfs_recursive(root: Node):
    if root is None:
        return

    print(root.val)
    if root.left is not None:
        dfs_recursive(root.left)
    if root.right is not None:
        dfs_recursive(root.right)


"""
        A
      /  \
      B  C
    /  \
    D  E
"""

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

    # dfs_iter(a)
    # dfs_recursive(a)
    bfs(root=a)
