import typing


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linkedlist_value(head: Node):
    val = []

    curr = head
    while curr is not None:
        val.append(curr.val)
        curr = curr.next

    print(val)


# A -> B -> C -> D -> None

def linkedlist_value_recur(head: Node, val_list: typing.List) -> typing.List:
    if head is None:
        return val_list

    val_list.append(head.val)
    val_list + linkedlist_value_recur(head.next, val_list)

    return val_list


if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # linkedlist_value(a)
    print(linkedlist_value_recur(a, []))
