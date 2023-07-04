

#Method 3: Linked list implementation

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class MyStack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp
        self.size = self.size + 1
    
    def pop(self):
        if self.head == None:
            return "Stack Underflow"
        temp = self.head
        self.head = self.head.next
        self.size = self.size - 1
        return temp.data
    
    def peek(self):
        if self.head == None:
            return "Stack Underflow"
        return self.head.data
    
    def length(self):
        return self.size
    
    def isEmpty(self):
        if self.head == None:
            return True
        return False

def Balanced_Parenthesis(se):
    if len(se) == 0:
        return True
    if len(se) % 2 != 0:
        return False
    pdict = {')':'(', '}':'{', ']':'['}
    stack = MyStack()
    for i in se:
        if i in ('(', '{', '['):
            stack.push(i)
        if i in (')','}',']') and stack.peek() == pdict[i]:
            stack.pop()
    return stack.isEmpty()

se = ")("
print(Balanced_Parenthesis(se))