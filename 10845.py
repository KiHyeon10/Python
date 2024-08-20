import sys

input = sys.stdin.readline

N = int(input())
queue = []
for i in range(N):
    com = input().split()
    
    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        if len(queue) != 0:
            print(0)
        else:
            print(1)
    elif com[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif com[0] == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)