import sys
input = sys.stdin.readline

N, Score, P = map(int, input().split())

if N == 0:
    print(1)
    exit()

Rank = list(map(int, input().split()))
L, R = 0, len(Rank)

while L < R:
    m = (L + R) // 2

    if Rank[m] > Score:
        L = m + 1
    else:
        R = m

R = L + 1

if R <= P:
    if N == P and Rank[-1] >= Score:
        print(-1)
    else:
        print(R)
else:
    print(-1)