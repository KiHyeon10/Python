a = list(map(int, input().split()))
j = 0
if len(a) == 1:
        print("Good")
        exit()
else:
   while j != len(a) -1 :
       if a[j] <= a[j +1]:
           j += 1
       else:
           print("Bad")
           exit()
           
    print("good")