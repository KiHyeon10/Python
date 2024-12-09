import sys
input = sys.stdin.readline

T = int(input())
count = 0

for _ in range(T):
    sen = list(input().strip())
    ans = []
    ans.append(sen[0])
    i = 1
    flag = 0

    if len(sen) != 1:
        while i != len(sen):
            if sen[i] not in ans:
                ans.append(sen[i])
            else:
                if sen[i-1] != sen[i]:
                    flag = 1
                    break
            i+= 1

    if flag == 0 or len(sen) == 1:
        count += 1

print(count)