class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None

def printList(head=None):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next

def searchList(head, x):  #Returns position and not reference
    curr = head
    count = 1
    while curr != None:
        if curr.key == x:
            return count
        curr = curr.next
        count = count + 1
    return -1

def insertAtBeginning(head, key):
    temp = Node(key)
    temp.next = head
    return temp

def insertAtEnd(head, key):
    if head == None:
        return Node(key)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(key)
    return head

def insertAtPosition(head, key, pos):
    temp = Node(key)
    if pos == 1:
        temp.next = head
        return temp
    elif pos != 1 and head == None:
        return head
    curr = head
    for i in range(pos-2):
        curr = curr.next
        if curr == None:
            return head
    temp.next = curr.next
    curr.next = temp
    return head     

def deleteFirst(head):
    if head == None:
        return None
    return head.next

def deleteLast(head):
    if head == None or head.next == None:
        return None
    curr = head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None
    return head

head = None
head = insertAtPosition(head,101,2)
head = insertAtPosition(head, 10, 1)
head = insertAtPosition(head, 10, 1)
head = insertAtPosition(head, 30, 2)
head = insertAtPosition(head, 50, 3)
head = insertAtPosition(head, 70, 4)
head = insertAtPosition(head, 20, 2)
head = insertAtPosition(head, 100,1)

printList(head)
print("\n")
head = deleteFirst(head)

printList(head)

head = deleteLast(head)

print("\n")
printList(head)
print(searchList(head, 301))