class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None]*k
        self.head = 0
        self.tail = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.queue[self.tail%self.size] is None:
            self.queue[self.tail%self.size] = value
            self.tail +=1
            return True
        return False

    def deQueue(self) -> bool:
        if self.queue[self.head%self.size] is not None:
            self.queue[self.head%self.size] = None
            self.head +=1
            return True
        return False

    def Front(self) -> int:
        if self.head == self.tail:
            return -1
        return self.queue[self.head%self.size]

    def Rear(self) -> int:
        if self.tail >= self.size:
            return self.queue[(self.tail-1)%self.size]
        elif self.tail < self.size and self.tail > self.head:
            return self.queue[(self.tail-1)%self.size]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.tail == self.head:
            return True
        return False

    def isFull(self) -> bool:
        if (self.head == 0 and self.tail >= self.size) or (self.queue[(self.tail%self.size)] == self.queue[self.head] != None) or (self.tail%self.size == self.head -1):
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()