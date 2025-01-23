import sys
input = sys.stdin.readline

L, R = map(int, input().split())

count = 0

str_L = str(L)
str_R = str(R)

if len(str_L) != len(str_R):
    print(0)
else:
    for l_digit, r_digit in zip(str_L, str_R):
        if l_digit == r_digit and l_digit == '8':
            count += 1
        elif l_digit != r_digit:
            break

    print(count)
