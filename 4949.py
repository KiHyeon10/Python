import sys

input = sys.stdin.readline

Stack = []
answer = []

while True:
    sen = input().rstrip()
    if sen == '.':
        break
    for i in range(len(sen)):
        if sen[i] == '(' or sen[i] == '[':
            Stack.append(sen[i])
        elif (sen[i] == ')' or sen[i] == ']'):
            if len(Stack) != 0:
                if sen[i] == ')' and Stack[len(Stack) - 1] == '(':
                    Stack.pop()
                elif sen[i] == ']' and Stack[len(Stack) - 1] == '[':
                    Stack.pop()
                else:
                    Stack.append(1)
                    break
            else:
                Stack.append(1)
                break
            
    if len(Stack) != 0:
        answer.append('no')
    else:
        answer.append('yes')
    Stack.clear()

print(*answer, sep='\n')