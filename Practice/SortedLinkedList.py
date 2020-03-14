class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SortedLinkedList:

    def __init__(self):

        self.start = None

    def show_list(self):

        if self.start is None:
            print("List is empty")
            return
        
        print("List is : ")
        p = self.start
        while p is not None:
            print(p.data, " ", end='')
            p = p.next
        print()
    
    def insert_in_order(self, value):
        new_node = Node(value)

        if self.start is None or self.start.data > value:
            new_node.next = self.start
            self.start = new_node
        
        else:
            p = self.start
            while p.next is not None and p.next.data <= value:
                p = p.next
            
            new_node.next = p.next
            p.next = new_node

llist = SortedLinkedList()

llist.insert_in_order(5)
llist.insert_in_order(25)
llist.insert_in_order(15)
llist.insert_in_order(35)
llist.insert_in_order(20)
llist.insert_in_order(50)
llist.insert_in_order(45)
llist.insert_in_order(65)
llist.insert_in_order(55)
llist.insert_in_order(10)
llist.show_list()