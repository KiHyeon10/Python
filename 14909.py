a = list(map(int, input().split()))
j = 0
for i in a:
    if i > 0:
        j += 1
    else:
        continue
    
print(j)