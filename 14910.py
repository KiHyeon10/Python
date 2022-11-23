a = list(map(int, input().split()))
i = sorted(a)

if a == i:
    print("Good")
else:
    print("Bad")