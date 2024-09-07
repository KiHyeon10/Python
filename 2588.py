import sys

input = sys.stdin.readline


N = int(input())
M = input()
M_L = list(M)

print(N * int(M_L[2]))
print(N * int(M_L[1]))
print(N * int(M_L[0]))
print(N * int(M))