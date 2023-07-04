class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def printDLL(head):
    curr = head
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next

def insertAtBeginning(head, data):
    temp = Node(data)
    if head != None:
        head.prev = temp
    temp.next = head
    return temp

def insertAtEnd(head, data):
    temp = Node(data)
    if head == None:
        return temp
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = temp
    temp.prev = curr
    return head

def deleteHead(head):
    if head == None or head.next == None:
        return None
    head = head.next
    head.prev = None
    return head

def deleteLast(head):
    if head == None or head.next == None:
        return None
    curr = head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None
    return head

def reverseDLL(head):
    if head == None or head.next == None:
        return head
    prev, curr = None, head
    while curr != None:
        prev = curr
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr.prev
    return prev

head = None
head = insertAtEnd(head, 0)
head = insertAtEnd(head, 23)
head = insertAtEnd(head, 222)

printDLL(head)
print("\n")

head = reverseDLL(head)
printDLL(head)