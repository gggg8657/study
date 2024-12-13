import sys

def printf(arr):
    for _ in range(len(arr)):
        print(arr[_])
    print("* * * * * * * *")

def update_world(arr, src):
    while len(src) > 0:
        row, col = src.pop()
        arr[row][col] = 1
    return arr

def my_function(i):
    if 'A' <= i <= 'Z':
        return str(i)
    else:
        return int(i)


input = sys.stdin.readline

N = int(input())

world = [[0 for _ in range(N)] for _ in range(N)]
world[0][0] = 1  # snake

K = int(input())

apple = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]
for i in range(K):
    world[apple[i][0]][apple[i][1]] = -1  # apple mapping

nworld = [x[:] for x in world]

L = int(input())

cmd = [list(map(my_function, input().split())) for _ in range(L)]
cmd.sort()

# print(cmd)

Flag = True
iter_time = 0

# 방향 플래그
# E : 0
# S : 1
# W : 2
# N : 3

direction = 0
snake = [[0, 0]]

while Flag:
    iter_time += 1
    head_row, head_col = snake[-1]
    cmd_turn=0
    # 방향에 따라 이동
    if direction == 0:  # East
        nrow, ncol = head_row, head_col + 1
    elif direction == 1:  # South
        nrow, ncol = head_row + 1, head_col
    elif direction == 2:  # West
        nrow, ncol = head_row, head_col - 1
    else:  # North
        nrow, ncol = head_row - 1, head_col

    # 벽 충돌 체크
    if nrow < 0 or nrow >= N or ncol < 0 or ncol >= N:
        Flag = False
        break

    # 자기 자신과 충돌 체크
    if world[nrow][ncol] == 1:
        Flag = False
        break

    # 사과를 먹으면
    if world[nrow][ncol] == -1:
        snake.append([nrow, ncol])
        world[nrow][ncol] = 1
    else:  # 사과가 없으면 꼬리 제거
        snake.append([nrow, ncol])
        world[nrow][ncol] = 1
        tail_row, tail_col = snake.pop(0)
        world[tail_row][tail_col] = 0

    # 방향 전환 처리
    if len(cmd) > 0 and iter_time == cmd[cmd_turn][0]:
        _, turn = cmd.pop(0)
        if turn == 'D':  # 오른쪽 회전
            direction = (direction + 1) % 4
        elif turn == 'L':  # 왼쪽 회전
            direction = (direction - 1) % 4
        cmd_turn+=1

print(iter_time)