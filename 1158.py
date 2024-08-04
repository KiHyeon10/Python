import sys

input = sys.stdin.readline

N, K = map(int, input().split())

num = list(range(1, N +1))
answer = []
a = []
i = K
length = N
count = 0

while len(a) != N:
    if i > len(num):
        i = i - length
        
        for j in range(len(answer)):
            a.append(num.pop(answer[j] - count))
            count += 1

        length = len(num)
        answer.clear()
        count = 0
        
    else:
        answer.append(i - 1)
        i += K
        
print('<', end='')
for i in range(len(a)):
    if i == len(a)-1:
        print(a[i], end='')
    else:
        print(a[i], end=', ')
print('>')