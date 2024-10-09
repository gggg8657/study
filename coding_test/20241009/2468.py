import sys
from collections import deque
from pprint import pp as print


queue = deque()

input = sys.stdin.readline

N = int(input())

world = [list(map(int, input().split()))for _ in range(N)]

# print(world)

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

result = 0

for H in range(101):
    visited = [[False for _ in range(N)] for _ in range(N)]
    tmp = 0
    for i in range(N):
        for j in range(N):
            if world[i][j] > H and visited[i][j]==False:
                bfs(world,visited,i,j,H)
                tmp+=1
    result = max(result, tmp)

print(result)