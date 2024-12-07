

#
# def printf(arr):
#     for _ in range(len(arr)):
#         print(arr[_])
#
#     print("* * * * * * * *")
#
# def update_world(arr, src):
#     while len(src)>0:
#         row,col = src.pop()
#         arr[row][col] = 1
#     return arr
#

import sys
def my_function(i):
    if 'A'<=i<='Z':
        return str(i)
    else: return int(i)

# input = sys.stdin.readline
#
# N = int(input())
#
# world = [[0 for _ in range(N)]for _ in range(N)]
# world[0][0] = 1 #snake
#
# K = int(input())
#
# apple = [list(map(lambda x: int(x)-1, input().split()))for _ in range(K)]
# for i in range(K):
#     world[apple[i][0]][apple[i][1]] = -1 # apple mapping
#
# nworld = [x[:] for x in world]
#
# L = int(input())
#
# cmd = [list(map(my_function, input().split())) for _ in range(L)]
# cmd.sort()
#
# print(cmd)
# # just snake game
#
# # TODO : 뱀이 늘어나는 조건 = 사과를 먹음 (근데, 사과 먹으면 꼬리가 그대로있는거로 늘어난걸 표현)
# #  즉, 이동한 위치에 사과가 없으면 꼬리가 이동함
# printf(world)
# Flag = True
# iter_time = 0
# # TODO : direction flag
# #  E : 0
# #  S : 1
# #  W : 2
# #  N : 3
#
# direction = 0
# snake = [[0,0]]
# 뱀 게임 수정된 코드
def turn_dir(direction, cmd):
    if cmd == 'L':
        return (direction + 3) % 4
    else:
        return (direction + 1) % 4

def print_map(world):
    for row in world:
        print(row)
    print("*" * 10)

def solution():
    N = int(input())
    world = [[0] * N for _ in range(N)]
    K = int(input())
    apple = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]
    for x, y in apple:
        world[x][y] = -1  # 사과 위치 설정

    L = int(input())
    cmd = [list(input().split()) for _ in range(L)]
    cmd = [[int(x), c] for x, c in cmd]

    snake = [[0, 0]]
    world[0][0] = 1  # 뱀의 초기 위치

    dx = [0, 1, 0, -1]  # 동, 남, 서, 북
    dy = [1, 0, -1, 0]

    direction = 0  # 초기 방향 (동쪽)
    time = 0
    cmd_index = 0

    while True:
        time += 1
        head_x, head_y = snake[-1]
        nx, ny = head_x + dx[direction], head_y + dy[direction]

        # 벽 또는 자기 몸과 부딪히는 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= N or world[nx][ny] == 1:
            break

        if world[nx][ny] == -1:  # 사과를 먹으면
            snake.append([nx, ny])
            world[nx][ny] = 1
        else:  # 사과가 없으면
            snake.append([nx, ny])
            world[nx][ny] = 1
            tail_x, tail_y = snake.pop(0)
            world[tail_x][tail_y] = 0

        # 방향 전환
        if cmd_index < len(cmd) and cmd[cmd_index][0] == time:
            direction = turn_dir(direction, cmd[cmd_index][1])
            cmd_index += 1
        print_map(world)
    return time

print(solution())
# '''
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D
# '''
# def turn_dir(dir, c): # 회전시키는 함수
#     if c == 'L':
#         return (dir + 3) % 4
#     else:
#         return (dir + 1) % 4
#
# def print_map(map): # 맵 확인용
#     for i in range(len(map)):
#         print(map[i])
#
# def solution():
#
#     n = int(input())
#     maps = [[0] * (n + 1) for _ in range(n + 1)] # n + 1크기의 배열 생성
#
#     k = int(input())
#     # 사과 2
#     # 뱀위치 1
#     for _ in range(k):  # 맵에 사과 위치 2로 지정
#         x, y = map(int ,input().split())
#         maps[x][y] = 2
#
#     l = int(input())
#     turn = [] # (시간, 회전) 리스트
#     for _ in range(l):
#         x, c = input().split()
#         turn.append([int(x), c])
#
#     x, y = 1, 1  # 뱀의 첫위치
#     maps[x][y] = 1
#
#     dx =[0, 1, 0, -1]  #상하좌우 방향
#     dy =[1, 0, -1, 0]
#
#     dir = 0 # 처음은 오른쪽
#     time = 0 # 시간
#     turn_index = 0 # 회전
#
#     snake_index = [[x,y]] # 뱀의 위치 저장
#     while True:
#         x += dx[dir]  # 1칸이동
#         y += dy[dir]
#         if x <= n and y <= n and x >=1 and y >= 1 and maps[x][y] != 1: # 벽이나 몸에 안부딪힌 경우
#             if maps[x][y] != 2: # 사과없음
#                 px, py = snake_index.pop(0)  # 꼬리 한칸이동
#                 maps[px][py] = 0
#             maps[x][y] = 1
#             snake_index.append([x,y]) # 어차피 머리는 움직이니까 머리는 뱀 위치에 추가
#         else:
#             time += 1
#             break
#         time += 1
#         # 여기서 회전
#         if turn_index < l and turn[turn_index][0] == time:
#             dir = turn_dir(dir, turn[turn_index][1])
#             turn_index += 1
#     return time
#
# print(solution())