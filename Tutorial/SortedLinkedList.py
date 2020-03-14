class Node(object):

    def __init__(self, value):
        self.info = value
        self.link = None


class SortedLinkedList(object):

    def __init__(self):
        self.start = None

    def insert_in_order(self, data):
        temp = Node(data)

        #! List is empty or node to be inserted before first node
        if self.start == None or data < self.start.info:
            temp.link = self.start
            self.start = temp
            return

        p = self.start
        while p.link is not None and p.link.info <= data:
            p = p.link
        temp.link = p.link
        p.link = temp

    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        print("List is : ")
        p = self.start

        while p is not None:
            print(p.info, " ", end='')
            p = p.link
        print()


list = SortedLinkedList()
list.insert_in_order(10)
list.insert_in_order(35)
list.insert_in_order(20)
list.insert_in_order(5)
list.insert_in_order(25)
list.insert_in_order(45)
list.insert_in_order(30)
list.insert_in_order(50)
list.insert_in_order(40)
list.insert_in_order(15)
list.display_list()
