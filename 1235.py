import sys
input = sys.stdin.readline

T = int(input())
num = []

for _ in range(T):
    num.append(input().rstrip())
count = 0

for i in range(len(num[0])-1, -1, -1):
    a = []
    for j in range(T):
        a.append(num[j][i:len(num[0])])

    if T == len(set(a)):
        count = len(num[0]) - i
        print(count)
        break