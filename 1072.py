import sys
input = sys.stdin.readline

def Find(X, Y):
    Z = (Y * 100) // X

    if Z >= 99:
        return -1
    
    left, right = 0, 10**9
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        new_rate = ((Y + mid) * 100) // (X + mid)
        
        if new_rate > Z:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result

for line in sys.stdin:
    X, Y = map(int, line.split())
    print(Find(X, Y))
