import sys
from collections import deque

input=sys.stdin.readline

'''
작전명 적록색약

1. 입력은 숫자 N
2. 입력은 그리고 그림 R G B 어쩌구
3. 출력은 구역으로 -> 덩어리 찾기네

sol

1. 완전 탐색 dx dy 쓰면서 nx = x + dx[i] 쓰면서 진행할꺼고
2. 인접한게 같은 색이면 덱에 넣고, 탐색 할거고, 
3. 다른색이면 덱에 안넣어? 생각이 잘못됐다.
4. 그럼, 다시 처음부터
5. 1. 은 유지
6. 완전 탐색 하면서, 덩어리 주위에 것nx 에 있는거나, ny에 있는것이 현재 값과 다르면, 카운트 추가
6.1. 하면, 일단 정상인 오케이
7. 그럼 적녹색약자는 어케 조지냐?
7.1. 조건을 하나 더 추가해? 그럼 코드가 개길어질텐데?
7.2. 조건을 하나 더 추가하지 않고, 처음에 탐색하면서 같이 할 수 있는 방법은 count B 를 만들어서
7.3. Count B 에는 만약 주위에 것이 현재와 달라, 그런데 만약 현재가 R 혹은 G 면 같은거로 처리 이게 젤 빠를거 같은데

'''
#
# 5
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
size = int(input())

table = []

for i in range(size):
    table.append(list(map(str,input())))


dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
queue = deque()


visited=[[False for _ in range(size)] for _ in range(size)]

count=0
countb=0
for k in range(size):
    for j in range(size):
        if not visited[k][j]:
            visited[k][j] = True
            queue.append((k,j))
            while queue:
                x,y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # print("nx, ny is " , table[nx][ny])
                    # print("x , y is " , table[x][y])
                    if 0<=nx<size and 0<=ny<size and table[x][y] == table[nx][ny] and visited[nx][ny] ==False:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        # print(visited)
            count+=1

        # elif:
tableRB = table
for i in range(size):
    for j in range(size):
        if tableRB[i][j] == 'R':
            # print(i, j)
            tableRB[i][j] = 'G'
        else:
            continue
visited = [[False for _ in range(size)] for _ in range(size)]
for k in range(size):
    for j in range(size):
        if not visited[k][j]:
            visited[k][j] = True
            queue.append((k, j))
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # print("nx, ny is " , table[nx][ny])
                    # print("x , y is " , table[x][y])
                    if 0 <= nx < size and 0 <= ny < size and table[x][y] == table[nx][ny] and visited[nx][
                        ny] == False:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        # print(visited)
            countb += 1

        # print(table[i])

print(count)
print(countb)



