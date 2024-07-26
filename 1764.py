import sys

input = sys.stdin.readline

N, M = map(int, input().split())
name = []
List = []

for _ in range(N):
    name.append(input().strip())

for _ in range(M):
    List.append(input().strip())

List = set(List)
answer = []

for i in range(N):
    if name[i] in List:
        answer.append(name[i])

answer.sort()
print(len(answer))
print(*answer, sep='\n')