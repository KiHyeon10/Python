import sys
input = sys.stdin.readline

N, L = map(int, input().split())

for i in range(L, 101):
    Start = (N - (i * (i-1)) // 2) / i

    if Start < 0:
        continue
    
    if Start.is_integer():
        Start = int(Start)
        sum = 0
        length = i

        for j in range(Start, Start + i):
            sum += j
        
        if sum == N:
            break
    
    else:
        Start = -1

if Start < 0:
    print(-1)

else:
    for i in range(int(Start), int(Start+length)):
        print(i, end=' ')