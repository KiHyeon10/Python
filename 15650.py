import sys

input = sys.stdin.readline

def Find(N, M, start, num):
    if len(num) == M:
        print(' '.join(map(str, num)))
        return
    
    for i in range(start, N + 1):
        num.append(i)
        Find(N, M, i + 1, num)
        num.pop()

N, M = map(int, input().split())

Find(N, M, 1, [])