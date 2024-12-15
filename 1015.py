import sys
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))
ans = [0] * len(num)
count = len(num)-1

while count != -1:
    step = [i for i, x in enumerate(num) if x == max(num)]

    if len(step) != 0:
        for i in range(len(step)-1, -1, -1):
            ans[step[i]] = count
            count -= 1
            num[step[i]] = -1

print(*ans, sep=' ')