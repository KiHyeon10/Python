import sys
input = sys.stdin.readline

N, M = map(int, input().split())
queue = [False] * N

def left():
    queue.append(queue.pop(0))

def right():
    queue.insert(0, queue.pop())

num = list(map(int, input().split()))

for i in range(M):
    queue[num[i]-1] = i + 1

point = 0
count = 0

for i in range(1, M+1):
    while queue[0] != i:
        if queue.index(i) > len(queue) - queue.index(i):
            right()
        
        elif queue.index(i) <= len(queue) - queue.index(i):
            left()
        
        count += 1

    queue.pop(0)

print(count)