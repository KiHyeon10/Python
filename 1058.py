import sys
input = sys.stdin.readline

N = int(input().strip())
Friend = [input().strip() for _ in range(N)]

Max = 0

for i in range(N):
    two_friends = set()

    for j in range(N):
        if Friend[i][j] == 'Y':
            two_friends.add(j)
            for k in range(N):
                if Friend[j][k] == 'Y' and k != i:
                    two_friends.add(k)

    Max = max(Max, len(two_friends))

print(Max)
