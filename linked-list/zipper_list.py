class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return self.val


"""
 A -> B -> C -> D
 1 -> 2 -> 3 -> 4
 
 A - 1 - B - 2 - C - 3 D   
 - 4
 
 A -> B -> C -> D
 1 -> 2 
 
 A -> B
 1 -> 2 -> 3 -> 4
"""


def zipper_list(list_a: Node, list_b: Node) -> Node:
    counter = 0
    curr_a = list_a
    curr_b = list_b

    while curr_a is not None and curr_b is not None:
        if counter % 2 == 0:
            _next = curr_a.next
            curr_a.next = curr_b
            curr_a = _next
            counter += 1
            continue

        if counter % 2 == 1:
            _next = curr_b.next
            curr_b.next = curr_a
            curr_b = _next
            counter += 1
            continue


    return list_a


def print_ll(head: Node):
    curr = head
    while curr is not None:
        print(curr)
        curr = curr.next


def dump_ll(head: Node) -> str:
    result = []
    curr = head
    while curr is not None:
        result.append(curr.val)
        curr = curr.next

    return "".join(result)

if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    a1 = Node("1")
    a2 = Node("2")
    a3 = Node("3")
    a4 = Node("4")

    a1.next = a2
    a2.next = a3
    a3.next = a4

    print_ll(zipper_list(a, a1))
