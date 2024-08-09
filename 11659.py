import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

answer = [0]
sum = 0
A = []

for i in num:
    sum += i
    answer.append(sum)

for i in range(M):
    i, j = map(int, input().split())
    A.append(answer[j] - answer[i-1])

print(*A, sep='\n')