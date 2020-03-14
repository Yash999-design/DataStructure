class StackEmptyError(Exception):
    pass

class StackFullError(Exception):
    pass

class Stack:
    def __init__(self, max_size=10):
        self.items = [None] * max_size
        self.count = 0
    
    def size(self):
        return self.count
    
    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == len(self.items)
    
    def push(self, x):
        if self.is_full():
            raise StackFullError("Stack is full, can't push")
        self.items[self.count] = x
        self.count += 1
    
    def pop(self):
        if self.is_empty():
            raise StackEmptyError("Stack is empty, can't pop")

        x = self.items[self.count - 1]
        self.items[self.count - 1] = None
        self.count -= 1
        return f"Popped item : {x}"
    
    def peek(self):
        if self.is_empty():
            raise StackEmptyError("Stack is empty, Thus no peek")
        return self.items[self.count - 1]
    
    def display_stack(self):
        print(self.items[0:self.count])

if __name__ == "__main__":
    tutStack = Stack(30)
    tutStack.push(5)
    tutStack.push(10)
    tutStack.push(15)
    tutStack.push(25)
    tutStack.push(35)
    tutStack.push(45)
    tutStack.push(55)
    tutStack.push(65)
    tutStack.push(75)
    tutStack.push(85)
    tutStack.push(95)
    tutStack.push(105)
    tutStack.push(115)
    tutStack.push(125)
    tutStack.push(135)
    tutStack.push(145)
    tutStack.push(155)
    tutStack.push(165)
    tutStack.push(175)
    tutStack.push(185)
    tutStack.push(195)
    tutStack.display_stack()
    print(tutStack.size())
    print(tutStack.pop())
