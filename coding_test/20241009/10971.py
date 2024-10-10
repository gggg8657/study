import sys
from pprint import pp as print
from collections import deque

input = sys.stdin.readline

N = int(input())

table = [list(map(int, input().split()))for _ in range(N)]

# print(cost)
# TODO
# BFS -> return cost of route
# if new cost of route < saved cost of route : cost of route = new cost of route
def bfs(table, visited, i,j, N):
    dx,dy = [1,-1,0,0,], [0,0,1,-1]
    queue.append((i,j))
    visited[i][j]=True
    cost = table[i][j]
    visit_list = []
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = dx[i]+x, dy[i]+y
            if nx<0 or nx>=N or ny<0 or ny>=N: continue
            if visited[nx][ny]==False and table[nx][ny] != 0:
                queue.append((nx,ny))
                visited[nx][ny]=True
                cost += table[nx][ny]
    return cost
cost = []
for i in range(N):
    for j in range(N):
        if table[i][j]!=0:
            queue = deque()
            visited = [[False for _ in range(N)] for _ in range(N)]
            cost.append(bfs(table,visited,i,j,N))

print(cost)
print(min(cost))

