import sys

input = sys.stdin.readline

N, M = map(int, input().split())

poketmon = {}
answer = []

for i in range(1, N + 1):
    a = input().strip()
    poketmon[i] = a
    poketmon[a] = i

for i in range(M):
    quest = input().strip()
    if quest.isdigit():
        answer.append(poketmon[int(quest)])
    else:
        answer.append(poketmon[quest])

print(*answer, sep='\n')