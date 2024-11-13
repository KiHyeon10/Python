T = int(input())

for i in range(T):
    num = list(map(int, input().split()))

    print("#{0} {1}".format(i+1, round(sum(num)/10)))

