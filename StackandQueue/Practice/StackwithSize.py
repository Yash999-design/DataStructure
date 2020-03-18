class EmptyStackError(Exception):
    pass


class Stack:

    def __init__(self, length=10):
        self.items = [None] * length
        self.count = 0

    def is_Empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def push(self, data):
        if self.count != len(self.items) - 1:
            self.items[self.count] = data
            self.count += 1

    def pop(self):
        if self.is_Empty():
            raise EmptyStackError("Stack is empty, so you can't pop")
        popped_item = self.items[self.count - 1]
        self.items.pop(self.count - 1)
        self.count -= 1
        return popped_item

    def peek(self):
        if self.is_Empty():
            raise EmptyStackError("Stack is empty, thus there is no peek")
        return self.items[self.count-1]

    def show_stack(self):
        if self.is_Empty():
            print("Stack is empty")
            return
        else:
            print(self.items[0: self.count])


if __name__ == "__main__":
    myStack = Stack()
    myStack.show_stack()
    myStack.push(10)
    myStack.push(20)
    myStack.push(30)
    myStack.push(40)
    myStack.push(50)
    myStack.push(60)
    myStack.push(70)
    myStack.show_stack()
    print(myStack.peek())
    print(myStack.is_Empty())
    print(myStack.size())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())
    myStack.show_stack()