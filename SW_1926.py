T = int(input())

for i in range(1, T+1):
    num = [int(digit) for digit in str(i)]
    if any(x in num for x in [3, 6, 9]):
        count = 0
        for n in range(len(num)):
            if num[n] % 3 == 0 and num[n] != 0:
                count += 1
        answer = ['-'] * count
        print(*answer, sep='', end=' ')
    else:
        print(i,  end=' ')