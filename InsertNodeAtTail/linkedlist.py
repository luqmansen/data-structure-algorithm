class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if self.start_node == None:
            print ("List has no element")
            return
        else:
            n = self.start_node
            while n != None:
                print(n.item, " ")
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node


    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node != None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref != None:
            n = n.ref
        n.ref = new_node

    def insert_after_item(self, x, data):

        n = self.start_node
        print(n.ref)
        while n != None:
            if n.item == x:
                break
            n = n.ref
        if n == None:
            print("item is not in list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_before_item(self, x, data):
        if self.start_node == None:
            print("item is not in list")
            return

        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print (n.ref)
        while n.ref != None:
            if n.rer.item == x:
                break
            n = n.ref

        if n.ref == None:
            print("item is not in list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


nll = LinkedList()

nll.insert_at_start(5)
nll.insert_at_start(10)
nll.insert_at_start(15)
nll.insert_at_end(49)
nll.insert_after_item(69,12)
nll.insert_at_start(20)


nll.traverse_list()