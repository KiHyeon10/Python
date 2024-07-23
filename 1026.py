import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
sum = 0

for i in range(0, N):
    sum += A[i] * B[i]

print(sum)