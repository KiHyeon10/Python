import sys

input = sys.stdin.readline

num = [0] * 101
num[1] = 1
num[2] = 1
num[3] = 1
num[4] = 2
num[5] = 2

for i in range(6, 101):
    num[i] = num[i - 2] + num[i - 3]
T = int(input())

for i in range(T):
    N = int(input())
    print(num[N])