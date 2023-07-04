class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None
    
def printList(head):
    curr = head
    while curr != None:
        print(curr.key, end = " ")
        curr = curr.next

def reverseLL(head):
    prev, curr = None, head
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

head = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head = reverseLL(head)
printList(head)
print("\n")