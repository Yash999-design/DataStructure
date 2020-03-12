class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None

    def prepend(self, data):

        new_node = Node(data)
        p = self.head
        new_node.next = self.head

        if p is None:
            new_node.next = new_node

        else:
            while p.next != self.head:
                p = p.next
            p.next = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            p = self.head
            while p.next != self.head:
                p = p.next
            p.next = new_node
            new_node.next = self.head

    def print_list(self):
        p = self.head

        while p is not None:
            #! This condition is non terminating.
            print(p.data)
            p = p.next
            if p == self.head:
                break
                #! This is the loop breaking condition 

cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)
cllist.append(5)
cllist.prepend(6)
cllist.prepend(7)
cllist.prepend(8)
cllist.prepend(9)
cllist.prepend(10)
cllist.print_list()
