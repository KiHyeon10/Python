import sys

input = sys.stdin.readline

def Sosu(N, K):
    num = [True] * (N + 1)
    num[0] = num[1] = False  # 0과 1은 소수가 아님
    count = 0
    
    for i in range(2, N + 1):
        if num[i]:
            for j in range(i, N + 1, i):
                if num[j]:
                    num[j] = False
                    count += 1
                    if count == K:
                        return j

N, K = map(int, input().split())
answer = Sosu(N, K)
print(answer)
