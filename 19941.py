import sys

input = sys.stdin.readline

N, K = map(int, input().split())

Ham = list(input().rstrip())
count = 0

for i in range(N):
    if Ham[i] == 'P':
        for j in range(max(i-K, 0), min(i+K+1, N)):
            if Ham[j] == 'H':
                Ham[j] = 1
                count += 1
                break
print(count)