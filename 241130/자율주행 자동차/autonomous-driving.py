# 갈 수 있는 길 확인 (왼쪽으로 돌리기)
# 진행 (칸 이동)
# 갈 수 있는 길 없으면 초기에서 후진

# 뒤가 인도면 못감
# 앞이 가본길이면 못감
# 안가본 길=0
# 인도 = 1
# 방문한 길 =2
# 뒷방향은 어딘지 알아놓기


import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())

x, y, d = map(int, input().split())

b = abs(d + 2 - 4)

world = [list(map(int, input().split())) for _ in range(n)]

world[y][x] = 2
def find_forward(world, x, y, d):
    #print(d)
    if d == 0:
        dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
    elif d == 1:
        dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
    elif d == 2:
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    elif d == 3:
        dy, dx = [1, 0, -1, 0], [0, -1, 0, 1]
    else : dy,dx = [0,0,-1,1],[-1,1,0,0]
    for _ in range(4):
        ny, nx = y + dy[_], x + dx[_]
        #print(f"i is {_} x | {ny}, y | {nx}")
        if 0 <= ny < n and 0 <= nx < m and world[ny][nx] == 0:
            #print(f"x | {ny}, y | {nx} world | {world[ny][nx]}")
            world[ny][nx]=2
            return ny, nx
    return -1, -1


def move_forward(world, x, y):
    world[y][x] = 2
    return world


def find_backward(world, x, y, b):
    if b == 0:
        ny = y - 1
        nx = x
    elif b == 1:
        ny = y
        nx = x - 1
    elif b == 2:
        ny = y + 1
        nx = x
    elif b == 3:
        ny = y
        nx = x - 1
    else:
        ny = y
        nx = x
    if 0 <= ny < n and 0 <= nx < m and world[ny][nx] != 1:
        return ny, nx
    else:
        return -2, -2


def move_backward(world, x, y):
    world[y][x] = 2
    return world


def check_end(x, y):
    if x == -2:
        cnt = 0
        cnt = sum(row.count(2) for row in world)
        print(cnt)
        return 9


cur_x, cur_y = x, y


def print_world(world):
    for _ in range(n):
        print(world[_])
    print("*************")


while True:
    # print_world(world)
    # print(f"x : {cur_y}, y:{cur_x}")
    if check_end(cur_x, cur_y) == 9:
        break
    cur_y, cur_x = find_forward(world, cur_x, cur_y, d)
    # print(f"x : {cur_y}, y:{cur_x}")
    if cur_x == -1:
        cur_y, cur_x = find_backward(world, cur_x, cur_y, b)
        # print(f"x : {cur_y}, y:{cur_x}")
        world = move_backward(world, cur_x, cur_y)
        # print_world(world)
    else:
        world = move_forward(world, x, y)
        # print_world(world)
