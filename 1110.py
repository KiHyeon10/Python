import sys

input = sys.stdin.readline

N = input().strip()

Cycle_num = 0
count = 0

num = [0] * 2
num[0] = int(N) // 10
num[1] = int(N) % 10

while int(N) != Cycle_num:
    if (num[0] + num[1]) >= 10:
        Cycle_num = (num[1]) * 10 + (num[0] + num[1] - 10)
    else:
        Cycle_num = (num[1] * 10) + (num[0] + num[1])
    
    num[0] = Cycle_num // 10
    num[1] = Cycle_num % 10
    if len(num) != 2:
        tmp = num[0]
        num[0] = 0
        num[1] = tmp
    count += 1

if count == 0:
    count += 1

print(count)