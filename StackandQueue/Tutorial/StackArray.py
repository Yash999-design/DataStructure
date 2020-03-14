class EmptyStackError(Exception):
    pass

class Stack:

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items[-1]
    
    def display(self):
        print(self.items)

if __name__ == "__main__":
    tutStack = Stack()
    print(tutStack.is_empty())
    tutStack.push(5)
    tutStack.push(10)
    tutStack.push(15)
    tutStack.push(20)
    tutStack.push(25)
    tutStack.push(30)
    tutStack.display()