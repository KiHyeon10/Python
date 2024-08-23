import sys

input = sys.stdin.readline

N = int(input())

num = set(map(int, input().split()))

M = int(input())

check = list(map(int, input().split()))

for i in check:
    if i in num:
        print(1)
    else:
        print(0)