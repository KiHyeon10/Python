import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = []
for i in range(N):
    a = input().rstrip()
    num.append([int(digit) for digit in str(a)])

Max = 1

for i in range(N):
    for j in range(M):
        for z in range(M-1, j, -1):

            if num[i][j] == num[i][z]:
                same = num[i][j]

                if z-j > N-1 or i+z-j > N-1:
                    continue

                if num[i+z-j][j] == same and num[i+z-j][z] == same:
                    Max = max(Max, z-j+1)

print(Max*Max)