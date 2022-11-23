j = int(input())
i = 1000 - j
money = 0
while i >= 1 and i < 1000:
    if i >= 500:
        i = i -500
        money += 1
    elif i >= 100:
        i = i - 100
        money += 1
    elif i >= 50:
        i = i-50
        money += 1
    elif i >= 10:
        i = i-10
        money += 1
    elif i >=5:
        i = i-5
        money += 1
    else:
        money += i
        i = 0

print(money)