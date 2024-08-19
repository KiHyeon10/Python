import sys
import re

input = sys.stdin.readline

Math = input().split('-')

flag = 0
a = 0

for i in Math:
    sum = 0
    plus = i.split('+')
    for j in plus:
        sum += int(j)

    if flag == 0:
        a += sum
        flag = 1
    else:
        a -= sum

print(a)