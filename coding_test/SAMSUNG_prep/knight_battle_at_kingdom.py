from collections import deque

class kisa:
    def __init__(self):
        self.r = 0
        self.c = 0
        self.h = 0
        self.w = 0
        self.HP = 0
        self.id = 0
        self.damage = 0  # 누적 피해량

def pad_with_2(matrix, item):
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    padding_row = [item] * (n_cols + 2)
    padded_matrix = [padding_row]
    for row in matrix:
        padded_matrix.append([item] + row + [item])
    padded_matrix.append(padding_row)
    return padded_matrix

def Move(ck, d):
    if d == 0: ck.r -= 1
    elif d == 1: ck.c += 1
    elif d == 2: ck.r += 1
    elif d == 3: ck.c -= 1
    return ck

def get_push_chain(ck, d, visited):
    if ck.id in visited:
        return []
    visited.add(ck.id)
    tmpr = ck.r + ([-1, 0, 1, 0][d])
    tmpc = ck.c + ([0, 1, 0, -1][d])
    chain = []
    for row in range(ck.h):
        for col in range(ck.w):
            nr, nc = tmpr + row, tmpc + col
            if world[nr][nc] == 2:
                return None
            for k in q:
                if k == ck or isDead[k.id]:
                    continue
                if k.r <= nr < k.r + k.h and k.c <= nc < k.c + k.w:
                    res = get_push_chain(k, d, visited)
                    if res is None:
                        return None
                    chain.extend(res)
    chain.append(ck)
    return chain

# 입력
L, N, Q = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(L)]
world = pad_with_2(world, 2)
R, C = len(world), len(world[0])

isTrap = [[False] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if world[i][j] == 1:
            isTrap[i][j] = True

q = deque()
isDead = [False] * N

for idx in range(N):
    k = kisa()
    k.r, k.c, k.h, k.w, k.HP = map(int, input().split())
    k.id = idx
    q.append(k)

order = deque()
for _ in range(Q):
    order.append(list(map(int, input().split())))

# 명령 처리
while order:
    i, d = order.popleft()
    commander_id = i - 1

    for k in q:
        if k.id == commander_id and not isDead[k.id]:
            ck = k
            break
    else:
        continue

    visited = set()
    push_list = get_push_chain(ck, d, visited)
    if push_list is None:
        continue

    for k in push_list:
        Move(k, d)

    for k in push_list:
        if k.id == commander_id or isDead[k.id]:
            continue
        damage = 0
        for row in range(k.h):
            for col in range(k.w):
                if isTrap[k.r + row][k.c + col]:
                    damage += 1
        if k.HP - damage <= 0:
            isDead[k.id] = True
        else:
            k.HP -= damage
            k.damage += damage

# 누적 피해 계산 (생존자만)
print(sum(k.damage for k in q if not isDead[k.id]))
