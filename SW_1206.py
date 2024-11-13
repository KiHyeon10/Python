for t in range(10):
    T = int(input())

    build = list(map(int, input().split()))

    count = 0
    for i in range(2, len(build)-2):
        Max = max(max(build[i-2:i]), max(build[i+1:i+3]))
        if build[i] > Max:
            count += build[i] - Max

    print("#{0} {1}".format(t+1, count))