'''
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(q):

    while q:
        x, y, s = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny] and a[nx][ny] == '.':
                    q.append((nx, ny, s))
                    visit[nx][ny] = visit[x][y] + 1
            else:
                if s == 'J':
                    return visit[x][y]


n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if a[i][j] == 'J':
            visit[i][j] = 1
            q.append((i, j, 'J'))
        if a[i][j] == 'F':
            visit[i][j] = 1
            q.appendleft((i, j, 'F'))

ans = bfs(q)
if ans:
    print(ans)
else:
    print('IMPOSSIBLE')
'''

import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, sys.stdin.readline().split())

#print(R,".", C)

visited = [[False for _ in range(C)] for _ in range(R)]

visitedF = [[False for _ in range(C)] for _ in range(R)]
# print(visited)

table =[]

for i in range(R):
    table.append(list(map(str,input())))


# print(table)

queueJ = deque()
queueF = deque()
def find_next_way(table,i,j,queue):
    flag=0
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    for k in range(4):
        nx,ny = i+dx[k], j+dx[k]
        if table[nx][ny] == '.':
            flag=10
            queue.append((nx,ny))
            return queue
    if flag!=10:
        print("IMPOSSIBLE")
        exit()
def move(table,i,j,queue):
    x,y = queue.popleft()
    visited[i][j]=True
    table[x][y]='J'
    table[i][j]='.'
    return table,visited,queue

for i in range(R):
    for j in range(C):
        if table[i][j]=='J':
            visited[i][j]=True
            queueJ = find_next_way(table, i, j, queueJ)
            table,visited,queueJ = move(table,i,j,queueJ)
        if table[i][j]=='F':
            visitedF[i][j]=True
            queueF=find_next_way(table,i,j,queueF)


'''
갈 수 있는 길이 있냐
탐색 -> 없으면 impossible
탐색 -> 있으면 이동

'''