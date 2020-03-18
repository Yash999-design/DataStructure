class StackEmptyError(Exception):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start == None
    
    def size(self):
        if self.start is None:
            return 0
        else:
            p = self.start
            count = 0
            while p is not None:
                count += 1
                p = p.next
            return count
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.start
        self.start = new_node
    
    def pop(self):
        if self.is_empty():
            raise StackEmptyError("Stack is empty, so you can't pop.")
        popped_item = self.start.value
        self.start = self.start.next
        return f"popped item is : {popped_item}"
    
    def peek(self):
        if self.is_empty():
            raise StackEmptyError("Stack is empty, thus there is no peek")
        return f"peek item is : {self.start.value}"
    
    def showStack(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            p = self.start
            while p is not None:
                print(p.value, " ", end='')
                p = p.next
            print()

if __name__ == "__main__":
    myStack = Stack()
    myStack.push(10)
    myStack.push(20)
    myStack.push(30)
    myStack.push(40)
    myStack.push(50)
    myStack.push(60)
    myStack.push(70)
    myStack.showStack()
    print(myStack.peek())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())