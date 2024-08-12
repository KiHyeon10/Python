import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
answer = []

for i in range(N):
    Site = input().split()
    dic[Site[0]] = Site[1]

for i in range(M):
    Find = input().rstrip()
    if Find in dic.keys():
        answer.append(dic[Find])
        
print(*answer, sep='\n')