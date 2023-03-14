meeting = int(input())

meet = [0] * meeting
time = []

for i in range(meeting):
    a, b = map(int, input().split())
    time.append([a, b])
    
time = sorted(time, key=lambda x:(x[1], x[0]))

vit = 1
end_time = time[0][1]
for i in range(1, meeting) :
    if time[i][0] >= end_time :
        vit += 1
        end_time = time[i][1]

print(vit)