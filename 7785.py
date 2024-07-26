import sys

input = sys.stdin.readline

N = int(input())
enter = set()

for i in range(N):
    log = list(input().split())

    if log[1] == 'enter':
        enter.add(log[0])
    elif log[1] == 'leave':
        enter.remove(log[0])

answer = list(enter)
answer.sort(reverse=True)
print(*answer, sep='\n')