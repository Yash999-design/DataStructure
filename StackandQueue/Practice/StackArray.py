class EmptyStackError(Exception):
    pass


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        popped_item = self.items[-1]
        self.items.pop()
        return f"popped_item is : {popped_item}"

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty, thus there is no peek")
        return self.items[-1]
    
    def show_list(self):
        print(self.items)

if __name__ == "__main__":
    myStack = Stack()
    myStack.push(10)
    myStack.push(20)
    myStack.push(30)
    myStack.push(40)
    myStack.push(50)
    myStack.show_list()
    print(myStack.peek())
    print(myStack.pop())
    myStack.show_list()
