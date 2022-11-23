import sys

input = sys.stdin.readline

n = int(input())
coin = [2, 5]
count = 0

while n%5 != 0:
    n -= 2
    count += 1
    if n < -1:
        print(-1)
        break;
    else:
        continue;
if n%5 == 0:
    count += n//5
    print(count)