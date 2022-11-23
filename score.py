kor = [ 49, 79, 20, 100, 80]
math = [ 43, 59, 85, 30, 90]
eng= [ 49, 79, 48, 60, 100]

sum = [kor, math, eng]

for looper in range(0, len(sum)) :
    a = 0
    for j in range(0, len(sum[looper])):
        a += sum[looper][j]
    
    print(a)

