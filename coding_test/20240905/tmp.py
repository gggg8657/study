from collections import deque


def solution(maps):
    answer = 0
    '''
    1. 완탐
    2. 완탐 중 방문기록 True 갯수 적은거 출력하기
    '''

    def show_board(maps):
        for i in range(5):
            print(maps[i], end="\n")

    queue = deque()

    visited = [[False for _ in range(len(maps))] for _ in range(len(maps))]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    cnt = 0
    # if not visited[i][j] and maps[i][j] == 1:
    queue.append((0, 0))
    visited[0][0] = True
    while queue and not visited[4][4]:
        show_board(maps)
        show_board(visited)
        print("queue is ", queue, "len of queue is ", len(queue))
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and maps[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                maps[ny][nx] = maps[y][x] + 1
                if visited[4][4] == True:
                    print(maps[4][4])
                    return cnt


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

solution(maps)