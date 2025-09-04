import sys
from collections import deque

input = sys.stdin.readline


row, col, t = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(row)]


# input test
# print (n, m, t, world)

def init_t_world():
    arr = [[]]
    arr = [[0 for _ in range(col)] for _ in range(row)]
    return arr


dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]


def spread(world, r, c, new_world):
    cnt = 0
    world_candi = deque()
    for _ in range(4):
        nr, nc = dr[_] + r, dc[_] + c
        if (nr >= 0 and nc >= 0) and (nr < row and nc < col):  # 지도 범위 안에 있으면
            if world[nr][nc] != -1:  # 폭풍이 아니면
                world_candi.append([nr, nc])  # 나누어질 공간 후보 추가
                cnt += 1  # 나누어질 공간 개수 추가
    spreading_dust = world[r][c] // 5
    if spreading_dust<=0:
        new_world[r][c] += world[r][c]
        # print("spreading 0 dusts SKIP")
        # pprint(new_world)
        return new_world
    while world_candi:
        nr, nc = world_candi.popleft()
        new_world[nr][nc] += spreading_dust
    new_world[r][c] = new_world[r][c] + world[r][c] - spreading_dust * cnt
    # pprint(new_world)
    return new_world


# pprint(world)


def search():
    new_world = init_t_world()
    R, C = row, col
    w = world  # 전역 참조를 로컬 이름으로 캐싱
    for r in range(R):                 # r 먼저, c 나중 (일관 루프/약간의 locality)
        wr = w[r]
        for c in range(C):
            if wr[c] > 0:             # 먼지 있는 칸만 확산
                spread(w, r, c, new_world)
    return new_world

def update_world(world, tmp_world):
    R = len(world); C = len(world[0])
    for r in range(R):
        wrow = world[r]
        trow = tmp_world[r]
        for c in range(C):
            # -1 유지
            if wrow[c] != -1:
                wrow[c] = trow[c]
    return world


def ShiftL(tworld, start_row):
    _tmp = [0 for _ in range(col)]
    for _ in range(col-1, 0, -1):
        if tworld[start_row][_] != -1:
            _tmp[_ - 1] = tworld[start_row][_]
        else:
            _tmp[_] = -1
    tworld[start_row] = _tmp
    return tworld

def ShiftR(tworld, start_row):
    _tmp = [0 for _ in range(col)]
    for _ in range(col-1):
        if tworld[start_row][_]!=-1: _tmp[_ + 1] = tworld[start_row][_]
        else : _tmp[_] = -1
    tworld[start_row] = _tmp
    return tworld

def ShiftD(tworld, start_col, start_row, end_row):
    _tmp = [0 for _ in range(end_row+1)]
    for _ in range(start_row, end_row):
        if tworld[_][start_col] != -1: _tmp[_ + 1] = tworld[_][start_col]
        else: _tmp[_] = -1
    for _ in range(start_row, end_row): tworld[_][start_col] = _tmp[_]
    return tworld

def ShiftU(tworld, start_col, start_row, end_row):
    _tmp = [0 for _ in range(start_row+1)]
    for _ in range(start_row, end_row, -1):
        if tworld[_][start_col] != -1:
            if _ == 0: continue
            _tmp[_ - 1] = tworld[_][start_col]
        else:
            _tmp[_] = -1
    for _ in range(start_row, end_row, -1):
        tworld[_][start_col] = _tmp[_]
    return tworld


pur_rows = [i for i in range(row) if world[i][0] == -1]
up_row = pur_rows[0]

def upp(world):
    #좌변 하로 밀고
    world = ShiftD(world, 0, 0, up_row)
    #윗변 좌로 밀고
    world = ShiftL(world, 0)
    #우변 위로 밀고
    world = ShiftU(world, col-1, up_row, -1)
    #밑변 우로 밀고
    world = ShiftR(world, up_row)
    return world
def low(world):
    #좌변 위로 밀고
    world = ShiftU(world, 0, row-1, up_row)
    #밑변 좌로 밀고
    world = ShiftL(world, row-1)
    #우변 하로 밀고
    world = ShiftD(world, col-1, up_row+1, row)
    #윗변 우로 밀고
    world = ShiftR(world, up_row+1)
    return world



def clean(world):
    world = upp(world)
    world = low(world)
    return world
# tmp_world = search() #먼지 확산된 세상은 tmp_world 가 됨
for _ in range(t):
    update_world(world, search())
    world = clean(world)
    # pprint(world)

sum=0
for sr in range(row):
    for sc in range(col):
        if world[sr][sc]!=-1: sum+=world[sr][sc]
print(sum)
'''
함수
1. 청소
2. 확산

func 확산 : 
    한칸씩 순회
    if 확산 조건 True : 임시 배열에 확산 될 먼지 추가
    else continue

func 확산 될 먼지 추가(row,col):
    for _ in range(4) : 
        nr, nc = r + dr [_], c + dc[_] 
        if world[nr][nc] 확산 가능:
            확산 될 양 = world[r][c]//5
            tmp_world[nr][nc] = 확산 될 양
            확산된 양 += 확산 될 양
        tmp_world[r][c] = world[r][c] - 확산 된 양
    return tmp_world

func 청소 :
    윗동네
    아랫동네

func 윗동네: #맨 아랫줄부터, -> 아래 밀기, 오른쪽 올리기, 윗줄 당기기, 왼쪽 내리기
    move_world = init_t_world()
    for _ in range(m):
        if world[n//2][_] >= 0:
            move_world[n//2][_+1] = world[n//2][_]
    for _ in range (n//2):
        if world[]


func 아랫동네:



func shift_r: (input : before world, output : moved world)
func shift_l:
func shift_u:
func shift_d:

func update_world
'''

