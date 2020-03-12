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

    def remove(self, key):
        """
        Basically we have to tackle two cases :
        1. The node is head
        2. The node is not head
        """
        if self.head.data == key:
            p = self.head
            while p.next != self.head:
                p = p.next
            p.next = self.head.next
            self.head = self.head.next

        else:
            p = self.head
            prev = None
            while p.next != self.head:
                prev = p
                p = p.next
                if p.data == key:
                    prev.next = p.next
                    p = p.next

    def __len__(self):
        # We are overriding the inbuilt len function to give us length of our linked list.
        p = self.head
        count = 0
        while p:
            count += 1
            p = p.next
            if p == self.head:
                break
        return count

    def split_list(self):
        length = len(self)

        if length == 0:
            return None

        if length == 0:
            return self.head

        mid = length//2
        count = 0

        p = self.head
        prev = None

        while p is not None and count < mid:
            count += 1
            prev = p
            p = p.next
        prev.next = self.head

        split_cllist = CircularLinkedList()
        while p.next != self.head:
            split_cllist.append(p.data)
            p = p.next
        split_cllist.append(p.data)

        self.print_list()
        print("\n")
        split_cllist.print_list()


cllist = CircularLinkedList()
cllist.append(6)
cllist.append(7)
cllist.append(8)
cllist.append(9)
cllist.append(10)
cllist.prepend(5)
cllist.prepend(4)
cllist.prepend(3)
cllist.prepend(2)
cllist.prepend(1)
# cllist.remove(10)
# cllist.remove(1)
# cllist.remove(2)
# cllist.remove(3)
# cllist.remove(4)
# cllist.remove(5)
# print(f"Length of linked list is : {len(cllist)}")
# cllist.print_list()
cllist.split_list()
