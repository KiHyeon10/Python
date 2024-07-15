import sys
from collections import Counter

input = sys.stdin.readline

Sen = input().strip()
Sen = Sen.upper()

counter = Counter(Sen)

max_val = max(counter.values())

max_values = [val for val, freq in counter.items() if freq == max_val]

if len(max_values) != 1:
    print('?')
else:
    print(max_values[0])