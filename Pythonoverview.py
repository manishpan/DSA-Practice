# This is an overview of python programming language

# Null in python
n = None

# Division in python is by default decimal and not integer division(unlike other languages)
print(5 / 2)  #Decimal division output - 2.5
print(5 // 2) #Integer division output - 2
print(-3 // 2)#Integer division output - -2 (other languages will round toward 0, but python rounds down)
print(int(-3 / 2)) #Like other programming languaggs, output is -1

#Similar case if for modulo operator
print(10 % 3) #output - 1
print(-10 % 3) #output - 2
#the following code corrects this behaviour and make it consistent with other languages
import math
print(math.fmod(-10, 3)) #output - -1.0

#Infinity
float("inf")
float("-inf")

#Arrays(called list in python)
arr = [1, 2, 3]
print(arr)

#can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)
print(arr)

arr[0] = 0

n = 5
arr = [1] * n
print(arr)

a, b, c = [1, 2, 3]

nums = [1, 2, 3]

#Using index
for i in range(len(nums)):
    print(nums[i])

#Using without Index
for i in nums:
    print(i)

#using index and value
for i, n in enumerate(nums):
    print(i, n)

nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

#Reverse
nums1.reverse()

#sorting
nums1.sort()

arr = ["bob", "alice", "jane", "john"]
arr.sort()
print(arr)

#Custom sort(by length of string)

arr.sort(key= lambda x: len(x))
print(arr)


#List comprehension
arr = [i+i for i in range(5)]
print(arr)

#2-d lists
arr = [[0] * i for i in range(4)]
print(arr)

#Strings are similar to arrays, but strings are immuatable
s = "abc"
print(s[0:2])

#Queues in python are by default double ended queues
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

queue.pop()
print(queue)


#Hashset , we can search, insert and remove in constant time in hashsets(no duplicates allowed)
mySet = set()   

mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))

print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(2 in mySet)

#list to set
print(set([1, 2, 3]))

#Set comprehension
mySet = {i for i in range(5)}
print(mySet)


### Hashmaps(aka dict)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
print(len(myMap))

myMap["alice"] = 80
print(myMap["alice"])

print("alice" in myMap)
myMap.pop("alice")
print("alice" in myMap)

myMap = {"alice": 90, "bob":70}
print(myMap)

#Dict comprehension
myMap = {i: 2*i for i in range(3)}

#Tuples
myMap = {(1, 2): 3}
print(myMap[(1, 2)])

mySet = set()
mySet.add((1,2))
print((1,2) in mySet)

#list can`t be keys
myMap[[3, 4]] = 5


#heap
import heapq

#under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

#Min is always at index 0
print(minHeap[0])`

while len(minHeap):
    print(heapq.heappop(minHeap))


#variables
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c
    return inner()

print(outer("a", "b"))

#Class
class MyClass:
    # Constructor
    def __init__(self, nums):
        #create member variables
        self.nums = nums
        self.size = len(nums)

    def getLength(self):
        return self.size