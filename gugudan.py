while(1):
    a = int(input("몇 단: "))
    if(a <= 1 or a >= 10):
        print("잘못된 입력 값")
    else:
        print("구구단", a, "을 계산한다")

        for i in range(1, 10):
            print(a, "*", i, "=", a*i)
