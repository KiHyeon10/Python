import sys
import math
input = sys.stdin.readline

A, B = map(int, input().split())

Find = [True for x in range(B+2)]
Find[0] = Find[1] = False

for i in range(2, int(math.sqrt(B+1))+1):
    if Find[i] == True:
        for j in range(i*i, B+2, i):
            Find[j] = False

count = [0] * (B + 2)

for i in range(2, B + 2):
    if Find[i]:
        count[i] = 1
    else:
        num = i
        for j in range(2, int(math.sqrt(i)) + 1):
            while num % j == 0:
                count[i] += 1
                num //= j
        if num > 1:
            count[i] += 1

answer = 0
for i in range(A, B + 1):
    if Find[count[i]]:
        answer += 1

print(answer)