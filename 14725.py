import sys

input = sys.stdin.readline

N = int(input())

cave = []

for _ in range(N):
    ant = list(input().split())
    cave.append(ant[1:])
cave.sort()

for j in range(len(cave[0])):
    print('--' * j + cave[0][j])

for i in range(1, N):
    count = -1
    for j in range(len(cave[i])):
        if len(cave[i-1]) <= j or cave[i-1][j] != cave[i][j]:
            break
        else:
            count = j
    
    for j in range(count+1, len(cave[i])):
        print('--'* j + cave[i][j])