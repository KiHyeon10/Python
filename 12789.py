import sys

input = sys.stdin.readline

N = int(input())

Student = list(map(int, input().split()))

Stack = []
Stack.append(Student.pop(0))
i = 1

while len(Student) != 0 or len(Stack) != 0:
    if len(Stack) != 0 and Stack[len(Stack) - 1] == i:
        Stack.pop()
        i += 1
    else:
        if len(Student) != 0 and Student[0] == i:
            Student.pop(0)
            i += 1
        elif len(Student) != 0:
            Stack.append(Student.pop(0))
        else:
            break
    
if len(Student) != 0 or len(Stack) != 0:
    print('Sad')
else:
    print('Nice')