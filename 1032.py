import sys

input = sys.stdin.readline

N = int(input())

if N == 1:
    answer = input().strip()
    print(answer)
else:
    s1 = list(input().strip())
    for i in range(1, N):
        s2 = list(input().strip())
        for j in range(0, len(s1)):
            if s1[j] != s2[j]:
                s1[j] = '?'
                
    print(''.join(s1))