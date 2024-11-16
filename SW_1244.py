T = int(input())

def Find(num, start):
    Max = start
    for i in range(len(num)-1, start, -1):
        if num[i] == max(num):
            return i
        elif num[Max] < num[i]:
            Max = i

    return Max

for t in range(T):
    num_input, Change_input = input().split()
    Change = int(Change_input)
    num = [int(digit) for digit in num_input]

    count = 0
    i = 0

    while count != Change:
        Max = Find(num, i)

        if Max == i and Max > len(num)-3:
            if num[Max] != max(num):
                if i == len(num)-1:
                    num[i], num[Max-1] = num[Max-1], num[i]
                elif i == len(num)-2:
                    num[i], num[Max+1] = num[Max + 1], num[i]
            count += 1

        elif num[i] <= num[Max] and i != Max:
            num[i], num[Max] = num[Max], num[i]
            count += 1

        if i < len(num)-1:
            i += 1

    print("#{0}".format(t+1), end=' ')
    print(*num, sep='')