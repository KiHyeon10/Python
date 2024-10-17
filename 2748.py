import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

fibo = [0] * (n+1)

def find(n):
    if fibo[n] != 0:
        return fibo[n]
    elif n == 0:
        return 0
    else:
        if n == 1 or n == 2:
            fibo[n] = 1
        else:
            fibo[n] = find(n-1) + find(n-2)
        return fibo[n]

print(find(n))