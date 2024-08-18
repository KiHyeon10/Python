import sys

input = sys.stdin.readline

sen = list(input().rstrip())

for i in range(len(sen)):
    sen_num = ord(sen[i])
    
    if sen_num > 64 and sen_num < 91:
        sen_num += 13
 
        if sen_num> 90:
            sen_num = 64 + (sen_num - 90)

        print(chr(sen_num), end='')
        
    elif sen_num > 96 and sen_num < 123:
        sen_num += 13
        
        if sen_num > 122:
            sen_num = 96 + (sen_num - 122)

        print(chr(sen_num), end='')

    else:
        print(sen[i],end='')