import sys

input = sys.stdin.readline

sen = input().strip()
answer = set()
start = 0
end = 1
i = 1

while i != len(sen):
    if sen[start:end] not in answer:
        answer.add(sen[start:end])
        start += 1
        end += 1
    else:
        start += 1
        end += 1
    if end == len(sen) + 1:
        i += 1
        start = 0
        end = i

print(len(answer) + 1)