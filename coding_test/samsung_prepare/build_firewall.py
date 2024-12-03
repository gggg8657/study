import sys
from itertools import combinations
import copy
from collections import deque

def world_view(arr):
    for _ in range(len(arr)):
        print(arr[_])
    print("* * * * * * * * * * * * * *")

def build_wall(tarr, points):
    # points ((),(),())
    for i in range(3):
        x,y = points[i]
        tarr[x][y] = 1
    # print("before burned")
    # world_view(tarr)
    return tarr

def BFS(narr):
    return_val = 0
    v = [[False for _ in range(m)] for _ in range(n)]
    for i in range(len(fire_coordinates)):
        x,y = fire_coordinates[i]
        q.append((x,y))
        v[x][y] = True
        while q:
            cx,cy = q.popleft()
            # print(cx,cy)
            for way in range(4):
                nx,ny = cx+dx[way], cy+dy[way]
                if 0<=nx<n and 0<=ny<m and v[nx][ny]==False and narr[nx][ny]==0:
                    narr[nx][ny] = 2
                    q.append((nx,ny))
                    v[nx][ny]=True
    # print("after burned")
    # world_view(narr)

    for _ in range(n):
        for U in range(m):
            if narr[_][U] == 0: return_val+=1
    return return_val

def combination(arr,n):
    comb=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                comb.append((arr[i],arr[j],arr[k]))
    # print(comb)
    return comb

input = sys.stdin.readline

n, m = map(int,input().split())

arr = [list(map(int,input().split()))for _ in range(n)]

q = deque()

# v = [[False for _ in range(m)]for _ in range(n)]

dy, dx = [-1,1,0,0,], [0,0,-1,1]

wall_cnt = 0
fire_cnt = 0
coordinates=[]
fire_coordinates=[]
for _ in range(n):
    for j in range(m):
        if arr[_][j] == 1: wall_cnt += 1
        elif arr[_][j] == 2:
            fire_cnt += 1
            fire_coordinates.append([_,j])
        elif arr[_][j] == 0: coordinates.append([_,j])
comb = combination(coordinates,3)
# point_list = list(combinations(coordinates, 3))
# print(point_list)
x = n*m - fire_cnt - wall_cnt
scene_no = int(x*(x-1)*(x-2)/6)
# print(scene_no)
ans = 0
for i in range(scene_no):
    tmp_world= copy.deepcopy(arr)
    new_points = comb.pop()
    tmp_world= build_wall(tmp_world,new_points)
    tmp = BFS(tmp_world)
    # print(f"result is {tmp}")
    if tmp>ans: ans =tmp
    else: continue

print(ans)
# print(world)