'''
N X N list
F_(i,j)
B_(i,j)
input:
4 2
TTCC
TTTM
CCMM
CMMM
1 3 3 3
2 23 16 8
12 6 7 8
12 8 3 5
1. morning
    add all B_(i,j) +=1
    #이건 그냥 별개
'''

import sys
input = sys.stdin.readline
N, T = map(int, input().split())

world = [list(map(str, input().strip())) for _ in range(N)]
belief = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

# print(world)
# print(belief)
from collections import deque
q = deque()
dr,dc = [-1,1,0,0],[0,0,-1,1]



def morning():
    for row in range(N):
        for col in range(N):
            belief[row][col] +=1

morning()
# print(belief)

def arr_transform(nr,nc):
    caching = world[nr][nc]
    if caching == 'T': world[nr][nc] =1
    elif caching == 'C': world[nr][nc] =2
    elif caching == 'M': world[nr][nc] = 3
    elif caching == 'CM':world[nr][nc] =4
    elif caching == 'TM': world[nr][nc]=5
    elif caching == 'TC':world[nr][nc]=6
    elif caching == 'TCM':world[nr][nc] =7

def noon():
    #그룹 만들고, (이미 world가 그룹임)
    #그룹 안에서 대표 정하고
    #정한 대표 좌표를 캐싱해서 넘겨주면 night에서 꽤나 쓸만할듯
    #ngic is new_group_init_candi
    ngic = deque()
    q = deque()
    group = {}
    cap = {}
    group_list = []
    id = 0
    cur_r,cur_c,cur_cap =-1,-1,0
    """
    캔디데이트 안에 있는 놈을 꺼내서, 이게 그룹에 갈만한놈인지 찾을거임
    일단, 0,0 부터 시작
    """
    ngic.append((0,0))
    while ngic:
        cr,cc = ngic.popleft()
        if (cr,cc) not in group:
            q.append((cr,cc))
            while q:
                tr,tc = q.popleft()
                group_list.append((tr,tc))
                for d in range(4):
                    nr,nc = dr[d]+tr, dc[d]+tc
                    """
                    월드 안에 있으면서, 방문 안했으면서, 지금 좌표에 있는거랑 4방 좌표 방문하면서 그 좌표에 있는거가 같은거면
                    그룹 리스트에 추가하고
                    큐에 추가하고
                    같은게 아니면, 캔디데이트로 둬서 다음번 순회 하도록 하기
                    """
                    if 0 <= nr < N and 0 <= nc < N and world[nr][nc] != world[tr][tc] and visited[nr][nc] == False:
                        if (nr, nc) not in ngic:
                            ngic.append((nr,nc))
                            arr_transform(nr, nc)
                            visited[nr][nc] = True
                    elif 0 <= nr < N and 0 <= nc < N and world[nr][nc] == world[tr][tc] and visited[nr][nc] == False:
                        if (nr, nc) not in ngic:
                            group_list.append((nr,nc))
                            q.append((nr,nc))
                            arr_transform(nr,nc)
                            visited[nr][nc] = True
                            """
                            값이 큰놈 찾기
                            값이 같으면, row 작은놈 찾기
                            row 도 같으면 col 작은놈 찾기
                            """
                            if belief[nr][nc] > cur_cap:
                                cur_r, cur_c = nr,nc
                            elif belief[nr][nc] == cur_cap:
                                if nr<cur_r: #바꾸기
                                    cur_r, cur_c = nr,nc
                                elif nr==cur_r:
                                    if nc<cur_c: #바꾸기
                                        cur_r, cur_c = nr,nc
                            """
                            이거 끝나면, 값이 크거나, 좌표 크기가 작거나 한놈이 대표값으로 cur_r, cur_c 에 저장됨
                            고놈이 이제 대장인건데, 
                            """
        group[id] = group_list
        cap[id] = (cur_r,cur_c)
        id+=1
    id -= 1
    """
    대장한테 조공 올리기
    """
    for _ in range(id):
        cur_cpr, cur_cpc = cap[_]
        tmp_list = group[_]
        for iter in range(len(tmp_list)):
            tmpr,tmpc = tmp_list[iter]
            if tmpr != cur_cpr and tmpc != cur_cpc:
                belief[tmpr][tmpc] -=1
                belief[cur_cpr][cur_cpc] += 1

    return cap, group

import operator

def cp_sort(cp):
    d = {}
    for item in range(len(cp)):
        tr,tc = cp[item]
        d[item] = (world[tr][tc])
        print(item)
        print(world[tr][tc])
    d = sorted(d.items(), key=operator.itemgetter(1), reverse=False)
    print(d)
    '''
    dictionary id 가 1 2 3 4 5 6 7 로 되어있는데,
    그 id 에 해당하는 좌표에 있는 값이, 저 순서가 아니라면, 
    id가 아닌, id의 번호를 그에 해당하는 값에다가 소팅을 해줘야됨
    '''
    pass

def night(cp, gr):
    cp_sort(cp)
    pass

def cal_answer():
    #TCM : 111 TC : 110 TM : 101 CM : 011 M :100 C: 010, T: 001
    score_board={'TCM':0,'TC':0, 'TM':0, 'CM':0, 'M':0, 'C':0,'T':0 }
    for i in range(N):
        for j in range(N):
            score_board[world[i][j]]+=1

    for item in score_board:
        print(score_board[item],end=' ')
    print('\n', end='')

def sim():
    for i in range(T):
        morning()
        cp, gr = noon()
        night(cp, gr)

        cal_answer()

sim()

#그룹핑을 할 필요가 없지, 시발 저 world 텍스트 맵이 그룹핑 맵이네
'''
2. noon
    def grouping():
        for row in range(N):
            for col in range(N):
                world[row][col]
        while q:
            cr,cc = q.popleft()
            group[cr][cc]=id
            nr, nc = dr, dc 0 1 2 3 : N S W E : -1,0 1,0 0,-1 0,1
            if arr[nr][nc] == arr[r][c] :
                group[nr][nc]=id
    def be_group(nr,nc,id):
        group_dic={}
        group_dic[id]((id : nr,nc))

    def find_the_leader():
        B = 0 <- initial belief
        roi = 51 <- initial row
        coi = 51 <- initial col
        tmp_pos_len = 0 <- local caching
        tmp = group_dictionary.popleft()
            for item in tmp:
                if B =< Belief[item_r][item_c]:
                    tmp.append(Belief[item_r][item_c])
                    tmp_pos.append(item_r, item_c)
                    tmp_pos_len +=1
            if tmp_pos_len == 1 : <- 후보가 한놈 정말 잘됐음
                be_the_leader(tmp_pos.popleft())
            for item in tmp_pos: <- 신앙심 높은 놈들 중 row 작은놈 찾기
                if roi >= item.row:
                    roi = item.row


3. night


'''
