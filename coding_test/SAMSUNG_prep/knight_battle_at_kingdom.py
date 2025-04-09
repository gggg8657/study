# # 2023 하반기 오전 1번 문제

# '''
# input : L, N, Q

# cond of L
#     0 means blank
#     1 means trap
#     2 means wall

# for N lines get information about knights : r, c, h, w, k
#     r : row
#     c : column
#     h : height
#     w : width
#     k : HP at begin
# 처음의 기사들의 위치는 겹쳐져 있지 않음
# 기사와 벽은 겹쳐서 주어지지 않음

# for next Q lines get information about order : i, d
#     i : i_th knights
#     d : direction
# i번째 기사에게 d 방향으로 한칸 이동하도록 명령
# d : 0 1 2 3 :: 북 동 남 서

# 3 <= L <= 40
# 1 <= N <= 30
# 1 <= Q <= 100
# 1 <= k <= 100
# '''

# # 입력 받고

# # 세팅하고

# # 기사 이동 (이동하려는 칸에 기사가 있으면 한칸 밀려남)
# #   이동 -> 근데 기사 있으면 그거 먼저 밀어냄 -> 근데 그 뒤에 벽이 있으면 안움직여짐 (못 움직임)

# # 대결 대미지 (밀려나면서 밟은 함정마다 체력 손실) : 기사가 모두 밀린 이후에 피를 깎음
# #   이동 -> 이동한 이후 함정 밟았나 확인 -> 체력 깎기

# # 출력 : Q번의 명령 수행 이후 : 생존한 기사들이 총 받은 대미지의 합을 출력하는 프로그램

# from collections import deque

# class kisa:
#     r = 0
#     c = 0
#     h = 0
#     w = 0
#     HP = 0
#     id = 0
# def print_init(world, isTrap, isWall, q, order):

#     print("\n\n * * * init world * * *\n")
#     print(world)
#     print("\n\n * * * init trap * * *\n")
#     print(isTrap)
#     print("\n\n * * * init wall * * *\n")
#     print(isWall)

#     print("\n\n * * * init knights * * *\n")
#     print(q)

#     print("\n\n * * * init orders * * *\n")
#     print(order)


# def is_in_range(r, c):
#     return 0 <= r < L and 0 <= c < L

# def is_knight(r,c):
#     for k in range(len(q)):
#         if q[k].id == n: continue
#         for i in range(q[k].h):
#             for j in range(q[k].w):
#                 if r == q[k].r +i and c == q[k].c+j: 
#                     print("knight is there")
#                     return True, k
#                 else : print("there is not knight")
#     return False, _

# def is_Wall(ck):
#     for i in range(ck.h):
#         for j in range(ck.w):
#             if isWall[ck.r + ck.h][ck.c + ck.w]: return True
#     return False

# def canGo(r, c):
#     ISKNIGHT = is_knight(r,c)
#     if isWall[r-1][c] ==False and is_in_range(r-1,c) and not is_knight(r,c): return True
#     else: return False

# def can_move(ck,d):
#     _ = 0
#     if d == 0 :
#         for i in range(ck.w):
#             for j in range(ck.h):
#                 ISKNIGHT, tmp = is_knight(ck.r-1,ck.c)
#                 if isWall[ck.r-1][ck.c] ==False and is_in_range(ck.r-1,ck.c) and not ISKNIGHT: # <- in check isWall, is knight (not me)
#                     print("can move")
#                     return 1, _
#                 elif isWall[ck.r-1][ck.c] : 
#                     print("cannot move the wall is on the way")
#                     return 2, _
#                 elif not is_in_range(ck.r-1,ck.c) : 
#                     print("cannot move out of the field")
#                     return 2, _
#                 elif ISKNIGHT: 
#                     print("should push knight first")
#                     return 0, tmp
#     elif d == 1 :
#         for i in range(ck.w):
#             for j in range(ck.h):
#                 ISKNIGHT, tmp = is_knight(ck.r,ck.c+1)
#                 if isWall[ck.r][ck.c+1] ==False and is_in_range(ck.r,ck.c+1) and not ISKNIGHT: # <- in check isWall, is knight (not me)
#                     print("can move")
#                     return 1, _
#                 elif isWall[ck.r][ck.c+1] : 
#                     print("cannot move the wall is on the way")
#                     return 2, _
#                 elif not is_in_range(ck.r,ck.c+1) : 
#                     print("cannot move out of the field")
#                     return 2, _
#                 elif ISKNIGHT: 
#                     print("should push knight first")
#                     return 0, tmp
#     elif d == 2 :
#         for i in range(ck.w):
#             for j in range(ck.h):
#                 ISKNIGHT, tmp = is_knight(ck.r+1,ck.c)
#                 if isWall[ck.r+1][ck.c] ==False and is_in_range(ck.r+1,ck.c) and not ISKNIGHT: # <- in check isWall, is knight (not me)
#                     print("can move")
#                     return 1, _
#                 elif isWall[ck.r+1][ck.c] : 
#                     print("cannot move the wall is on the way")
#                     return 2, _
#                 elif not is_in_range(ck.r+1,ck.c) : 
#                     print("cannot move out of the field")
#                     return 2, _
#                 elif ISKNIGHT: 
#                     print("should push knight first")
#                     return 0, tmp
#     elif d == 3 :
#         for i in range(ck.w):
#             for j in range(ck.h):
#                 ISKNIGHT, tmp = is_knight(ck.r,ck.c-1)
#                 if isWall[ck.r][ck.c-1] ==False and is_in_range(ck.r,ck.c-1) and not ISKNIGHT: # <- in check isWall, is knight (not me)
#                     print("can move")
#                     return 1, _
#                 elif isWall[ck.r][ck.c-1] : 
#                     print("cannot move the wall is on the way")
#                     return 2, _
#                 elif not is_in_range(ck.r,ck.c-1) : 
#                     print("cannot move out of the field")
#                     return 2, _
#                 elif ISKNIGHT: 
#                     print("should push knight first")
#                     return 0, tmp


# L, N, Q = map(int, input().split())

# world = []

# for _ in range(L):
#     world.append(list(map(int, input().split())))

# isTrap = [[False] * L for _ in range(L)]
# isWall = [[False] * L for _ in range(L)]
# for _ in range(L):
#     for j in range(L):
#         if world[_][j] == 1:
#             isTrap[_][j] = True
#         elif world[_][j] == 2:
#             isWall[_][j] = True

# q = deque()
# # isKnight=[[False for _ in range(L)] for _ in range(L)]
# iter =0
# for _ in range(N):
#     k = kisa()
#     k.r, k.c, k.h, k.w, k.HP = list(map(int, input().split()))
#     k.id = iter
#     iter +=1
#     q.append(k)
#     print(k.h)
#     # for i in range(k.h):
#     #     for j in range(k.w):
#     #         isKnight[k.r-1+i][k.c-1+j] = True

# order = deque()
# for _ in range(Q):
#     a = list(map(int, input().split()))
#     a[0] -= 1
#     order.append(a)

# def move_knight(ck,d):    
#     if d == 0 and 0< ck.r:
#         ck.r -=1
#     elif d == 1 and ck.c < L:
#         ck.c +=1
#     elif d == 2 and ck.r < L:
#         ck.r +=1
#     elif d == 3 and 0 < ck.c:
#         ck.c -=1
    
# print_init(world, isTrap, isWall, q, order)
# flag = -1
# while order:
#     n, d = order.popleft()
#     ck = q[n-1] # n 번째 기사 출격 대기중
#     flag, num = can_move(ck, d)
#     while flag == 0 : #다른 기사 밀어내기 해야됨
#         #다른 기사가 어떤 기사인지 알면 좋겠는데...
#         #어떤 기사냐? 바로바로 num 번째 기사
#         nk = q[num]
#         flag, num = can_move(nk,d)    
#         #기사 밀기
#     if flag == 1 : #그냥 이동
#         move_knight(ck,d)
#     elif flag == 2 : #이동 불가
#         continue
    
#     # 이동 하고 나서 처음에 오더 받은 기사 빼고 지뢰 밟은놈 다 조지기
#     # Write your code Here
#     for chr in range(L):
#         for chc in range(L):
#             for kngts in q:
#                 if kngts.id != d and isTrap[chr][chc]==True:
#                     kngts.HP -=1
    
# ans = 0
# for NTR in q:
#     ans +=NTR.HP

# print (ans)
#     #n번째 기사 이동 가능?
#     # 이동 불가능 (벽, 범위 밖) -> 다음 명령어
#     # 목적지에 기사 있음 (밀어내야됨) -> 이동 가능?
# 방향: 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [ 0, 1, 0,-1]

class Unit:
    def __init__(self, uid, si, sj, h, w, k):
        self.uid = uid
        self.si = si
        self.sj = sj
        self.h = h
        self.w = w
        self.k = k

    def position_after_move(self, dr):
        return self.si + di[dr], self.sj + dj[dr]

    def update_position(self, dr):
        self.si += di[dr]
        self.sj += dj[dr]

    def get_area(self, dr=None):
        # 이동 후 영역 리턴 (이동 전이면 dr=None)
        si = self.si + di[dr] if dr is not None else self.si
        sj = self.sj + dj[dr] if dr is not None else self.sj
        return si, sj, self.h, self.w

    def take_damage(self, dmg):
        self.k -= dmg

    def is_dead(self):
        return self.k <= 0

N, M, Q = map(int, input().split())
arr = [[2]*(N+2)]+[[2]+list(map(int, input().split()))+[2] for _ in range(N)]+[[2]*(N+2)]

units = {}
init_k = [0]*(M+1)

for m in range(1, M+1):
    si, sj, h, w, k = map(int, input().split())
    units[m] = Unit(m, si, sj, h, w, k)
    init_k[m] = k

def check_collision(a1, a2):
    si1, sj1, h1, w1 = a1
    si2, sj2, h2, w2 = a2
    return si1 <= si2 + h2 - 1 and si1 + h1 - 1 >= si2 and \
           sj1 <= sj2 + w2 - 1 and sj1 + w1 - 1 >= sj2

def push_unit(start_id, dr):
    q = [start_id]
    pset = {start_id}
    damage = [0] * (M + 1)

    while q:
        cur_id = q.pop(0)
        cur_unit = units[cur_id]
        ni, nj, h, w = cur_unit.get_area(dr)

        for i in range(ni, ni+h):
            for j in range(nj, nj+w):
                if arr[i][j] == 2:
                    return
                if arr[i][j] == 1:
                    damage[cur_id] += 1

        for other_id, other_unit in units.items():
            if other_id in pset:
                continue
            if check_collision((ni, nj, h, w), other_unit.get_area()):
                q.append(other_id)
                pset.add(other_id)

    damage[start_id] = 0

    for idx in pset:
        unit = units[idx]
        if unit.k <= damage[idx]:
            del units[idx]
        else:
            unit.update_position(dr)
            unit.take_damage(damage[idx])

for _ in range(Q):
    idx, dr = map(int, input().split())
    if idx in units:
        push_unit(idx, dr)

ans = 0
for idx, unit in units.items():
    ans += init_k[idx] - unit.k
print(ans)