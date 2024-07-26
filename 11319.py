import sys

input = sys.stdin.readline

gather = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

N = int(input())
count = 0
sentence = []
answer = []

for i in range(N):
    sen = list(input().strip())
    sen.remove(' ')
    while ' ' in sen:
        sen.remove(' ')
    sentence.append(sen)

for i in range(N):
    for j in range(len(sentence[i])):
        if sentence[i][j] in gather:
            count += 1
    answer.append([len(sentence[i]) - count, count])
    count = 0


for i in range(len(answer)):
    print(*answer[i])