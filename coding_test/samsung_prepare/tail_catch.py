# https://www.codetree.ai/training-field/frequent-problems/problems/tail-catch-play/description?page=3&pageSize=10
'''
input case :
7 2 1
3 2 1 0 0 0 0
4 0 4 0 2 1 4
4 4 4 0 2 0 4
0 0 0 0 3 0 4
0 0 4 4 4 0 4
0 0 4 0 0 0 4
0 0 4 4 4 4 4
'''

def print_world(world, n):
    for _ in range(n):
        print(world[_])
    print("* * * * * * * * * * * * *")


def bfs(row,col,team_n):
    q = deque()
    team=[]

    q.append((row,col))
    v[row][col] = 1
    team.append((row,col))
    world[row][col]=team_n

    while q:
        crow, ccol = q.popleft()
        # 4방 , 범위 내, 미방문, 조건 : 2 또는 출발지 아닌곳에서 온 3
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            nrow,ncol = crow+di, ccol+dj
            if 0<=nrow<n and 0<=ncol<n and v[nrow][ncol]==0:
                if world[nrow][ncol]==2 or ((crow,ccol) != (row,col) and world[nrow][ncol]==3):
                    q.append((nrow,ncol))
                    v[nrow][ncol]=1
                    team.append((nrow,ncol))
                    world[nrow][ncol]=team_n
    teams[team_n] = team

import sys
from collections import deque

queue = deque()
input = sys.stdin.readline

n, m, k = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(n)]


v = [[0]*n for _ in range(n)]
team_n = 5
teams = {}

for row in range(n):
    for col in range(n):
        if v[row][col] == 0 and world[row][col]==1:
            bfs(row,col,team_n)
            team_n+=1

print_world(world,n)
print(teams)

ans = 0

di, dj = [0, -1, 0, 1], [1, 0, -1, 0]

for round in range(k):
    # 1 머리방향으로 한칸씩 이동
    for team in teams.values():                     #   팀별로 리스트를 가져오기
        trow,tcol = team.pop()                      # tail point pop
        world[trow][tcol] = 4                       # change to 4
        hrow,hcol = team[0]                         # head point
        # near 4방 (범위 내) -> 4인 값을 추가 + 번호 교체
        for ni,nj in ((hrow-1,hcol), (hrow+1,hcol), (hrow,hcol-1), (hrow,hcol+1)):
            if 0<=ni<n and 0<=nj<n and world[ni][nj] == 4:
                team.insert(0, (ni,nj))             # 새 머리 좌표 추가 -> 맨 앞에 추가
                world[ni][nj] = world[hrow][hcol]   # 새 머리 위치에 팀 번호 추가
                break
        #제일 꼬리를 먼저 pop 하고 그 위치를 4로 바꿔
    # 2 라운드 번호에 맞게 시작 방향, 위치 계산
    dr = (round//n)%4
    offset = round%n#direction calculation
    if dr == 0:                                     # R
        ci,cj = offset, 0
    elif dr == 1:
        ci,cj = n-1, offset
    elif dr == 2:
        ci,cj = n-1-offset, n-1
    else :
        ci,cj = 0, n-1-offset
    print_world(world, n)
    print(teams)
    # 3 공에 맞은 사람 점수 추가 및 방향 반전
    for _ in range(n):                              # MAX N 까지 탐색
        if 0<=ci<n and 0<=cj<n and world[ci][cj]>4: # 누가 맞음
            team_n = world[ci][cj]
            # 좌표 index +1 해서, 제곱
            print(len(teams[team_n]))
            ans += (teams[team_n].index((ci,cj))+1)**2
            teams[team_n] = teams[team_n][::-1] # 팀 방향 바꾸기
            break
        if dr == 0 : cj+=1
        elif dr == 1 : ci-=1
        elif dr == 2 : cj-=1
        elif dr == 3 : ci+=1
print(ans)


