import random
target = random.randint(1, 100)

while(True):
    i = int(input())
    if(i == target):
        print("hehehehehehe")
        break
    elif(i > target):
        print("down")
    else:
        print("up")
