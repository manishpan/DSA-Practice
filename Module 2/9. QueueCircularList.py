class MyQueue:
    def __init__(self, c):
        self.que = [0] * c
        self.front = 0
        self.rear = 0
        self.size = 0
        self.capacity = c

    def enque(self, x):
        self.rear = (self.rear + 1) % self.capacity
        if self.rear == self.front:
            print("Queue is full")
            return
        self.que[self.rear] = x
        self.size = self.size + 1

    def deque(self):
        if self.front == self.rear:
            return "Queue is empty"
        self.front = (self.front + 1) % self.capacity
        temp = self.que[self.front]
        self.que[self.front] = 0
        self.size = self.size - 1
        return temp

    def getFront(self):
        if self.front == self.rear:
            return "Queue is empty"
        return self.que[self.front]
    
    def getRear(self):
        if self.front == self.rear:
            return "Queue is empty"
        return self.que[self.rear]

    def length(self):
        return self.size
    
    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False

q = MyQueue(5)
q.enque(10)
q.enque(20)
q.enque(30)
print(q.deque())
print(q.length())
q.enque(40)
print(q.getFront())
print(q.getRear())
print(q.isEmpty())