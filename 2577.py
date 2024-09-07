import sys

input = sys.stdin.readline

num = [0] * 10

A = int(input())
B = int(input())
C = int(input())

sum = list(str(A*B*C))

for i in range(len(sum)):
    num[int(sum[i])] += 1

print(*num,sep='\n')