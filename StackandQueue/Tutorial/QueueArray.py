class EmptyQueueError(Exception):
    pass

class Queue:

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.items[0]
    
    def display(self):
        print(self.items)

if __name__ == "__main__":
    myQueue = Queue()
    myQueue.enqueue(10)
    myQueue.enqueue(20)
    myQueue.enqueue(30)
    myQueue.enqueue(40)
    myQueue.enqueue(50)
    myQueue.enqueue(60)
    myQueue.enqueue(70)
    myQueue.enqueue(80)
    myQueue.enqueue(90)
    myQueue.enqueue(100)
    myQueue.display()
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.display()
