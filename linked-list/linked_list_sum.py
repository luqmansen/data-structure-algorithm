class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def ll_sum(head: Node) -> int:
    sumval = 0

    curr = head
    while curr is not None:
        sumval += curr.val
        curr = curr.next

    return sumval


def ll_sum_recursive(head: Node) -> int:
    if head is None:
        return 0

    return head.val + ll_sum(head.next)


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(5)

    a.next = b
    b.next = c
    c.next = d

    # print(ll_sum(a))
    print(ll_sum_recursive(a))
