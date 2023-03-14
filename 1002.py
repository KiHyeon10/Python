import sys
input = sys.stdin.readline

a = int(input())
point = []
for j in a:
    point[j] = map(int, input().split())

for i in len(point):
    for j in len(point[i]):
        if 