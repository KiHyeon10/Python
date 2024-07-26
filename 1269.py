import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

count_A = A - B
count_B = B - A
print(len(count_A) + len(count_B))