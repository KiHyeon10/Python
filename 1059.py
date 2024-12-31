import sys
input = sys.stdin.readline

L = int(input())
num = list(map(int, input().split()))
n = int(input())
num.sort()


if n in num:
    print(0)
else:

    Start, End = 1, 0
    for x in num:
        if x < n:
            Start = x + 1
        elif x > n and End == 0:
            End = x - 1
            break
    
    if End == 0:
        End = num[-1]

    count = 0
    for A in range(Start, n + 1):
        for B in range(n, End + 1):
            if A < B:
                count += 1
    
    print(count)
