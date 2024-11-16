T = int(input())

for _ in range(T):
     N, P = map(int, input().split())
     sum = 0
     B = 1

     for i in range(1, N+1):
         sum += i
         if sum == P:
             sum -= B
             B += 1
     print(sum)