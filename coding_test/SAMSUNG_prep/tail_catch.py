import sys
from copy import deepcopy as copy
from collections import deque

input = sys.stdin.readline()

n , m , k = map(int, input().split())

ans = 0 # for saving result 
world = []

for row in range(n):
    world.append(list(map(int, input().split())))

gl = []
map =[[False for _ in range(n)] for _ in range(n)]

dr,dc = [-1,0,1,0],[0,1,0,-1]
class human:
    def __init__(self):
        self.r
        self.c
        self.isHead
        self.isTail
        self.no

def move(glist):
    new_world = copy(world)
    for team in glist:
        newteam = deque()
        poplefted = team[0]
        if poplefted.isHead == True:
            while team:
                man = team.pop()
                if team: 
                    for _ in range(4):
                        nr, nc = man.r + dr[_], man.c+dc[_]
                        if 0<=nr<n and 0<=nc<n and world[nr][nc] == 4:
                            new_world[man.r][man.c] = 4
                            man.r, man.c = nr,nc
                            
                else : 
                    new_world[man.r][man.c] = 4
                    man.r = team[-1].r
                    man.c = team[-1].c
                newteam.append(man)
        elif poplefted.isTail == True:
            while team:
                man = team.popleft()
                if team: 
                    for _ in range(4):
                        nr, nc = man.r + dr[_], man.c+dc[_]
                        if 0<=nr<n and 0<=nc<n and world[nr][nc] == 4:
                            new_world[man.r][man.c] = 4
                            man.r, man.c = nr,nc
                else : 
                    new_world[man.r][man.c] = 4
                    man.r = team[-1].r
                    man.c = team[-1].c
                newteam.append(man)
        else : print("\n ERROR Not appropriate Access")
        #update world with newteam_q on new_world
        for member in newteam:
            if member.isHead :
                new_world[member.r][member.c] = 1
            elif member.isTail :
                new_world[member.r][member.c] = 3
            else : 
                new_world[member.r][member.c] = 2



    # move human 
        # if Head :
        # if Body :
        # if Tail : 

    # mark on the map

def shot_count(glist, iter):




    # for col in range(len(world[row])):
    #     if col != 0 :
    #         map[row][col]= True

    # 팀 두개 나눠서 저장하고 있기
team_cnt = 0
team_que = deque()
adv_q = deque()
for row in range(n):
    if team_cnt>=2: break
    for col in range(n):
        if world[row][col] == 1: #머리 찾고
            tmp = human()
            tmp.r = row
            tmp.c = col
            tmp.isHead = True
            tmp.isTail = False
            tmp.no = 1
            team_que.append(tmp)
            adv_q.append(row,col)
            cnt = 0
            while adv_q:
                cnt+=1
                cr, cc = adv_q.popleft()
                for dir in range(4):
                    nr, nc = cr + dr[dir], cc + dc[dir]
                    if 0<=nr<n and 0<=nc<n and world[nr][nc] == 2: #몸통 찾고
                        adv_q.append(nr,nc)
                        tmp = human()
                        tmp.r = nr
                        tmp.c = nc
                        tmp.isHead = False
                        tmp.isTail = False
                        tmp.no = cnt
                        team_que.append(tmp)
                    elif 0<=nr<n and 0<=nc<n and world[nr][nc] == 3: #꼬리 찾음
                        adv_q.append(nr,nc)
                        tmp = human()
                        tmp.r = nr
                        tmp.c = nc
                        tmp.isHead = False
                        tmp.isTail = True
                        tmp.no = cnt
                        team_que.append(tmp)
                        team_cnt+=1
                        break


for _ in range(k):
    gl = move(gl) #move function return group list and also mark update function make new world with road array and mark 1 2 3 on the road
    gl, tmp = shot_count(gl, _) # shot function return group list and result
    ans += tmp


