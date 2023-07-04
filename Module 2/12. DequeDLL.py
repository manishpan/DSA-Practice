class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None

    def insertFront(self, x):
        temp = Node(x)
        if self.front == None:
            self.front = temp
            self.rear = temp
        temp.next = self.front
        self.front.prev = temp
        self.front = temp
        self.size = self.size + 1
    
    def insertRear(self, x):
        temp = Node(x)
        if self.front == None:
            self.front = temp
            self.rear = temp
        temp.prev = self.rear
        self.rear.next = temp
        self.rear = temp
        self.size = self.size + 1

    def deleteFront(self):
        if self.front == None:
            return None
        temp = self.front.data
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        self.front.prev = None
        self.size = self.size - 1
        return temp
    
    def deleteRear(self):
        if self.front == None:
            return "Queue is empty"
        temp = self.rear
        self.rear = self.rear.prev
        temp.prev = None
        self.size = self.size - 1
        return temp.data
    
    def getFront(self):
        pass

    def getRear(self):
        pass

    def isEmpty(self):
        pass

    def length(self):
        pass