import sys
from collections import deque

input = sys.stdin.readline


def show_board(board):
    for i in board:
        for j in i:
            print(j, end='')
        print('')


board = [list(input().rstrip()) for _ in range(12)]
ans = 0
dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
is_boom = True
queue = deque()
while is_boom:
    is_boom = False
    for i in range(11, -1, -1):
        for j in range(0, 6):
            if board[i][j] != '.':
                is_visit = [[False for _ in range(6)] for _ in range(12)]
                cnt = 1  # 현재까지 비교한 친구들 숫자
                now = board[i][j]  # 비교할 대상 얘랑 같으면 친구임
                boom_list = [[i, j]]  # 터질놈들
                queue.append([i, j])  # BFS queue 어쩌구
                is_visit[i][j] = True  # 반드시 처음 넣어준거 isvisit처리
                while queue:
                    y, x = queue.popleft()
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if 0 <= ny < 12 and 0 <= nx < 6 and is_visit[ny][nx] == False and board[ny][nx] == now:
                            boom_list.append([ny, nx])
                            is_visit[ny][nx] = True
                            queue.append([ny, nx])
                            cnt += 1
                if cnt >= 4:  # 친구가 4이상이면 집합금지
                    for y, x in boom_list:
                        board[y][x] = '.'  # 터트려
                    is_boom = True  # 터진기록작성
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if board[j][i] != '.' and board[k][i] == '.':
                    board[k][i] = board[j][i]
                    board[j][i] = '.'

    if is_boom == True:
        ans += 1

print(ans)
