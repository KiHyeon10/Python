import sys

input = sys.stdin.readline

N = int(input())

def Find(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    
    num = [0] * (n + 1)  # n+1 크기의 리스트 생성
    num[1] = 1
    num[2] = 3
    
    for i in range(3, n + 1):
        num[i] = (num[i-1] + num[i-2] + num[i-2]) % 10007  # 모듈로 연산을 반복문 내부에서 적용
    
    return num[n]

print(Find(N))
