class EmptyQueueError(Exception):
    pass


class Queue:

    def __init__(self, default_size=10):
        self.items = [None] * default_size
        self.count = 0
        self.front = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def enqueue(self, value):
        if self.count == len(self.items):
            # self.resize(self.items * 2) #! Here i multiplied the list with integer which is wrong
            # self.resize(self.count * 2) #! This is also working fine but only when you havent applied dequeue because after that your count will change and thus do not give required result
            self.resize(len(self.items) * 2)

        i = (self.count+self.front) % len(self.items)
        self.items[i] = value
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty, thus you can not dequeue.")
        i = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return i

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty, thus there is no peek.")
        return self.items[self.front]

    def show_queue(self):
        print(self.items)

    def resize(self, length):
        old_list = self.items
        self.items = [None] * length
        i = self.front

        for j in range(self.count):
            self.items[j] = old_list[i]
            i = (i+1) % len(old_list)
        self.front = 0

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
    myQueue.enqueue(110)
    myQueue.enqueue(120)
    myQueue.enqueue(130)
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.enqueue(140)
    myQueue.enqueue(150)
    myQueue.enqueue(160)
    myQueue.enqueue(170)
    myQueue.enqueue(180)
    myQueue.enqueue(190)
    myQueue.enqueue(200)
    myQueue.enqueue(210)
    myQueue.enqueue(220)
    myQueue.enqueue(230)
    myQueue.enqueue(240)    
    myQueue.enqueue(250)    
    myQueue.show_queue()