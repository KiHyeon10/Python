import sys
import math

input = sys.stdin.readline

M, N = map(int, input().split())

answer = list(True for i in range(N + 1))

for i in range(2, int(math.sqrt(N)) + 1):
    if answer[i] == True:
        j = 2
        while i * j <= N:
            answer[i * j] = False
            j += 1

for i in range(M, len(answer)):
    if answer[i]:
        if i > 1:
            print(i)