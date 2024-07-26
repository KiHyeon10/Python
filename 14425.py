import sys

input = sys.stdin.readline

N, M = map(int, input().split())

cor = []
ques = []
count = 0

for _ in range(N):
    cor.append(input().strip())
for _ in range(M):
    ques.append(input().strip())

for i in range(M):
    if ques[i] in cor:
        count += 1

print(count)