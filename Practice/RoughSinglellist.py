class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList:
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
                print(p.info, " ", end="")
                p = p.link
            print()

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print("Number of nodes in the list = ", n)

    def search(self, x):
        p = self.start
        position = 1
        while p is not None:
            if p.info == position:
                print(f"Item {x} found at ", position)
                return True
            p = p.link
            position += 1
        else:
            print(f"Item {x} not found in the list")
            return False

    def insert_in_begining(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        else:
            p = self.start
            while p.link is not None:
                p = p.link
            p.link = temp
    
    def concatenate_list(self, list2):
        p = self.start
        q = list2.start

        if p is None:
            p = q
            return
        
        if q is None:
            return
        
        while p.link is not None:
            p = p.link
        p.link = q
        



list1 = SingleLinkedList()
list2 = SingleLinkedList()
list1.insert_at_end(1)
list1.insert_at_end(2)
list1.insert_at_end(3)
list1.insert_at_end(4)
list1.insert_at_end(5)
list2.insert_at_end(6)
list2.insert_at_end(7)
list2.insert_at_end(8)
list2.insert_at_end(9)
list2.insert_at_end(10)
list1.concatenate_list(list2)
list1.display_list()
list2.display_list()
