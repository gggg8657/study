def show_world(arr):
    for line in arr:
        print(line)
    print("* * * * * * * * * * *")

def find_exit_from_(arr, a):
    if a == 4:
        S,E = 0, N
    else : S, E = M, M+M
    for row in range(S, E):
        for col in range(S, E):
            for direction in range(4):
                nrow, ncol = row+drow[direction], col+dcol[direction]
                if arr[nrow][ncol] == a: return nrow,ncol

import sys

input = sys.stdin.readline

N, M, F = map(int, input().split())

world = [list(map(int, input().split()))for _ in range(N)]

D_world = []

NONE = [99 for _ in range(M)]
E_world = [list(map(int, input().split()))for _ in range(M)]
D_world.append(E_world)
W_world = [list(map(int, input().split()))for _ in range(M)]
D_world.append(W_world)
S_world = [list(map(int, input().split()))for _ in range(M)]
D_world.append(S_world)
N_world = [list(map(int, input().split()))for _ in range(M)]
D_world.append(N_world)
T_world = [list(map(int, input().split()))for _ in range(M)]
D_world.append(T_world)



world_map = [[0 for _ in range(M*M)]for _ in range(M*M)]
mid = []
bottom = []
for _ in range(M):
    world_map[_] = NONE + N_world[_] + NONE

for _ in range(M, M+M):
    world_map[_] = W_world[_-M] + T_world[_-M] + E_world[_-M]

for _ in range(M+M, M+M+M):
    world_map[_] = NONE + S_world[_-M-M] + NONE

from collections import deque

q = deque()
drow,dcol = [-1,1,0,0],[0,0,-1,1]
while q:
    row,col = q.popleft()
    for d in range(4):
        nrow = row+drow[d]
        ncol = col+ncol[d]
        if world[nrow][ncol] == 99:
            if row == M:
                if col<M : # 서쪽의 맨 윗줄
                    nrow,ncol = ncol,nrow # M, 0 1 2 -> 0 1 2 , M
                elif col>2*M: # 동쪽의 맨 윗줄
                else: #가운데칸
            elif row==2*M-1:
                if col<M: #서쪽의 맨 아랫줄
                elif col>2*M: #동쪽의 맨 윗줄
                else : #가운데칸
            elif col == M:
                if row<M: #북쪽의 맨 왼쪽줄
                elif row>2*M: #남쪽의 맨 왼쪽 줄
                else: #가운데칸
            elif col == 2*M -1:
                if row<M: #북쪽의 맨 오른줄
                elif row>2*M: #남쪽의 맨 오른줄
                else: #가운데 칸
        else:



show_world(world_map)
for line in world_map:
    if 2 in line:
        MLx, MLy = world_map.index(line), line.index(2)
print(MLx,MLy)

drow, dcol = [-1,1,0,0,], [0,0,-1,1]
erow, ecol = find_exit_from_(world, 0)
EROW, ECOL = find_exit_from_(world, 4)

ESANG = [list(map(int, input().split()))for _ in range(F)]

show_world(world)
show_world(D_world)
show_world(ESANG)