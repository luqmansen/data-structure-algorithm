import typing


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def ll_find(head: Node, target: str) -> bool:
    if head.val == target:
        return True

    curr = head
    while curr is not None:
        if curr.val == target:
            return True
        curr = curr.next

    return False


# A -> B -> C -> D -> None

def ll_find_recursive(head: Node, target: str) -> bool:
    if head is None:
        return False
    if head.val == target:
        return True

    return ll_find_recursive(head.next, target)


if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # print(ll_find(a, "d"))
    # print(ll_find(a, "F"))
    # print(ll_find_recursive(a, "d"))
    print(ll_find_recursive(a, "F"))
