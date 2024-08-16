import sys

input = sys.stdin.readline

N, K = map(int, input().split())
num = list(range(1, N+1))
answer = []
i = 1
check = K - 1
while len(num) != 0:
    if check >= len(num):
        check -= len(num)
    if check < len(num):
        answer.append(num.pop(check))
        check += K - 1

output = '<' + ', '.join(map(str, answer)) + '>'
print(output)