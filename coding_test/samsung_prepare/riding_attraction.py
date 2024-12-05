# import sys
# from collections import deque
#
# def show_world(world):
#     for _ in range(n):
#         print(world[_])
#     print("* * * * * * * * * *")
#
#
# def BFS(arr, world):
#     #arr 는 특정 학생 배열임 그래서, 여기선 그 학생이 어디 갈지 정하는거임
#     visit = [[False for _ in range(size)] for _ in range(size)]
#     pos_score = [[0 for _ in range(size)] for _ in range(size)]
#     near_world = [[0 for _ in range(size)] for _ in range(size)]
#     q.append([0,0])
#     visit[0][0] = True
#     while q:
#         print(q)
#         y,x = q.popleft()
#         for d in range(4):
#             ny, nx = y+dy[d], x+dx[d]
#             if 0<=ny<size and 0<=nx<size and world[ny][nx]==0 and visit[ny][nx]==False: #앉을 수 있는 자리임
#                 q.append([ny,nx]) #갈 수 있는 자리임 그냥
#                 visit[ny][nx]=True
#                 for friend in range(1,len(arr)):
#                     for _ in range(4):
#                         fy, fx = ny+dy[_], nx+dx[_]
#                         if 0<=fy<size and 0<=fx<size:
#                             if arr[friend] == world[fy][fx]:
#                                 pos_score[ny][nx]+=1
#                             if world[fy][fx] == 0:
#                                 near_world[ny][nx] +=1
#
#     return pos_score, near_world
#
#         # 조건 : 네방향으로 인접한 칸 중 앉아있는 좋아하는 친구 수가 가장 많은 위치
#         # 만약 다 같은 수 -> 비어있는 칸 수가 많은 곳 감
#         # 동일한 위치가 여러곳이면, 행 번호가 작은 위치
#         # 동일한 행에서는 열 번호가 작은 위치
#
# q = deque()
#
# input = sys.stdin.readline
#
# n = int(input())
#
# world = [[0 for _ in range(n)] for _ in range(n)]
#
# arr = [list(map(int, input().split()))for _ in range(n*n)]
# dy,dx = [-1,1,0,0], [0,0,-1,1]
# size = n
# print(n)
# print(arr)
# print(world)
# for _ in range(n*n):
#     show_world(world)
#     x = arr[_]
#     pos_score, near_empty = BFS(x,world)
#     M = max(pos_score[0])
#     M_point_y, M_point_x = 0,pos_score[0].index(M)
#     for y in range(len(pos_score)):
#         if M<max(pos_score[y]):
#             M = max(pos_score[y])
#             M_point_y, M_point_x = y,pos_score[y].index(M)
#         else: M=M
#     if M==0:
#         world[1][1] = arr[_][0]
#         print(f"init and first commit on the middle M is {M}")
#     else:
#         world[M_point_y][M_point_x] = arr[_][0]
#         print(M)
#     print(M)
#     print(M_point_y, M_point_x)
#     show_world(world)
#         # world[pos[0]][pos[1]] = arr[_][0]
#
#
#
# 시간 복잡도 = O(n^4) = 약 80만
#
# n=int(input())
#
# a=[[0]*n for _ in range(n)]
# ans=0
#
# dx=[-1,0,1,0]
# dy=[0,-1,0,1]
#
# # 학생 정보 받기
# order=[]
# like=[None]*(n**2+1)
# for _ in range(n**2):
#     n0, n1, n2, n3, n4 = map(int, input().split())
#     like[n0]=[n1,n2,n3,n4]
#     order.append(n0)
#
# def inBoard(nx,ny):
#     if 0<=nx<n and 0<=ny<n:
#         return True
#     return False
#
# for round in range(1,n**2+1):
#
#     no=order[round-1]
#     # 탑승 위치 탐색
#     tx,ty=-1,-1
#     cand = [] # 탑승 위치 후보
#     for x in range(n):
#         for y in range(n):
#             cnt = 0  # 좋아하는 친구 수
#             empty = 0  # 비어있는 칸의 수
#             # 항상 비어있는 칸으로만 이동합니다.
#             if a[x][y]!=0:continue
#             for k in range(4):
#                 nx,ny=x+dx[k],y+dy[k]
#                 if not inBoard(nx,ny):continue
#                 if a[nx][ny] in like[no]:
#                     cnt+=1
#                 elif a[nx][ny]==0:
#                     empty+=1
#             cand.append([cnt,empty,x,y])
#     # 격자를 벗어나지 않는 4방향으로 인접한 칸 중 앉아있는 좋아하는 친구의 수가 가장 많은 위치로 갑니다.
#     # 만약 1번 조건을 만족하는 칸의 위치가 여러 곳이라면, 그 중 인접한 칸 중 비어있는 칸의 수가 가장 많은 위치로 갑니다. 단 이때 격자를 벗어나는 칸은 비어있는 칸으로 간주하지 않습니다.
#     # 만약 2번 조건까지 동일한 위치가 여러 곳이라면, 그 중 행 번호가 가장 작은 위치로 갑니다.
#     # 만약 3번 조건까지 동일한 위치가 여러 곳이라면, 그 중 열 번호가 가장 작은 위치로 갑니다.
#     cand.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
#     tx,ty=cand[0][-2],cand[0][-1]
#     # 학생 탑승
#     a[tx][ty]=no
#
# for x in range(n):
#     for y in range(n):
#         cnt=0
#         no=a[x][y]
#         for k in range(4):
#             nx,ny=x+dx[k],y+dy[k]
#             if not inBoard(nx,ny):continue
#             if a[nx][ny] in like[no]:
#                 cnt+=1
#         if cnt==0:
#             continue
#         else:
#             ans+=10**(cnt-1)
#
# print(ans)
n = int(input())
grid = [[0] * n for _ in range(n)]
like = {}
order = []
for _ in range(n * n):
    arr = list(map(int, input().split()))
    student, prefs = arr[0], arr[1:]
    like[student] = prefs
    order.append(student)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def in_bounds(x, y):
    return 0 <= x < n and 0 <= y < n

for student in order:
    candidates = []
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 0:
                like_count = 0
                empty_count = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if in_bounds(nx, ny):
                        if grid[nx][ny] in like[student]:
                            like_count += 1
                        elif grid[nx][ny] == 0:
                            empty_count += 1
                candidates.append((-like_count, -empty_count, x, y))
    candidates.sort()
    x, y = candidates[0][2], candidates[0][3]
    grid[x][y] = student

# Calculate satisfaction
satisfaction = 0
for x in range(n):
    for y in range(n):
        student = grid[x][y]
        like_count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_bounds(nx, ny):
                if grid[nx][ny] in like[student]:
                    like_count += 1
        if like_count > 0:
            satisfaction += 10 ** (like_count - 1)
print(satisfaction)