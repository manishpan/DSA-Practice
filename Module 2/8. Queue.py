class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class MyQueue:
    def __init__(self):
        self.front, self.rear, self.size = None, None, 0

    def enque(self, x):
        temp = Node(x)
        if self.front == None:
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self.size = self.size + 1

    def deque(self):
        if self.front == None:
            return "Queue is empty."
        temp = self.front.data
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        self.size = self.size - 1
        return temp
    
    def getFront(self):
        if self.front == None:
            return "Queue is empty"
        return self.front.data
    
    def getRear(self):
        if self.front == None:
            return "Queue is empty"
        return self.rear.data

    def length(self):
        return self.size
    
    def isEmpty(self):
        if self.front == None:
            return True
        return False
    
q = MyQueue()
q.enque(10)
q.enque(20)
q.enque(30)
print(q.deque())
print(q.length())
q.enque(40)
print(q.getFront())
print(q.getRear())
print(q.isEmpty())