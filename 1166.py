import sys
input = sys.stdin.readline

N, L, W, H = map(int, input().split())

Start, End = 0, min(L, W, H)

while End - Start > 1e-9:
    num = (End + Start) / 2

    count = int(L / num) * int(W / num) * int(H / num)

    if count >= N:
        Start = num
    else:
        End = num

print(f"{End:.9f}")