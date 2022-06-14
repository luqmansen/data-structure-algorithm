class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return self.val


def print_ll(head: Node):
    if head is None:
        return
    print(head.val, end="\n")
    print_ll(head.next)


def reverse_ll_rec(head: Node, prev=None) -> Node:
    if head is None:
        return prev
    _next = head.next
    head.next = prev
    return reverse_ll_rec(_next, head)


# Null <- A   B -> C -> D -> None
#   prev  cur  next
def reverse_ll(head: Node) -> Node:
    prev = None
    curr = head
    while curr is not None:
        _next = curr.next
        curr.next = prev
        prev = curr
        curr = _next

    return prev


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # print_ll(reverse_ll(a))
    print_ll(reverse_ll_rec(a))
    # print_ll(reverse_ll(a))
