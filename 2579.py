import sys

input = sys.stdin.readline

T = int(input())
Stairs = []

for _ in range(T):
    Stairs.append(int(input()))

i = T - 1
score = Stairs[i]
flag1 = 0

while i != 0:
    if i - 2 < 0:
        if flag1 < 1:
            i -= 1
            score += Stairs[i]
        break

    elif Stairs[i-1] > Stairs[i-2] and flag1 < 1:
        i -= 1
        score += Stairs[i]
        flag1 = 1

    elif Stairs[i-1] < Stairs[i-2] or flag1 > 1:
        i -= 2
        score += Stairs[i]
        flag1 = 0

print(score)