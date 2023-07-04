class MyDeque:
    def __init__(self, c):
        self.l = [None] * c
        self.cap = c
        self.size = 0
        self.front = 0

    def insertRear(self, x):
        if self.size == self.cap:
            return
        new_rear = (self.front + self.size) % self.cap
        self.l[new_rear] = x
        self.size = self.size + 1

    def insertFront(self, x):
        if self.size == self.cap:
            return
        self.front = (self.front - 1) % self.cap
        self.l[self.front] = x
        self.size = self.size + 1

    def deleteFront(self):
        if self.size == 0:
            return None
        res = self.l[self.front]
        self.front = (self.front + 1) % self.cap
        self.size = self.size - 1
        return res
    
    def deleteRear(self):
        if self.size == 0:
            return None
        rear = (self.front + self.size - 1) % self.cap
        res = self.l[self.rear]
        return res
    

        