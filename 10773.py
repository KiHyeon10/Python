import sys

input = sys.stdin.readline

Stack = []

total = int(input())

for i in range(0, total):
    num = int(input())
    
    if num == 0:
        Stack.pop()
    else:
        Stack.append(num)

print(sum(Stack))