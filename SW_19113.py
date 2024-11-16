TC = int(input())

for t in range(TC):
    N = int(input())
    num = list(map(int, input().split()))
    answer = []
    i = 0
    
    while True:
        if i > len(num) or len(num) == 0:
            break

        if num[i] * 0.75 in num and num[i] % 4 == 0:
            answer.append(int(num[i]*0.75))
            a = num[i]
            num.pop(i)
            num.remove(a*0.75)
            if i != 0:
                i -= 1
        else:
            i += 1

    print("#{0} ".format(t+1), end='')
    print(*answer, sep=' ')