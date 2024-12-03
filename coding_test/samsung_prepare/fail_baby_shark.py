# # 문제 분석
#
# #bfs -> 상하좌우 이동 자기보다 작은놈 먹고, 같은놈 지나가고, 큰놈한테 쫄면서 감
#
# #움직이긴 하는데, 일단 조건 : 먹을 수 있는 고기가 한마리면 그놈먹으러감, 1마리보다 많으면 가까운놈 먹음,
# #가까운놈 많으면, 가장 위에 있는 고기, 가장 위에서도 많으면 가장 왼쪽 먹음
#
# #더 먹을놈 (자기보다 작은놈 없으면, 엄마부르는 스몰더년)
#
# #고기 먹으면, 그 칸 빈칸됨
#
# #자신의 크기와 같은 수의 물고기를 처묵 시, 크기 증가
#
# #엄마 부르기 전까지 몇초 걸리는지 구하시오,
#
# import sys
# from collections import deque
#
# def show_world(world):
#     for _ in range(len(world)):
#         print(world[_], end="\t*\n")
#     print("* * * * * * * * * * * * * * * * *")
#
#
# input = sys.stdin.readline
#
# n = int(input())
#
# arr=[]
# shark ={}
# fish = {}
# flag = 0
# shark_size = 2
# for row in range(n):
#     arr.append(list(map(int,input().split())))
#     for x in range(1, 7):
#         if x in arr[row]:
#             flag = 1
#             if x not in fish:
#                 fish[x] = []  # 초기화
#             fish[x].append((row, arr[row].index(x)))
#     if 9 in arr[row]:
#         shark["pos"] = (row,arr[row].index(9))
#         shark["size"] = shark_size
#
# if flag == 0 :
#     print("0")
#     exit()
#
#
# q = deque()
#
# q.append(shark["pos"])
#
#
# print(fish)
# print(q)
# print(n)
#
# show_world(arr)
# print(shark)
# print(fish.keys())
#
# print(shark["size"])
# food = deque()
# # while any(shark["size"] > key for key in fish.keys()):
# def check_food():
#     for key in fish.keys():
#         if shark["size"] > key:
#             food.append(fish[key])      #먹을 수 있는 물고기 위치들 받았음
#
# def eat_fish():
#
# # while q:
# drow, dcol = [-1,0,1,0], [0,1,0,-1]
# def bfs(row,col):
#     v = [[0]*n for _ in range(n)]
#     queue = deque([[row,col]])
#     food = []
#
#     v[row][col] = 1
#
#     while queue:
#         row,col = queue.popleft()
#
#         for i in range(4):
#             nrow, ncol = row + drow[i], col + dcol[i]
#             if 0<=nrow<n and o<=ncol<n and v[nrow][ncol]==0:
#                 if arr[row][col]>arr[nrow][ncol] and arr[nrow][ncol]!=0:
#                     v[nrow][ncol] = v[row][col]+1
#
#
#
#
from collections import deque

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

# 상어 초기 위치 및 이동 방향
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
x, y = [(i, j) for i in range(N) for j in range(N) if space[i][j] == 9][0]
space[x][y] = 0  # 초기 위치는 빈칸으로 초기화

size, eaten, time = 2, 0, 0

def bfs(sx, sy):
    visited = [[0] * N for _ in range(N)]
    queue = deque([(sx, sy, 0)])  # 현재 위치와 거리
    visited[sx][sy] = 1
    candidates = []

    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if space[nx][ny] <= size:  # 이동 가능
                    visited[nx][ny] = 1
                    if 0 < space[nx][ny] < size:  # 먹을 수 있는 물고기
                        candidates.append((dist + 1, nx, ny))
                    else:  # 빈칸이거나 같은 크기의 물고기
                        queue.append((nx, ny, dist + 1))
    return sorted(candidates, key=lambda x: (x[0], x[1], x[2]))

# 메인 루프
while True:
    fish = bfs(x, y)
    if not fish:  # 더 이상 먹을 물고기가 없으면 종료
        break
    dist, nx, ny = fish[0]
    time += dist
    eaten += 1
    if eaten == size:  # 크기 증가 조건
        size += 1
        eaten = 0
    space[nx][ny] = 0  # 물고기 먹음
    x, y = nx, ny

print(time)