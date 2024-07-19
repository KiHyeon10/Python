N = int(input())
count = 0
In, Out = dict(), []
for i in range(0, 2 * N):
    if i < N:
        car = input().strip()
        In[car] = i
    else:
        car = input().strip()
        Out.append(car)
 
for i in range(N-1):
	for j in range(i+1, N):
		if In[Out[i]] > In[Out[j]]:
			count += 1
			break

print(count)