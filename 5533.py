import sys

input = sys.stdin.readline

N = int(input())

score = []

for i in range(N):
    score.append([])
    score[i] = list(map(int, input().split()))
    
flag1 = 0
flag2 = 0
flag3 = 0

for i in range(0, N):
    for j in range(1, N):
        if i == j:
            continue
        
        if score[i][0] == score[j][0]:
            score[j][0] = 0
            flag1 = 1
        
        if score[i][1] == score[j][1]:
            score[j][1] = 0
            flag2= 1
        
        if score[i][2] == score[j][2]:
            score[j][2] = 0
            flag3 = 1
    
    if flag1 == 1:
        score[i][0] = 0
        flag1 = 0
    if flag2 == 1:
        score[i][1] = 0
        flag2 = 0
    if flag3 == 1:
        score[i][2] = 0
        flag3 = 0

for i in range(N):
    print(sum(score[i]))