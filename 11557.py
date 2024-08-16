import sys

input = sys.stdin.readline

T = int(input())

Uni = {}
answer = []

for _ in range(T):
    N = int(input())
    for _ in range(N):
        S = input().split()
        Uni[S[0]] = int(S[1])
    answer.append(max(Uni, key=Uni.get))

print(*answer,sep='\n')