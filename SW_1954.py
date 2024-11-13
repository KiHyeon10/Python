T = int(input())

def Find(num):
    return any(0 in row for row in num)

for t in range(T):
    N = int(input())
    num = [[0 for _ in range(N)] for _ in range(N)]
    count = 1

    for i in range(N):
        num[0][i] = count
        count += 1

    i = 0
    j = N-1
    start = 1
    while Find(num):
        if start == 4 and j != N-1 and num[i][j+1] == 0:
            j += 1
            num[i][j] = count
            count += 1
            if j == N-1 or num[i][j+1] != 0:
                start = 1

        elif start == 1 and i != N-1 and num[i+1][j] == 0:
            i += 1
            num[i][j] = count
            count += 1
            if i == N-1 or num[i+1][j] != 0:
                start = 2

        elif start == 2 and j != 0 and num[i][j-1] == 0:
            j -= 1
            num[i][j] = count
            count += 1
            if j == 0 or num[i][j-1] != 0:
                start = 3

        elif start == 3 and num[i-1][j] == 0:
            i -= 1
            num[i][j] = count
            count += 1
            if i == 0 or num[i-1][j] != 0:
                start = 4

    print("#{0}".format(t+1))
    for a in range(N):
        for b in range(N):
            print(num[a][b], end=' ')
        print()