class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_ll(head: Node):
    if head is None:
        print(-1)

    curr = head

    while curr is not None:
        print(curr.val)
        curr = curr.next


def print_ll_recursive(head: Node):
    if head is None:
        return

    print(head.val)
    print_ll_recursive(head.next)


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    print_ll_recursive(a)
