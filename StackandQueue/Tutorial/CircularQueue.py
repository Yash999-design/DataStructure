class EmptyQueueError(Exception):
    pass


class Queue:

    def __init__(self, default_size=10):
        self.items = [None] * default_size
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def enqueue(self, item):
        if self.count == len(self.items):
            self.resize(2*len(self.items))

        i = (self.front + self.count) % len(self.items)
        self.items[i] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items[self.front]

    def display(self):
        print(self.items)

    def resize(self, newsize):
        old_list = self.items
        self.items = [None] * newsize
        i = self.front
        for j in range(self.count):
            self.items[j] = old_list[i]
            i = (1+i) % len(old_list)
        self.front = 0


if __name__ == "__main__":
    myQueue = Queue()
    myQueue.enqueue(5)
    myQueue.enqueue(10)
    myQueue.enqueue(15)
    myQueue.enqueue(25)
    myQueue.enqueue(35)
    myQueue.enqueue(45)
    myQueue.enqueue(55)
    myQueue.enqueue(65)
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.enqueue(115)
    myQueue.enqueue(125)
    myQueue.enqueue(135)
    myQueue.enqueue(145)
    myQueue.enqueue(155)
    myQueue.enqueue(165)
    myQueue.enqueue(175)
    myQueue.enqueue(185)
    myQueue.display()
