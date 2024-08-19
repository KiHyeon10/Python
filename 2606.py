import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

network = [[] for _ in range(N+1)]

def Find(network, V, Finding):
    V[Finding] = True
    
    for i in network[Finding]:
        if not V[i]:
            Find(network, V, i)
        

for i in range(K):
    com1, com2 = map(int, input().split())
    
    network[com1].append(com2)
    network[com2].append(com1)

V = [False] * (N+1)

Find(network, V, 1)

print(sum(V) - 1)