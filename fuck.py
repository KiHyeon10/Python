a = int(input("촐생 년도: "))2020

age = 2022 - a + 1

if(age >= 20 and age <= 26):
    print("대학생")
elif(age >= 17 and age <20):
    print("고등학생")
elif(age< 17 and age >= 14):
    print("중학생")
elif(age < 14 and age >= 8):
    print("초등학생")
else:
    print("학생이 아닙니다")
