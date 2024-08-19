import sys
from collections import deque

input = sys.stdin.readline

N, M, Node = map(int, input().split())

def dfs(graph, V, Node):
    V[Node] = True
    print(Node, end=' ')
    
    for i in sorted(graph[Node]):
        if not V[i]:
            dfs(graph, V, i)

def bfs(graph, V, Node):
    queue = deque([Node])
    V[Node] = True
    
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        
        for i in sorted(graph[node]):
            if not V[i]:
                V[i] = True
                queue.append(i)

graph = [[] for _ in range(N+ 1)]

for _ in range(M):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

V = [False] * (N+1)

dfs(graph, V, Node)
print()

V = [False] * (N+1)

bfs(graph, V, Node)