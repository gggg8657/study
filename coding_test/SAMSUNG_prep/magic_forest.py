def print_world(arr):
    print(" * * * CURRENT WORLD * * * \n")
    for _ in range(len(arr)):
        print(arr[_])


from collections import deque


# print(world)
# if r_i 골렘이 아래로 더 갈 수 있다? :
# 1. 정령이 행 - 1 위치가 아님
# 2. 아래에 겹치는 골렘이 없음
# 3. 사각형이니까, 지도에 의해 못가진 않음

def check_down(r_i, c_i):
    if r_i != r - 2:  # 마지막 행에 도착한게 아니면
        # 골렘 체크
        if world[r_i + 1][c_i - 1] == 0 and world[r_i + 1][c_i + 1] == 0 and world[r_i + 2][c_i] == 0:
            # 내려가도 됨
            return 1
        else:
            return 2  # 마지막 행 아닌데, 내려갈 수 없음 -> 아래에 골렘 있음
    else:
        return 0


dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def check_left(r_i, c_i):
    if c_i >= 0 and c_i - 2 >= 0:
        if world[r_i][c_i - 2] == 0 and world[r_i + 1][c_i - 1] == 0:
            left = check_down(r_i, c_i - 1)
        else:
            left = 2
    else:
        left = 0
    return left  # 1 왼쪽 아래 가능, 0 왼쪽 불가능, 2 왼쪽 아래가 불가능


def check_right(r_i, c_i):
    right = 0
    if c_i < c - 2 and c_i + 2 < c and c_i + 2 < c and r_i + 2 < r:
        if world[r_i][c_i + 2] == 0 and world[r_i + 1][c_i + 1] == 0:
            if world[r_i + 1][c_i + 2] == 0 and world[r_i + 2][c_i + 1] == 0:
                right = 1
        else:
            right = 2
    else:
        right = 0
    return right  # 1 오른쪽 아래 가능, 0 오른쪽 불가능, 2 오른쪽 아래가 불가능


def direction(r_i, c_i, d_i):
    if d_i == 0:
        isDoor[r_i - 1][c_i] = True
    elif d_i == 1:
        isDoor[r_i][c_i + 1] = True
    elif d_i == 2:
        isDoor[r_i + 1][c_i] = True
    else:
        isDoor[r_i][c_i - 1] = True


def inRange(y, x):
    return 0 <= y < r and 0 <= x < c


def bfs(y, x):
    result = y
    q = deque([(y, x)])
    visit = [[False] * c for _ in range(r)]
    visit[y][x] = True
    while q:
        cur_y, cur_x = q.popleft()
        for k in range(4):
            ny, nx = cur_y + dy[k], cur_x + dx[k]
            if inRange(ny, nx) and not visit[ny][nx] and (world[ny][nx] == world[cur_y][cur_x] or (isDoor[cur_y][cur_x] == True and world[ny][nx]!=0)):
                q.append((ny, nx))
                visit[ny][nx] = True
                result = max(result, ny)
    return result


queue = deque()
r, c, k = map(int, input().split())
r += 3
world = [[0 for _ in range(c)] for _ in range(r)]
isDoor = [[False for _ in range(c)] for _ in range(r)]

for _ in range(k):
    r_tmp = 0
    c_tmp, d_tmp = map(int, input().split())
    queue.append([r_tmp, c_tmp - 1, d_tmp])


visited = [[False for _ in range(c)] for _ in range(r)]

answer = 0
iter = 0
while queue:
    iter -= 1
    r_i, c_i, d_i = queue.popleft()
    while True:
        down = check_down(r_i, c_i)
        left = check_left(r_i, c_i)
        right = check_right(r_i, c_i)
        if down == 1:
            r_i, c_i = r_i + 1, c_i  # move down
            # print("moved");
            continue
        elif left == 1:
            r_i, c_i = r_i, c_i - 1  # move left
            # print("moved left");
            r_i, c_i = r_i + 1, c_i  # move down
            # print("moved down")
            d_i = (d_i - 1) % 4
            # print("rotate to left")
            continue
        elif right == 1:
            r_i, c_i = r_i, c_i + 1
            # print("moved right")
            r_i, c_i = r_i + 1, c_i  # move down
            # print("moved down")
            d_i = (d_i + 1) % 4;
            # print("rotate to right")
            continue
        elif r_i <= 3 and left != 1 and right != 1 and down != 1:
            # reset world
            # print("nothing to move clear world")
            world = [[0 for _ in range(c)] for _ in range(r)]
            isDoor = [[False for _ in range(c)] for _ in range(r)]
            break
        else:
            # 골렘이 도착한 위치에 사각형을 그린다
            world[r_i][c_i] = iter
            for _ in range(4):
                nx, ny = r_i + dx[_], c_i + dy[_]
                if nx < 0 or ny < 0 or nx >= r or ny >= c: continue
                world[nx][ny] = iter
            # 골렘이 도착한 위치에 사각형을 그린다
            direction(r_i, c_i, d_i)
            # 정령 탈출일기 작성
            # bfs를 통해 정령이 최대로 내려갈 수 있는 행를 계산하여 누적합니다
            answer += bfs(r_i, c_i) - 3 + 1
            # for _ in range(4):
            #     nx, ny = r_i + dx[_], c_i + dy[_]
            #     if nx < 0 or ny < 0 or nx >= r or ny >= c: continue

            '''
            정령 탈출
            조건 1. 처음에 이동한 출구에서 인접한 골렘이 있으면 탈출
                2. 없으면 탈출 못하니까 그냥 최대한 내려감
                3. 내려간대서 출구찾기는 없음
                4. 만약 탈출 했으면 다시 처음

            구현 1. 인접한 출구 찾기 
                2. 인접한 출구로 이동 <- 임시 배열에서 이 출구 다시 못쓰도록 골렘으로 바꾸고 나감
                3. 이동한 출구에 붙어있는 골렘 어느곳이든 이동 <- BFS
                4. 출구로 만약에 나가면 BFS 나가는거 1로 골렘으로 바꿔버려서 다시 못들어가게 함
                5. 골렘마다 다른 아이디 줘야하는거 아닌가? 
            '''
            break

print(answer)
# 그렸으니, 이제 정령 이동
# BFS 쓰기?


# 현 상황, 어떤 골렘이 끝까지 오긴함
# 이제 정령이 이동
# 정령이 이동하는 방향
# 정령이 이동하는 방향은 골렘의 출구 방향과 같다


# print_world(world)


'''
case : 1
6 5 6
2 3
2 0
4 2
2 0
2 0
2 2


case : 16
8 8 14
5 0
4 0
7 1
2 3
7 1
3 2
4 0
2 2
6 3
3 3
4 2
2 3
3 3
5 3

83
'''


