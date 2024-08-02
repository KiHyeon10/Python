import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
Ground = []

for _ in range(N):
    Ground.append(list(map(int, input().split())))

count_max = 0
count_min = 0
Max = max(map(max, Ground))
Min = min(map(min, Ground))

for i in range(N):
    for j in range(M):
        count_max +=  Max - Ground[i][j]
        count_min += Ground[i][j] - Min

if count_max <=B and count_max < count_min * 2:
    print(count_max, Max)
elif count_max > B or count_min * 2 < count_max:
    print(2*count_min, Min)
elif count_max <= B and count_max == count_min * 2:
    print(count_max, Max)