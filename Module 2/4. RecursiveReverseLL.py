class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None
    
def printList(head):
    curr = head
    while curr != None:
        print(curr.key, end = " ")
        curr = curr.next

def recursiveReverseLL1(head):
    if head == None or head.next == None:
        return head
    rest_head = recursiveReverseLL1(head.next)
    rest_tail = head.next
    rest_tail.next = head
    head.next = None
    return rest_head

def recursiveReverseLL2(curr, prev=None):
    if curr == None:
        return prev
    next = curr.next
    curr.next = prev
    return recursiveReverseLL2(next, curr)

head = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head = recursiveReverseLL2(head)
printList(head)
print("\n")
head = recursiveReverseLL1(head)
printList(head)
print("\n")