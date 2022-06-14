from unittest import TestCase
from zipper_list import zipper_list, Node, dump_ll


class Test(TestCase):
    def test_zipper_list_same_length(self):
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

        self.assertEqual("a1b2c3d4", dump_ll(zipper_list(a, a1)))

    def test_zipper_list_a_lengthier(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        a1 = Node("1")
        a2 = Node("2")

        a1.next = a2

        self.assertEqual("a1b2cd", dump_ll(zipper_list(a, a1)))

    def test_zipper_list_b_lengthier(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        a1 = Node("1")
        a2 = Node("2")

        a1.next = a2

        self.assertEqual("1a2bcd", dump_ll(zipper_list(a1, a)))
