class Node(object):

    def __init__(self, value):
        self.info = value
        self.link = None

class HeaderLinkedList(object):

    def __init__(self):
        self.head = Node(0)
    
    def display_list(self):
        if self.head.link == None:
            print("List is empty")
        
        p = self.head.link
        print("List is : ")
        while p is not None:
            print(p.info, " ", end='')
            p = p.link
        print()
    
    def insert_at_end(self,data):
        temp = Node(data)

        p = self.head
        while p.link is not None:
            p = p.link 
        p.link = temp
    
    def insert_before(self, data, x):
        #! Find reference to predecessor of node containing x
        p = self.head
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            print(f"{x} not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def delete_first_node(self):
        p = self.head
        if p.link is None:
            return p
        p.link = p.link.link
    
    def delete_last_node(self):
        p = self.head
        if p.link is None:
            return p
        while p.link.link is not None:
            p = p.link
        p.link = None
    
    def delete_node(self, data):
        p = self.head
        while p.link is not None:
            if p.link.info == data:
                break
            p = p.link
        if p.link is None:
            print(f"{data} is not found in the list")
        else:
            p.link = p.link.link



llist = HeaderLinkedList()
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_end(3)
llist.insert_at_end(4)
llist.insert_at_end(5)
# llist.delete_last_node()
llist.delete_node(3)
llist.display_list()