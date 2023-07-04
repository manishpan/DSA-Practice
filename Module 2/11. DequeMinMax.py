from collections import deque

class RandomDS:
    def __init__(self):
        self.d = deque()

    def insertMin(self, x):
        self.d.appendleft(x)
    
    def insertMax(self, x):
        self.d.append(x)
    
    def extractMin(self):
        return self.d.popleft()
    
    def extractMax(self):
        return self.d.pop()
    
    def getMin(self):
        return self.d[0]
    
    def getMax(self):
        return self.d[-1]
    
de = RandomDS()
de.insertMin(5)
de.insertMin(10)
de.insertMin(3)
de.insertMax(15)
de.insertMin(2)
print(de.getMin())
print(de.getMax())
de.insertMin(1)
print(de.getMin())
de.insertMax(20)
print(de.getMax())