import sys
# from pprint import pp as print
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

arr = [i for i in range(101)]

src_list = []
tar_list = []
cnt_list = []
for _ in range(N+M):
    a,b = map(int,input().split())
    src_list.append(a)
    tar_list.append(b)


def ride_snake_ladder(cur):
    if cur in src_list:
        next_idx = src_list.index(cur)
        tar = tar_list[next_idx]
        # print("src : ",cur,"tar: ",tar)
        return tar
    else:
        # print("not changed")
        return cur

dx = [1,2,3,4,5,6]

def bfs(x):
    cnt = 0
    visit = [False for _ in range(101)]
    queue = deque()
    queue.append((x,0))
    visit[x] = True
    while queue:
        x, cnt = queue.popleft()
        # x = ride_snake_ladder(x)
        for i in range(6):
            nx = dx[i]+x
            # print("nx is ", nx)
            if nx == 100:
                return cnt+1
            nx = ride_snake_ladder(nx)
            if nx<=100 and visit[nx]==False:
                queue.append((nx, cnt+1))
                visit[nx]=True

                # print("current count is ", cnt)


# print(arr)

print(bfs(1))



# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
#
# # 사다리와 뱀 위치를 저장하는 리스트
# src_list = []
# tar_list = []
#
# # 사다리와 뱀 정보를 입력받음
# for _ in range(N + M):
#     a, b = map(int, input().split())
#     src_list.append(a)
#     tar_list.append(b)
#
# # 사다리나 뱀을 탈 때의 위치를 반환하는 함수
# def ride_snake_ladder(cur):
#     if cur in src_list:
#         next_idx = src_list.index(cur)
#         tar = tar_list[next_idx]
#         return tar
#     return cur
#
# # BFS
# def bfs():
#     visit = [-1] * 101
#     queue = deque([1])
#     visit[1] = 0
#
#     while queue:
#         x = queue.popleft()
#
#
#         for dice in range(1, 7):
#             nx = x + dice
#             if nx > 100:
#                 continue
#
#
#             nx = ride_snake_ladder(nx)
#
#
#             if visit[nx] == -1:
#                 visit[nx] = visit[x] + 1
#                 queue.append(nx)
#
#             if nx == 100:
#                 return visit[nx]
#
#
# result = bfs()
# print(result)
