class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None

    def prepend(self, data):
        
        new_node = Node(data)
        new_node.next = self.head

        p = self.head

        if p.next == self.head:
            p.next = new_node
        
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

        if self.head is None:
            print("List is empty")

        elif self.head.next == self.head:  # ! If list has only one value
            print(self.head.data)

        else:  # ! If list has more than one values
            p = self.head
            while p.next != self.head:
                print(p.data)
                p = p.next
            print(p.data)

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