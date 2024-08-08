import sys

input = sys.stdin.readline

answer = []

while True:
    N = input().rstrip()
    if N == '0':
        break
    Rev_N = N[::-1]
    if Rev_N == N:
        answer.append('yes')
    else:
        answer.append('no')

print(*answer,sep='\n')