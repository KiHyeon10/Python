import sys

input = sys.stdin.readline

N = int(input())

answer = [0] * 10

count = 1
start = 1

def cal(x, answer, count):
    while x > 0:
        answer[x % 10] += count
        x //= 10

while start <= N:
    while N % 10 != 9:
        cal(N, answer, count)
        N -= 1
    if N < start:
        break
    while start % 10 != 0:
        cal(start, answer, count)
        start += 1
    start //= 10
    N //= 10
    for i in range(10):
        answer[i] += (N - start + 1) * count
    count *= 10

for i in range(10):
    print(answer[i], end= ' ')