import sys
from collections import deque

def bfs(init_x,init_y,visited,sex):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(init_x,init_y)])
    visited[init_x][init_y] = True
    cnt =1
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if sex[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt

input = sys.stdin.readline

N = int(input())

visited = [[False for _ in range(N)] for _ in range(N)]
sex = [list(map(int, input().strip()))for _ in range(N)]


sexy = []
for i in range(N):
    for j in range(N):
        if sex[i][j] == 1 and not visited[i][j]:
            size = bfs(i,j,visited,sex)
            sexy.append(size)

# print(sexy)
sexy.sort()

power_sex = len(sexy)
print(power_sex)
for ass in sexy:
    print(ass)
# print(visited)
