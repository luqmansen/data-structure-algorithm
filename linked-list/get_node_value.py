class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def get_node_val(head: Node, target_idx: int) -> str:
    if head is None:
        return "empty head"

    curr_idx = 0
    curr = head
    while curr is not None:
        if target_idx == curr_idx:
            return curr.val
        curr_idx += 1

        curr = curr.next

    return "not found"


def get_node_val_recursive(head: Node, target_idx: int):
    if head is None:
        return "not found"

    if target_idx == 0:
        return head.val

    return get_node_val_recursive(head.next, target_idx - 1)


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    # A -> B -> C -> D -> None
    a.next = b
    b.next = c
    c.next = d

    # print(get_node_val(a, 5))
    print(get_node_val_recursive(a, 4))
