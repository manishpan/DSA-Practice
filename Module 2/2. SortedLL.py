class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None
    
def printList(head):
    curr = head
    while curr != None:
        print(curr.key, end = " ")
        curr = curr.next

def sortedInsert(head, key):
    temp = Node(key)
    if head == None:
        return temp
    elif key < head.key:
        temp.next = head
        return temp
    curr = head
    while curr.next != None and curr.next.key < key:
        curr = curr.next
    temp.next = curr.next
    curr.next = temp
    return head

head = Node(10)
head.next = Node(30)
head.next.next = Node(40)

printList(head)
print("\n")
head = sortedInsert(head, 20)
printList(head)
print("\n")
head = sortedInsert(head, 5)
printList(head)
print("\n")
head = sortedInsert(head, 50)
printList(head)
print("\n")
head = sortedInsert(head, 45)
printList(head)
