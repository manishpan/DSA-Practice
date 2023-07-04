from collections import deque

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def printGraph(adj):
    for i in adj:
        print(i)

def BreadthFirstSearch(adj, s):
    q = deque()
    hashset = set()
    q.append(s)
    while q:
        temp = q.popleft()
        if temp not in hashset:
            hashset.add(temp)
            print(temp, end = ' ')
            q.extend(adj[temp])

def BFS(adj, s, visited):
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        s = q.popleft()
        #print(s, end = ' ')
        for u in adj[s]:
            if visited[u] == False:
                visited[u] = True
                q.append(u)

def BFSDis(adj):
    visited = [False] * len(adj)
    for u in range(len(adj)):
        if visited[u] == False:
            BFS(adj, u, visited)

def NumberofConnectedCompomentsBFS(adj):
    visited = [False] * len(adj)
    count = 0
    for u in range(len(adj)):
        if visited[u] == False:
            count = count + 1
            BFS(adj, u, visited)
    return count

def DFSRec(adj, s, visited):
    visited[s] = True
    #print(s, end = ' ')
    for u in adj[s]:
        if visited[u] == False:
            DFSRec(adj, u, visited)

def DFS(adj, s):
    visited = [False] * len(adj)
    DFSRec(adj, s, visited)

def DFSDis(adj):
    visited = [False] * len(adj)
    for u in range(len(adj)):
        if visited[u] == False:
            DFSRec(adj, u, visited)

def NumberofConnectedComponentsDFS(adj):
    visited = [False] * len(adj)
    res = 0
    for u in range(len(adj)):
        if visited[u] == False:
            res = res + 1
            DFSRec(adj, u, visited)
    return res

def DFS_Iterative(adj, s):
    pass

def BFS_Iterative(adj, s):
    pass

def DFS_Preorder(adj, s):
    pass

def DFS_Postorder(adj, s):
    pass

V = 4
adj = [[] for i in range(V)]
addEdge(adj, 0, 1)
addEdge(adj, 0, 2)
addEdge(adj, 1, 2)
addEdge(adj, 1, 3)

printGraph(adj)
BreadthFirstSearch(adj, 0)
print()
print(NumberofConnectedCompomentsBFS(adj))
print()
DFS(adj, 3)
print()
DFSDis(adj)
print()
print(NumberofConnectedComponentsDFS(adj))