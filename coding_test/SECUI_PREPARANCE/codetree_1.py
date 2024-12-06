import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
y, x, d = map(int, input().split())

# 지도 입력
world = [list(map(int, input().split())) for _ in range(n)]

# 현재 위치 방문 표시
world[y][x] = 2

# 방향 벡터 (북, 동, 남, 서)
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def find_forward(world, x, y, d):
    """왼쪽으로 돌면서 이동할 수 있는 방향 찾기"""
    for _ in range(4):  # 네 방향 확인
        d = (d + 3) % 4  # 왼쪽으로 회전
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < n and 0 <= nx < m and world[ny][nx] == 0:  # 이동 가능
            return ny, nx, d, True  # 이동 위치와 방향 반환
    return y, x, d, False  # 이동 불가

def find_backward(world, x, y, d):
    """뒤로 이동 가능한지 확인"""
    b = (d + 2) % 4  # 뒤로 가는 방향 계산
    ny, nx = y + dy[b], x + dx[b]
    if 0 <= ny < n and 0 <= nx < m and world[ny][nx] != 1:  # 이동 가능
        return ny, nx, d, True
    return y, x, d, False  # 이동 불가

cur_x, cur_y = x, y

while True:
    moved = False
    # 앞으로 이동 시도
    cur_y, cur_x, d, moved = find_forward(world, cur_x, cur_y, d)
    if moved:  # 이동 가능
        world[cur_y][cur_x] = 2  # 방문 표시
        continue
    # 후진 시도
    cur_y, cur_x, d, moved = find_backward(world, cur_x, cur_y, d)
    if not moved:  # 후진도 불가능하면 종료
        break

# 방문한 칸 수 계산
visited_count = sum(row.count(2) for row in world)

# 출력
for row in world:
    print(' '.join(map(str, row)))
print(visited_count)
