import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = []
answer = []
count = 0

for i in range(N):
    n = [int(digit) for digit in str(input().rstrip())]
    num.append(n)

for i in range(N):
    n = [int(digit) for digit in str(input().rstrip())]
    answer.append(n)

if N < 3 or M < 3:
    if num != answer:
        count = -1
else:
    for i in range(N):
        for j in range(M):
            if num[i][j] == answer[i][j]:
                continue
            else:
                if N - i > 2 and M - j > 2:
                    for a in range(i, i+3):
                        for b in range(j, j+3):
                            num[a][b] ^= 1
                    count += 1
                else:
                    count = -1
                    break
        if count == -1:
            break

print(count)