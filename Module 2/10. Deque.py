from collections import deque

q = deque()

q.append(10)
q.append(20)
q.append(30)
q.appendleft(40)
print(q)
print(q.pop())
print(q.popleft())
print(q)