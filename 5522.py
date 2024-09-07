import sys

input = sys.stdin.readline

sum = 0

for _ in range(5):
    num = int(input())
    sum += num

print(sum)