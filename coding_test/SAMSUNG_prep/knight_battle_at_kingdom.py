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

from collections import deque

class kisa:
    r = 0
    c = 0
    h = 0
    w = 0
    HP = 0
    id = 0
def print_init(world, isTrap, isWall, q, order):

    print("\n\n * * * init world * * *\n")
    print(world)
    print("\n\n * * * init trap * * *\n")
    print(isTrap)
    print("\n\n * * * init wall * * *\n")
    print(isWall)

    print("\n\n * * * init knights * * *\n")
    print(q)

    print("\n\n * * * init orders * * *\n")
    print(order)


L, N, Q = map(int, input().split())

world = []

for _ in range(L):
    world.append(list(map(int, input().split())))

def pad_with_2(matrix, item):
    if not matrix:
        return [[item, item], [item, item]]  # 빈 행렬 처리

    n_rows = len(matrix)
    n_cols = len(matrix[0])
    padding_row = [item] * (n_cols + 2)

    # 사이 중간 행은 좌우에 2를 추가
    padded_matrix = [padding_row]  # top
    for row in matrix:
        padded_matrix.append([item] + row + [item])
    padded_matrix.append(padding_row)  # bottom

    return padded_matrix

world = pad_with_2(world, 2)

print(world)

isTrap = [[False] * L for _ in range(L)]


isTrap = pad_with_2(isTrap, False)

for _ in range(L+2):
    for j in range(L+2):
        if world[_][j] == 1:
            isTrap[_][j] = True

q = deque()
# isKnight=[[False for _ in range(L)] for _ in range(L)]
iter =0
init_HP = 0
for _ in range(N):
    k = kisa()
    k.r, k.c, k.h, k.w, k.HP = list(map(int, input().split()))
    k.id = iter
    init_HP +=k.HP #피 몇 깎였는지가 중요함 -> 처음피 총합 저장
    iter +=1
    q.append(k)
    
order = deque()
for _ in range(Q):
    order.append(list(map(int, input().split())))

while order:
    i, d = order.popleft()
    flag, nk=canGo(ck,d)
    if flag == 1: # 갈 수 있음
        Move(ck,d) #기사 이동
        for kgt in dother:
            if kgt.id == i+1 : 
                continue #명령받고 이동한놈
                for row in range(kgt.h):
                    for col in range(kgt.w):
                        if isTrap[kgt.r + row][kgt.c + col] == True:
                            kgt.HP -=1
                            if kgt.HP == 0 : del q[kgt.id]

    elif flag == 2: # 기사 때문에 갈 수 없음
        another = deque()
        dother = deque()
        havetomove= deque()
        another.append(ck)
        dother.append(ck)
        flag, ck = canGo(nk,d)

        if flag == 3: 
            another = deque()
            dother = deque()
            break



# 갈 수 있음
#     지금 기사 이동
#     i, d = order.popleft()
#     밀려진 기사가 밟았는지 확인
#     for kgt in 디아더 창고:
#         if kgt.id == i+1 : continue
#         for _ in range(kgt.h):
#             for j in range(kgt.w):
#                 if isTrap[kgt.r + _][kgt.c + j] == True:
#                     kgt.HP -=1
#                     만약 기사 사망하면 del q[kgt.id]

# 기사 때문에 갈 수 없음 
#     어나더 창고, 디아더 창고 초기화
#     지금 기사 어나더 창고에 넣고, 밀린기사 확인하기 위한 디아더 창고에 넣고, 길막하는 기사 이동 할 수 있는지 확인
#     길막하는 기사가 둘 다 갈 수 있는지, 그러려면, 이동해야될 놈에 append() 
#     flag = True <- 이놈은 밀릴 놈이 있음을 증명
#     하나씩 뺴면서 갈 수 있는지 체크하고 LIFO pop() 쓰고
    
#     그중 막히는 놈 있으면 다음 명령어 는 벽때문에 갈 수 없음으로 여기서 따로 처리 X
    
# 벽 때문에 갈 수 없음
#     flag = False <- 밀릴놈이 있었는데 못움직임
#     다음 명령어 q.popleft()

# for _ in q:
#     최종 피 += _.HP

# print(처음피 - 최종 피)
