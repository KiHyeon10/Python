import sys
input = sys.stdin.readline

K, S, T = input().split()
T = int(T)

def to_coord(pos):
    return [ord(pos[0]) - ord('A'), int(pos[1]) - 1]

def to_pos(coord):
    return chr(coord[0] + ord('A')) + str(coord[1] + 1)

King = to_coord(K)
Stone = to_coord(S)

directions = {
    'R': (1, 0), 'L': (-1, 0), 'T': (0, 1), 'B': (0, -1),
    'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)
}

for _ in range(T):
    command = input().strip()
    if command not in directions:
        continue

    dx, dy = directions[command]
    new_king = [King[0] + dx, King[1] + dy]

    if not (0 <= new_king[0] < 8 and 0 <= new_king[1] < 8):
        continue

    if new_king == Stone:
        new_stone = [Stone[0] + dx, Stone[1] + dy]
        if not (0 <= new_stone[0] < 8 and 0 <= new_stone[1] < 8):
            continue
        Stone = new_stone

    King = new_king

print(to_pos(King))
print(to_pos(Stone))
