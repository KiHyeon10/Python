import sys

input = sys.stdin.readline

N = int(input())
Card_N = list(map(int, input().split()))
M = int(input())
Card_M = list(map(int, input().split()))

answer = {}

for i in Card_N:
  if i in answer:
    answer[i] += 1
  else:
    answer[i] = 1

for m in Card_M:
  if m in answer:
    print(answer[m], end=' ')
  else:
     print(0, end=' ')