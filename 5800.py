import sys

input = sys.stdin.readline

K = int(input())
answer = []

for i in range (0, K):
    score = list(map(int, input().split()))
    N = score.pop(0)
    
    gap = 0
    
    score.sort(reverse=True)
    answer.append([])
    answer[i].append(score[0])
    answer[i].append(score[N-1])
    
    for j in range (1, N):
        if score[j-1] - score[j] > gap:
            gap = score[j-1] - score[j]
    answer[i].append(gap)

for i in range(0, K):
    print("Class", end=" ")
    print(i + 1)
    print("Max %d, Min %d, Largest gap %d" % (answer[i][0], answer[i][1], answer[i][2]))
    