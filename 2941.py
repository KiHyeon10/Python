import sys
input = sys.stdin.readline

sen = list(input().rstrip())
values = ['-', '=', 'j']
ans = [True] * (len(sen) - 1)

count = len(sen)
find = [i for i, x in enumerate(sen) if x in values]

for i in range(len(find)):
    if sen[find[i]] == '=':
        if sen[find[i]-1] == 'z' and sen[find[i]-2] == 'd':
            count -= 2
        else:
            count -= 1

    elif sen[find[i]] == 'j':
        if sen[find[i] - 1] == 'l' or sen[find[i] - 1] == 'n':
            count -= 1
    
    else:
        count -= 1

print(count)