T = int(input())

for _ in range(T):
    A, B, N = map(int, input().split())
    count = 0

    while max(A, B) <= N:
        if A >= B:
            B += A
        elif A < B:
            A += B
        count += 1

    print(count)