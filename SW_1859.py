import sys

input = sys.stdin.readline

T = int(input())


for t in range(T):
    N = int(input())
    num = list(map(int, input().split()))

    cal = [0] * N
    cal[-1] = num[-1]

    for i in range(N-2, -1, -1):
        cal[i] = max(num[i], cal[i+1])

    count = 0
    for i in range(N):
        count += cal[i] - num[i]

    print("#{0} {1}" .format(t+1, count))