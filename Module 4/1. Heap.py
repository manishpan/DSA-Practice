import math

class MinHeap:
    def __init__(self, ls=[]):
        self.arr = ls
        i = (len(l) - 2) // 2
        while i >= 0:
            self.minHeapify(i)
            i = i - 1

    def parent(self, i):
        return (i-1) // 2
    
    def leftChild(self, i):
        return 2 * i + 1
    
    def rightChild(self, i):
        return 2 * i + 2
    
    def insert(self, x):
        self.arr.append(x)
        i = len(self.arr) - 1
        while i != 0 and self.arr[i] < self.arr[self.parent(i)]:
            par = self.parent(i)
            self.arr[i], self.arr[par] = self.arr[par], self.arr[i]
            i = par
            
    def minHeapify(self, i):
        arr = self.arr
        left = self.leftChild(i)
        right = self.rightChild(i)
        smallest = i
        n = len(arr)
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.minHeapify(smallest)
    
    def minHeapifyIterative(self, i):
        pass

    def extractMin(self):
        if len(self.arr) == 0:
            return math.inf
        res = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()        
        self.minHeapify(0)
        return res

    def decreaseKey(self, i, x):
        arr = self.arr
        arr[i] = x
        while i != 0 and arr[i] < arr[self.parent(i)]:
            par = self.parent(i)
            arr[i], arr[par] = arr[par], arr[i]
            i = par

    def delete(self, i):
        if i > len(self.arr):
            return
        self.decreaseKey(i, -math.inf)
        self.extractMin()

