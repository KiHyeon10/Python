import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    clothes = {}
    for i in range(n):
        product, C = input().split()
        if C in clothes:
            clothes[C].append(product)
        else:
            clothes[C] = [product]

    sum = 1
    for i in clothes.keys():
        sum *= len(clothes[i]) + 1
    print(sum-1)