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

    def remove(self, key):
        # p = self.head
        # prev = None

        # if self.head is None:
        #     return

        # # ! delete only node from the circular linked list if it matches the key.
        # elif p.next == self.head:
        #     if p.data == key:
        #         self.head = None
        #     else:
        #         print(f"{key} is not found")
        
        # #! delete first node from the non-empty list.
        # # if self.head.data == key:
        # #     self.head = self.head.next
        
        # # while p.next != self.head:
        # #     p = p.next
        # # p.next = p.next.next

        # while p.next != self.head:  # ! delete any node from the non empty circular linked list
        #     prev = p
        #     p = p.next
        #     if p.data == key:
        #         break

        # if p.data == key:  # ! If loop terminates because of key found in the circular linked list.
        #     prev.next = p.next
        # else:
        #     print(f"{key} is not found")

        # #! delete last node from the non-empty circular linked list
        # while p.next != self.head:
        #     p = p.next
        #     prev = p
        # if p.data == key:
        #     prev.next = p.next
        # else:
        #     print("Key is not found in the list.")
        

        """
        We have to take care for two cases 
        1. when the key is head node
        2. when the key is not head node
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
        """We are overriding the inbuilt len function so that it gives us the length of our circular linked list"""
        p = self.head
        count = 0
        while p:
            count += 1
            p = p.next
            if p == self.head:
                break
        return count
    
    def split_list(self):
        """We need the len function. Because we will split our list from the mid so we need the mid point of the list."""

        if len(self) == 0:
            return None
        
        if len(self) == 1:
            return self.head
        
        p = self.head
        prev = None

        count = 0
        mid_point = len(self)//2

        while p is not None and count < mid_point:
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
# cllist.remove(1)
# cllist.remove(10)
cllist.split_list()
# cllist.print_list()
