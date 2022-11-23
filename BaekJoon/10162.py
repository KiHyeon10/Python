i = int(input())
a = [0, 0, 0]
time = [300, 60, 10]
if i % 10 == 0:
    for j in range (len(time)):
       a[j] = i//time[j]
       i %= time[j]
    print(a[0], a[1], a[2])

else:
    print(-1)
