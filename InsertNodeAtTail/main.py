#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        print(node.data)
        node = node.next
        if node:
            fptr.write(sep)


# Complete the insertNodeAtTail function below.
def insertNodeAtTail(head, data):
    if head is None:
        return SinglyLinkedListNode(data)
    last = head
    while last.next is not None:
        last = last.next
    last.next = SinglyLinkedListNode(data)
    return head

if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist.head = insertNodeAtTail(llist.head, llist_item)
        # x = llist.head
        # llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
