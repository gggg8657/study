#named TOMATO MAT TO TO MAT TOMATO

import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int, input().split())

# print(m, n)

table = [list(map(int, input().split()))for _ in range(n)]

# print(table)

queue = deque()

def find_number_in_2d_list(table):
    [queue.append((i, j)) for i, row in enumerate(table) for j, value in enumerate(row) if value == 1]
    return queue

find_number_in_2d_list(table)

#find if there can't be success
def bfs(world, visited, x,y):
    dx,dy = [-1,1,0,0], [0,0,-1,1]
    queue.append((x,y))
    visited[x][y]=True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = dx[i]+x, dy[i]+y
            if 0<=ny<m and 0<=nx<n and world[ny][nx]!=-1 and visited[ny][nx]==False:
                queue.append((ny,nx))
                visited[ny][nx]=True
                world[ny][nx]=1


'''
def bfs(world, visited, x,y, H):
    dx,dy = [-1,1,0,0,],[0,0,-1,1]
    queue.append((x,y))
    visited[x][y]=True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
            if 0<=nx<N and 0<=ny<N and world[nx][ny]>H and visited[nx][ny]==False:
                queue.append((nx,ny))
                visited[nx][ny]=True

'''