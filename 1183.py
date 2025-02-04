import sys
input = sys.stdin.readline

N = int(input())
T = []

for _ in range(N):
    a, b = map(int, input().split())
    T.append(b-a)

T.sort()
m = N // 2

if N % 2 == 1:
    print(1)
else:
    print(T[m] - T[m-1] + 1)