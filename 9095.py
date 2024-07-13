import sys

input = sys.stdin.readline

N = int(input())

answer = [0] * 11
answer[0] = 1
num = [0] * N

for i in range (0, N):
    num[i] = int(input())

for i in range(1, len(answer)):
    if i - 1 >= 0:
        answer[i] += answer[i - 1]
    if i - 2 >= 0:
        answer[i] += answer[i - 2]
    if i - 3 >= 0:
        answer[i] += answer[i - 3]

for i in range (0, len(num)):
    print(answer[num[i]])