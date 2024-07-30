import sys

input = sys.stdin.readline

sen = list(input().strip())

start = 0
end = 0
flag = 0
answer = []

for i in range(len(sen)):
    if sen[i] != ' ':
        end += 1
    elif flag == 0 and sen[i] == ' ':
        for j in range(i-1, start - 1, -1):
            answer.append(sen[j])
        answer.append(' ')    
        start = i + 1
        end = i
    if flag == 0 and sen[i] == '<':
        for j in range(i-1, start - 1, -1):
            answer.append(sen[j])
        answer.append('<')
        start = i + 1
        flag = 1
    elif flag == 1 and sen[i] == '>':
        for j in range(start, i):
            answer.append(sen[j])
        answer.append('>')
        start = i + 1
        end = i
        flag = 0
        
if flag == 0 and sen[len(sen) - 1] != '>':
    for j in range(i, start - 1, -1):
         answer.append(sen[j])

print("".join(answer))