class EmptyQueueError(Exception):
    pass

class Queue:

    def __init__(self):
        self.items = []
        self.front = 0
    
    def is_empty(self):
        return self.front == len(self.items)
    
    def size(self):
        return len(self.items) - self.front
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty so you can't complete dequeue operation")
        x = self.items[self.front]
        self.items[self.front] = None
        self.front += 1
        return f"Popped item : {x}"
    
    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty, thus there is no peak")
        return self.items[self.front]

    def display(self):
        print(f"Queue is : {self.items[self.front:]}")

if __name__ == "__main__":
    myQueue = Queue()
    myQueue.enqueue(10)
    myQueue.enqueue(20)
    myQueue.enqueue(30)
    myQueue.enqueue(40)
    myQueue.enqueue(50)
    myQueue.enqueue(60)
    print(myQueue.dequeue())
    myQueue.display()
    print(myQueue.peek())