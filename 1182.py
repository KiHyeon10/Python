import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))
All = []

def Find(n, index=0, sum=0, s=[]):
    if index == len(n):
        s.append(sum)
        return

    Find(n, index + 1, sum + n[index], s)
    Find(n, index + 1, sum, s)
    return s

All = Find(num)
All.sort()
print(All)
count = 0

for i in range(len(All)):
    if All[i] > S:
        break
    elif All[i] == S:
        count += 1

if S == 0:
    print(count - 1)
else:
    print(count)