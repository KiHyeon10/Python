import sys

input = sys.stdin.readline

H, W = map(int, input().split())
Wall = list(map(int, input().split()))

if max(Wall) == 0:
    print(0)
    sys.exit()

# 왼쪽과 오른쪽에서의 최대 높이를 저장할 배열
left_max = [0] * W
right_max = [0] * W

# 왼쪽에서의 최대 높이 계산
left_max[0] = Wall[0]
for i in range(1, W):
    left_max[i] = max(left_max[i - 1], Wall[i])

# 오른쪽에서의 최대 높이 계산
right_max[W - 1] = Wall[W - 1]
for i in range(W - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], Wall[i])

# 고이는 빗물의 총량 계산
total_water = 0
for i in range(W):
    water_level = min(left_max[i], right_max[i])
    if water_level > Wall[i]:
        total_water += water_level - Wall[i]

print(total_water)
