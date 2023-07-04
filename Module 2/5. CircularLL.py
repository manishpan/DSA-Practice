class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def printCircular(head):
    if head == None:
        return
    print(head.key, end = " ")
    curr = head.next
    while curr != head:
        print(curr.key, end=" ")
        curr = curr.next 

def insertAtBeginningLinear(head, key):
    temp = Node(key)
    if head == None:
        temp.next= temp
        return temp
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = temp
    temp.next = head
    return temp

def insertAtBeginning(head, key):
    temp = Node(key)
    if head == None:
        temp.next = temp
        return temp
    temp.next = head.next
    head.next = temp
    temp.key, head.key = head.key, temp.key
    return head

def insertAtEnd(head, key):
    temp = Node(key)
    if head == None:
        temp.next = temp
        return temp
    temp.next = head.next
    head.next = temp
    head.key, temp.key = temp.key, head.key
    return temp

def deleteHead(head):
    if head == None or head.next == head:
        return None
    head.key = head.next.key
    head.next = head.next.next
    return head

def deleteKNode(head, k):
    if head == None:
        return head
    elif k == 1:
        return deleteHead(head)
    curr = head
    for i in range(k-2):
        curr = curr.next
    curr.next = curr.next.next
    return head

head = None
head = insertAtEnd(head, 10)
head = insertAtEnd(head, 5)
head = insertAtEnd(head, 20)
head = insertAtEnd(head, 15)
head = insertAtEnd(head, 33)
head = insertAtEnd(head, 45)
head = insertAtEnd(head, 25)

printCircular(head)
print("\n")

head = deleteKNode(head, 4)
printCircular(head)
print("\n")