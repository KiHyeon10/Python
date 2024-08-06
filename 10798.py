import sys

input = sys.stdin.readline
answer = []
line = 0
Max = 0
for i in range(5):
    sen = list(input().rstrip())
    line = len(sen)
    if line > Max:
        Max = line
    answer.append(sen)

for i in range(Max):
    for j in range(5):
        if i >= len(answer[j]):
            continue
        else:
            print(answer[j][i],end='')