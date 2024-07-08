import sys

input = sys.stdin.readline

Stack = [] #스택 저장
answer = [] #답 저장

def empty():
    if len(Stack) == 0:
        return 1;
    else:
        return 0;

command = int(input())

for i in range(0, command):
    
    com = input().strip()
    
    if "push" in com:
        com = com.split()
        value = int(com[1])
        Stack.append(value)
        
    elif com == 'pop':
        if len(Stack) == 0:
            answer.append(-1)
        else:
            answer.append(Stack.pop())
            
    elif com == "empty":
        answer.append(empty())
        
    elif com == "size":
        answer.append(len(Stack))
        
    elif com == "top":
        if empty() == 1:
            answer.append(-1)
        else:
            answer.append(Stack[len(Stack) - 1])

for i in range (0, len(answer)):
    print(answer[i])