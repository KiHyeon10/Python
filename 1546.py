import sys

input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))

Big = max(score)

for i in range(N):
    if score[i] != Big:
        score[i] = score[i] / Big * 100
    else:
        score[i] = 100

print(sum(score)/len(score))