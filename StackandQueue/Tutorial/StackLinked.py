class EmptyStackError(Exception):
    pass

class Node:
    
    def __init__(self, value):
        self.info = value
        self.link = None
    
class Stack:

    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top == None
    
    def size(self):
        
        if self.is_empty():
            return 0
        
        count = 0
        p = self.top
        while p is not None:
            count += 1
            p = p.link
        return count
    
    def push(self, data):
        temp = Node(data)
        temp.link = self.top
        self.top = temp
    
    def pop(self):

        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        
        popped_item = self.top.info
        self.top = self.top.link
        
        return f"popped item is : {popped_item}"

    def peek(self):

        if self.is_empty():
            raise EmptyStackError("Stack is empty, thus no peek")
        print("\n")
        return f"peek of the stack is : {self.top.info}"
    
    def show_list(self):
        if self.is_empty():
            print("Stack is empty")
            return

        print("Stack is : ")
        p = self.top
        while p is not None:
            print(p.info, " ", end='')
            p = p.link
        print("\n")

myStack = Stack()

myStack.push(5)
myStack.push(10)
myStack.push(15)
myStack.push(25)
myStack.push(35)
myStack.push(45)
myStack.push(55)
myStack.push(65)
myStack.push(75)
myStack.push(85)
myStack.show_list()
print(myStack.peek())
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.show_list()
