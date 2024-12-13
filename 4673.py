num = [True] * 10001

for i in range(1, len(num)):
    n = [int(digit) for digit in str(i)]
    Self_num = i + sum(n)
    
    if Self_num <= 10000:
        num[Self_num] = False

for i in range(1, len(num)):
    if num[i] == True:
        print(i)