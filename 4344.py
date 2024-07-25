import sys

input = sys.stdin.readline

N = int(input())
case = []
answer = []
for i in range(N):
    case.append(list(map(int,input().split())))
    K = case[i].pop(0)
    avg = sum(case[i]) / K
    count = 0
    
    for j in range(K):
        if case[i][j] > avg:
            count += 1
    answer.append(round(count/K * 100, 3))

for i in range(len(answer)):
    print(answer[i], end="%\n")