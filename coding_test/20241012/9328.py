from collections import deque
import sys

input = sys.stdin.readline

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
def bfs():
    global result

    q.append((0, 0))  # (x, y)
    visit[0][0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx <= h + 1 and 0 <= ny <= w + 1 and not visit[nx][ny] and field[nx][ny] != '*':
                visit[nx][ny] = True

                # 문서를 발견한 경우
                if field[nx][ny] == '$':
                    result += 1
                    field[nx][ny] = '.'
                    q.append((nx, ny))

                # 열쇠를 발견한 경우
                elif 'a' <= field[nx][ny] <= 'z':
                    key_idx = ord(field[nx][ny]) - ord('a')
                    if not keys[key_idx]:  # 새로운 열쇠라면
                        keys[key_idx] = True
                        q.append((nx, ny))
                        open_doors(key_idx)
                    field[nx][ny] = '.'
                    q.append((nx, ny))

                # 문을 발견한 경우
                elif 'A' <= field[nx][ny] <= 'Z':
                    door_idx = ord(field[nx][ny]) - ord('A')
                    if keys[door_idx]:  # 열쇠가 있으면 문을 열고 들어간다
                        field[nx][ny] = '.'
                        q.append((nx, ny))
                    else:
                        doors[door_idx].append((nx, ny))

                # 빈 공간인 경우
                else:
                    q.append((nx, ny))


def open_doors(key_idx):
    while doors[key_idx]:
        x, y = doors[key_idx].popleft()
        field[x][y] = '.'
        visit[x][y] = True
        q.append((x, y))


for _ in range(int(input())):
    h, w = map(int, input().split())
    field = [['.'] * (w + 2) for _ in range(h + 2)]

    # 필드를 입력 받음
    for i in range(1, h + 1):
        line = input().strip()
        for j in range(1, w + 1):
            field[i][j] = line[j - 1]

    # 초기 열쇠 목록을 입력 받음
    initial_keys = input().strip()
    keys = [False] * 26
    if initial_keys != '0':
        for ch in initial_keys:
            keys[ord(ch) - ord('a')] = True

    # 방문 체크
    visit = [[False] * (w + 2) for _ in range(h + 2)]

    # 문 위치 저장
    doors = [deque() for _ in range(26)]

    # 훔친 문서 개수
    result = 0

    # BFS 탐색
    bfs()

    print(result)
