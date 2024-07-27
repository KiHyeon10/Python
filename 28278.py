import sys

input = sys.stdin.readline

N = int(input())

Stack = []
answer = []

for i in range(N):
    com = input().split()
    
    if com[0] == '1':
        Stack.append(com[1])
    elif com[0] == '2':
        if Stack:
            answer.append(Stack.pop())
        else:
            answer.append(-1)
    elif com[0] == '3':
        answer.append(len(Stack))
    elif com[0] == '4':
        if  Stack:
            answer.append(0)
        else:
            answer.append(1)
    elif com[0] == '5':
        if Stack:
            answer.append(Stack[len(Stack) - 1])
        else:
            answer.append(-1)

print(*answer, sep='\n')