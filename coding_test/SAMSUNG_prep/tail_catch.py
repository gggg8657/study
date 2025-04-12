import sys
from copy import deepcopy as copy
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

ans = 0 # for saving result 
world = []

for row in range(n):
    world.append(list(map(int, input().split())))

gl = []
mymap =[[False for _ in range(n)] for _ in range(n)]

dr,dc = [-1,0,1,0],[0,1,0,-1]
class human:
    def __init__(self):
        self.r =0
        self.c =0 
        self.isHead = False
        self.isTail = False
        self.no = 0

def move(glist, world):
    new_world = copy(world)
    moved_glist = []
    for team in glist:
        newteam = deque()
        poplefted = team[0]
        if poplefted.isHead == True:
            while team:
                man = team.pop()
                if len(team)==0: 
                    for _ in range(4):
                        nr, nc = man.r + dr[_], man.c+dc[_]
                        if 0<=nr<n and 0<=nc<n and (world[nr][nc] == 4 or world[nr][nc] == 3):
                            new_world[man.r][man.c] = 4
                            man.r, man.c = nr,nc
                            break
                else : 
                    new_world[man.r][man.c] = 4
                    man.r = team[-1].r
                    man.c = team[-1].c
                newteam.append(man)
        elif poplefted.isTail == True:
            while team:
                man = team.popleft()
                if len(team)==0: 
                    for _ in range(4):
                        nr, nc = man.r + dr[_], man.c+dc[_]
                        if 0<=nr<n and 0<=nc<n and (world[nr][nc] == 4 or world[nr][nc] == 3):
                            new_world[man.r][man.c] = 4
                            man.r, man.c = nr,nc
                            break
                else : 
                    new_world[man.r][man.c] = 4
                    man.r = team[0].r
                    man.c = team[0].c
                newteam.append(man)
        else : print("\n ERROR Not appropriate Access")
        moved_glist.append(newteam)
        #update world with newteam_q on new_world
        for member in newteam:
            if member.isHead :
                new_world[member.r][member.c] = 1
            elif member.isTail :
                new_world[member.r][member.c] = 3
            else : 
                new_world[member.r][member.c] = 2
    world = copy(new_world)
    return moved_glist, world

    # move human 
        # if Head :
        # if Body :
        # if Tail : 

    # mark on the map

#북 동 남 서 
# 총 쏘는 방향 서 남 동 북
# iter//n == 0 1 2 3

# 같은 테케에서 k 횟수가 10으로 증가하면 망함. 

'''
7 2 10
3 2 1 0 0 0 0
4 0 4 0 2 1 4
4 4 4 0 2 0 4
0 0 0 0 3 0 4
0 0 4 4 4 0 4
0 0 4 0 0 0 4
0 0 4 4 4 4 4
'''

def shot_count(glist, iter):
    result = 0
    # print("shot!")
    while iter >= 4 * n : 
        iter -= 4 * n
    row_pos, col_pos = 0,0
    if iter//n == 0: #왼쪽에서 쏨
        row_pos = iter%n-1
        for col_pos in range(n):
            #gun shoot 
            if 0<=row_pos<n and 0<=col_pos<n:
                for _ in range(len(glist)):
                    team = glist[_]
                    for mate in team:
                        if mate.r == row_pos and mate.c == col_pos:
                            result = mate.no ** 2
                            print(f"🟡 [SHOT] 맞은 위치: ({mate.r}, {mate.c}) / 팀 번호: {_+1} / 팀 내 순번: {team.index(mate)+1} / 점수: {result}")
                            for i in range(len(team)):
                                tm = team[i]
                                tm.no = len(team) - tm.no +1
                                if tm.isHead == True: 
                                    tm.isHead = False 
                                    tm.isTail = True
                                elif tm.isTail == True:
                                    tm.isTail = False
                                    tm.isHead = True
                            return glist, result
    elif iter//n == 1: #아래쪽에서 쏨
        col_pos = iter%n-1
        for row_pos in range(n-1, -1 ,-1):
            #gun shoot 
            if 0<=row_pos<n and 0<=col_pos<n :
                for _ in range(len(glist)):
                    team = glist[_]
                    for mate in team:
                        if mate.r == row_pos and mate.c == col_pos:
                            result = mate.no **2
                            print(f"🟡 [SHOT] 맞은 위치: ({mate.r}, {mate.c}) / 팀 번호: {_+1} / 팀 내 순번: {team.index(mate)+1} / 점수: {result}")
                            for i in range(len(team)):
                                tm= team[i]
                                tm.no = len(team) - tm.no +1
                                if tm.isHead == True: 
                                    tm.isHead = False 
                                    tm.isTail = True
                                elif tm.isTail == True:
                                    tm.isTail = False
                                    tm.isHead = True
                            return glist, result
    elif iter//n == 2: #오른쪽에서 쏨
        row_pos = n-1- iter%n
        for col_pos in range(n-1, -1,-1):
            #gun shoot 
            if 0<=row_pos<n and 0<=col_pos<n :
                for _ in range(len(glist)):
                    team = glist[_]
                    for mate in team:
                        if mate.r == row_pos and mate.c == col_pos:
                            result = mate.no**2
                            print(f"🟡 [SHOT] 맞은 위치: ({mate.r}, {mate.c}) / 팀 번호: {_+1} / 팀 내 순번: {team.index(mate)+1} / 점수: {result}")
                            for i in range(len(team)):
                                tm= team[i]
                                tm.no = len(team) - tm.no +1
                                if tm.isHead == True: 
                                    tm.isHead = False 
                                    tm.isTail = True
                                elif tm.isTail == True:
                                    tm.isTail = False
                                    tm.isHead = True
                            return glist, result
    elif iter//n == 3: #위에서 쏨
        col_pos = n-1- iter%n
        for row_pos in range(n):
            #gun shoot 
            if 0<=row_pos<n and 0<=col_pos<n:
                for _ in range(len(glist)):
                    team = glist[_]
                    for mate in team:
                        if mate.r == row_pos and mate.c == col_pos:
                            result = mate.no**2
                            print(f"🟡 [SHOT] 맞은 위치: ({mate.r}, {mate.c}) / 팀 번호: {_+1} / 팀 내 순번: {team.index(mate)+1} / 점수: {result}")
                            for i in range(len(team)):
                                tm= team[i]
                                tm.no = len(team) - tm.no +1
                                if tm.isHead == True: 
                                    tm.isHead = False 
                                    tm.isTail = True
                                elif tm.isTail == True:
                                    tm.isTail = False
                                    tm.isHead = True
                            return glist, result

    #if shot glist flip head tail
    #
    return glist, result



    # for col in range(len(world[row])):
    #     if col != 0 :
    #         map[row][col]= True

    # 팀 두개 나눠서 저장하고 있기
team_cnt = 0

adv_q = deque()

teams_list = []
for row in range(n):
    if team_cnt>=k: break
    for col in range(n):
        saved_rc = []
        team_que = deque()
        if world[row][col] == 1  and [row,col] not in saved_rc: #머리 찾고
            tmp = human()
            tmp.r = row
            tmp.c = col
            tmp.isHead = True
            tmp.isTail = False
            tmp.no = 1
            team_que.append(tmp)
            adv_q.append([row,col])
            saved_rc.append([row,col])
            cnt = 1
            while adv_q:
                cnt+=1
                cr, cc = adv_q.popleft()
                for dir in range(4):
                    nr, nc = cr + dr[dir], cc + dc[dir]
                    if 0<=nr<n and 0<=nc<n and world[nr][nc] == 2 and [nr,nc] not in saved_rc: #몸통 찾고
                        tmp = human()
                        tmp.r = nr
                        tmp.c = nc
                        tmp.isHead = False
                        tmp.isTail = False
                        tmp.no = cnt
                        adv_q.append([nr,nc])
                        saved_rc.append([nr,nc])
                        team_que.append(tmp)
                        last_r, last_c = nr,nc
                        break
            for dir in range(4):
                nr, nc = last_r + dr[dir], last_c + dc[dir]
                if 0 <= nr < n and 0 <= nc < n and world[nr][nc] == 3 and [nr, nc] not in saved_rc:
                    tmp = human()
                    tmp.r = nr
                    tmp.c = nc
                    tmp.isHead = False
                    tmp.isTail = True
                    tmp.no = cnt
                    team_que.append(tmp)
                    saved_rc.append([nr, nc])
                    break  # 꼬리 한 개만 붙이면 됨            

            teams_list.append(team_que)




for _ in range(k):
    print(f"[{_}] : Before Move")
    for tmp1 in range(n):
        print(world[tmp1])
    teams_list, world = move(teams_list, world) #move function return group list and also mark update function make new world with road array and mark 1 2 3 on the road
    print(f"[{_}] : After Move")
    for tmp1 in range(n):
        print(world[tmp1])
    teams_list, tmp = shot_count(teams_list, _+1) # shot function return group list and result
    print(tmp)
    ans += tmp
print(ans)

