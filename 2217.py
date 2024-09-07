import sys

input = sys.stdin.readline

N = int(input())

rope = []

for _ in range(N):
    num = int(input())
    rope.append(num)

count = 1
Max = min(rope) * N
sum = 0
rope.sort()

for i in range(N-1, -1, -1):
    sum = rope[i] * count
    
    if sum > Max:
        Max = sum
        count += 1
    else:
        break

print(Max)