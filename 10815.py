import sys

input = sys.stdin.readline

N = int(input())
Card_N = set(input().split())
M = int(input())
Card_M = input().split()

answer = []

for i in range(M):
    if Card_M[i] in Card_N:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)