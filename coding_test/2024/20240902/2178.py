import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

table = []

for i in range(N):
    table.append(list(map(int,input())))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
queue = deque()
queue.append((0,0))

while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<M and table[nx][ny] ==1:
            queue.append((nx,ny))
            table[nx][ny] = table[x][y] + 1

print(table[N-1][M-1])





# while

# 4,6 이 목적지
#
'''
1. graph 만들고
2. graph 에서 N,M 까지 가야되면, N,M 인지는 index 로
3. prob solving
3.1. 전체 순회 -> 0으로는 graph 연결 안됨
3.2. graph 연결 된 곳만 지나감, 
3.3. 지나간 곳은 방문 처리 (왜냐? 제일 짧은길인데, 돌아갈리가 없음)
3.4. 6 by 6 배열
3.5. map 만들고
3.6. 0,1 -> 1,0 으로 진행
'''

