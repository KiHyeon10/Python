import sys

input = sys.stdin.readline

Case = int(input())
answer = []

for c in range (0, Case):
    PS = list(input().strip())
    another = []
    flag = 0
    
    for i in range(0, len(PS)):
        if PS[i] == '(':
            another.append('(')
        elif PS[i] == ')':
            if len(another) != 0:
                another.pop()
            else:
                flag = 1
                break
    
    if len(another) == 0 and flag == 0:
        answer.append('YES')
    else:
        answer.append('NO')
        
for i in range(len(answer)):
    print(answer[i])