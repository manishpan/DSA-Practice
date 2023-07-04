import math

class Node:
    def __init__(self, k):
        self.key = k
        self.left, self.right = None, None

def IterativeInorder(root):
    if root == None:
        return
    stack = []
    curr = root

    while curr != None:
        stack.append(curr)
        curr = curr.left
    
    while len(stack) > 0:
        curr = stack.pop()
        print(curr.key, end=' ')
        curr = curr.right
        while curr != None:
            stack.append(curr)
            curr = curr.left

def Search(root, key):
    while root != None:
        if root == None:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return False

def SearchRecursive(root, key):
    pass

def insertRecursive(root, key):
    pass

def Insert(root, key):
    if root == None:
        return Node(key)
    prev = None
    curr = root
    while curr != None:
        prev = curr
        if key == curr.key:
            return root
        elif key > curr.key:
            curr = curr.right
        else:
            curr = curr.left
    if key > prev.key:
        prev.right = Node(key)
    else:
        prev.left = Node(key)
    return root
        
def getSuccessor(curr, key):
    while curr.left != None:
        curr = curr.left
    return curr.key

def deleteNode(root, key):
    if root == None:
        return 
    if root.key > key:
        root.left = deleteNode(root.left, key)
    elif root.key < key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            succ = getSuccessor(root, key)
            root.key = succ
            root.right = deleteNode(root.right, succ)
        return root

def Floor(root, key):
    floor = None
    while root != None:
        if root.key == key:
            return key
        elif root.key > key:
            root = root.left
        else:
            floor = root.key
            root = root.right
    return floor    

def Ceil(root, key):
    ceil = None
    while root != None:
        if root.key == key:
            return key
        elif root.key < key:
            root = root.right
        else:
            ceil = root.key
            root = root.left
    return ceil

root = None
root = Node(40)
root.left = Node(20)
root.left.left = Node(8)
root.left.right = Node(30)
root.right = Node(80)
root.right.left = Node(60)
root.right.right = Node(100)
root.right.right.right = Node(120)

print(Search(root, 120))
IterativeInorder(root)
root = Insert(root, 201)
print()
IterativeInorder(root)
print()
print(Floor(root, 23))
print(Ceil(root, 61))