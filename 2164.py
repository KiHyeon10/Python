import sys

input = sys.stdin.readline

N = int(input())
if N == 1:
    print(1)
    exit()

num = list(range(2, N+1, 2))

while len(num) != 1:
    print(num)
    num = [value for index, value in enumerate(num) if index % 2 != 0]

print(*num)