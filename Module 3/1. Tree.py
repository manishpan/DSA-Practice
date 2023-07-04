import math
from collections import deque

class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k
    
def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

def preorder(root):
    if root != None:
        print(root.key, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end = ' ')

def NumNodes(root):
    if root == None:
        return 0
    return NumNodes(root.left) + NumNodes(root.right) + 1

def Maximum(root):
    if root == None:
        return (-math.inf)
    left_max = Maximum(root.left)
    right_max = Maximum(root.right)
    return max(left_max, right_max, root.key)

def Search(root, key):
    if root == None:
        return False
    if root.key == key:
        return True
    return Search(root.left, key) or Search(root.right, key)

def Height(root):
    if root == None:
        return 0
    left_height = Height(root.left)
    right_height = Height(root.right)
    return max(left_height, right_height) + 1

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

def IterativePreorder(root):
    if root == None:
        return
    stack = [root]

    while len(stack) > 0:
        curr = stack.pop()
        print(curr.key, end=' ')
        if curr.right != None:
            stack.append(curr.right)
        if curr.left != None:
            stack.append(curr.left)
    
def IterativePostorder(root):
    pass

def LevelOrderTraversal(root):
    if root == None:
        return 
    de = deque()
    de.append(root)
    while len(de) > 0:
        curr = de.popleft()
        print(curr.key, end = ' ')
        if curr.left != None:
            de.append(curr.left)
        if curr.right != None:
            de.append(curr.right)

root = None
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

print(NumNodes(root))
print(Maximum(root.left))
print(Search(root, 22))
print(Height(root))
inorder(root)
print()
IterativeInorder(root)
print()
preorder(root)
print()
IterativePreorder(root)
print()
postorder(root)
print()
IterativePostorder(root)
print()
LevelOrderTraversal(root)