import sys
from collections import deque

input = sys.stdin.readline

'''

덩어리 찾기 함수 하나 만들고

y축 기준 맨 아래로 내리기 함수 하나 만들고

덩어리가 없으면 종료
'''


# table 만들고
table=[]


for i in range(12):
    table.append(list(map(str,input())))

#방문 표 만들고
visited=[[False for _ in range(6)]for _ in range(12)]
#현위치 기반 좌표 조지기 만들고 (덩어리 찾기용)
dx,dy = [-1,1,0,0],[0,0,-1,1]

queue = deque()

tmp_cnt = 0


def arran(table):
    for _ in range(12):
        for i in range(11,0,-1):
            for j in range(5,0,-1):
                if table[i][j] =='.' and table[i-1][j]!='.':
                    table[i][j]=table[i-1][j]
                    table[i-1][j]='.'
                    print("swap")



def show_table(table):
    for i in range(12):
        print(table[i],' ')

show_table(table)
arran(table)
show_table(table)
#bfs 덩어리 찾기용
def bfs(visited, table, x,y):
    return 0

flag = '.'
flagcnt = 0
def find_chunk(table, visited, queue, tmp_cnt, flag, flagcnt):
    for i in range(12):
        for j in range(6):
            if table[i][j] == '.':
                visited[i][j] = True
                continue
            elif table[i][j] !='.' and visited[i][j] != True:
                flag = table[i][j]
                queue.append((i,j))
                x, y = queue.popleft()
                visited[i][j]=True
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    print(f"cur is {table[x][y]} nx ny is {table[nx][ny]}")
                    if 0 <= nx <= 12 and 0 <= ny <= 6 and table[nx][ny] == flag:
                        # tmp_cnt += 1
                        queue.append((nx, ny))
                        visited[nx][ny] = True
        print(visited[i])


