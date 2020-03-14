class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList(object):

    def __init__(self):
        self.start = None
    
    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        
        else:
            print("List is : ")
            p = self.start
            while p is not None:
                print(p.data, " ", end='')
                p = p.next
            print()
    
    def insert_in_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.start
        self.start.prev = new_node
        # new_node.prev = None
        self.start = new_node
    
    def insert_in_empty_list(self, data):
        new_node = Node(data)
        # new_node.next = self.start
        self.start = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        p = self.start
        if p is None:
            self.start = new_node
        
        else:
            while p.next is not None:
                p = p.next
            p.next = new_node
            # new_node.next = None
            new_node.prev = p
    
    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        if n == 0:
            return
        data = int(input("Enter the first element to be inserted : "))
        self.insert_in_empty_list(data)

        for i in range(n-1):
            data = int(input("Enter the next element to be inserted : "))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        new_node = Node(data)
        p = self.start

        while p is not None:
            if p.data == x:
                break
            p = p.next
        
        if p is None:
            print(x, " not found in the list")
        
        else:
            new_node.next = p.next
            new_node.prev = p
            if p.next is not None:
                p.next.prev = new_node
            p.next = new_node
    
    def insert_before(self, data, x):
        new_node = Node(data)
        
        if self.start is None:
            print("List is empty")
            return
        
        if self.start.info == x:
            new_node.next = self.start
            self.start.prev = new_node
            self.start = new_node
            return

        p = self.start

        while p is not None:
            if p.data == x:
                break
            p = p.next
        if p is None:
            print(x, " not present in the list")
        else:
            new_node.prev = p.prev
            new_node.next = p
            p.prev.next = new_node
            p.prev = new_node
    
    def delete_first_node(self):

        if self.start is None:
            print("List is empty")
            return
        
        if self.start.next is None:
            self.start = None
            return
        
        self.start = self.start.next
        self.start.prev = None
    
    def delete_last_node(self):

        if self.start is None:
            print("List is empty")
            return
        
        if self.start.next is None:
            self.start = None
            # self.start.prev = None
        
        p = self.start
        
        while p.next is not None:
            p = p.next
        
        p.prev.next = None

    def delete_node(self, x):

        if self.start is None:
            print("List is Empty")
            return

        if self.start.next is None:
            if self.start.data == x:
                self.start = None
            else:
                print(x, "not found")
            return

        #! Deletion of first node
        if self.start.data == x:
            self.start = self.start.next
            self.start.prev = None
            return 

        p = self.start.next
        while p.next is not None:
            if p.data == x:
                break
            p = p.next
        
        #! node to be deleted is in between
        if p.next is not None:
            p.prev.next = p.next
            p.next.prev = p.prev
        
        else: #! p refers to last node
            #! node to be deleted is last node
            if p.data == x:
                p.prev.next = None
            else:
                print(x, " not found")

    def reverse_list(self):
        if self.start is None:
            return

        p1 = self.start
        p2 = p1.next
        p1.next = None
        p1.prev = p2

        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev

        self.start = p1

list = DoubleLinkedList()
list.create_list()

while True:
    print("1. Display list")
    print("2. Insert in empty list")
    print("3. Insert a node in the beginning of the list")
    print("4. Insert a node at the end of the list")
    print("5. Insert a node after a specified node")
    print("6. Insert a node before a specified node")
    print("7. Delete first node")
    print("8. Delete last node")
    print("9. Delete any node")
    print("10. Reverse the list")
    print("11. Quit")

    option = int(input("Enter your choice : "))

    if option == 1:
        list.display_list()

    elif option == 2:
        data = int(input("Enter the element to be inserted : "))
        list.insert_in_empty_list(data)

    elif option == 3:
        data = int(input("Enter the element to be inserted : "))
        list.insert_in_beginning(data)

    elif option == 4:
        data = int(input("Enter the element to inserted : "))
        list.insert_at_end(data)

    elif option == 5:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the element after which to insert : "))
        list.insert_after(data, x)

    elif option == 6:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the element before which to insert : "))
        list.insert_before(data, x)

    elif option == 7:
        list.delete_first_node()

    elif option == 8:
        list.delete_last_node()

    elif option == 9:
        data = int(input("Enter the element to be deleted : "))
        list.delete_node(data)

    elif option == 10:
        list.reverse_list()

    elif option == 11:
        break

    else:
        print("Wrong option")

    print()
