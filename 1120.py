import sys
input = sys.stdin.readline

A, B = input().split()
ans = len(B)

for i in range(len(B) - len(A) + 1):
    sub_B = B[i:i + len(A)]

    count = sum(1 for a, b in zip(A, sub_B) if a != b)
    ans = min(ans, count)

print(ans)
