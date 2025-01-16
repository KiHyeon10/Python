import sys
input = sys.stdin.readline

N = input().rstrip()
count = 0

for i in range(1, int(N)+1):
    num = [int(digit) for digit in str(i)]

    if len(num) == 1:
        count += 1
    
    else:
        a = num[1] - num[0]
        flag = 0

        for i in range(2, len(num)):
            if num[i] != num[i-1] + a:
                flag = 1
                break
        
        if flag == 0:
            count += 1

print(count)