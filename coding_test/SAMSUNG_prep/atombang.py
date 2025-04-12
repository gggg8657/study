from collections import deque, defaultdict
import sys
input = sys.stdin.readline

class atom:
    def __init__(self, id):  # 고유 ID 부여
        self.id = id
        self.r = 0
        self.c = 0
        self.m = 0
        self.s = 0
        self.d = 0

def check(cq):
    pos_dict = defaultdict(deque)
    for atom in cq:
        pos_dict[(atom.r, atom.c)].append(atom)

    tmp = deque()
    for atoms in pos_dict.values():
        if len(atoms) >= 2:
            tmp.append(atoms)

    return tmp, True if tmp else (_, False)

def Divide(tq_dict, mem, unique_id):
    new_atoms = deque()

    while mem:
        tmp = mem.popleft()
        total_m = 0
        total_s = 0
        direction = []
        r = c = -1
        ids_to_remove = []

        while tmp:
            atom_n = tmp.popleft()
            ids_to_remove.append(atom_n.id)
            total_m += atom_n.m
            total_s += atom_n.s
            direction.append(atom_n.d % 2)
            r, c = atom_n.r, atom_n.c  # 위치 기록

        for _id in ids_to_remove:
            if _id in tq_dict:
                tq_dict.pop(_id)

        new_m = total_m // 5
        if new_m == 0:
            continue

        new_s = total_s // len(direction)
        dirs = [1, 3, 5, 7] if min(direction) != max(direction) else [0, 2, 4, 6]

        for d in dirs:
            a = atom(unique_id)
            unique_id += 1
            a.r, a.c = r, c
            a.m = new_m
            a.s = new_s
            a.d = d
            new_atoms.append(a)

    return tq_dict, new_atoms, unique_id

# 입력 처리
n, m, k = map(int, input().split())
dr, dc = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]

q = deque()
for i in range(m):
    a = atom(i)
    a.r, a.c, a.m, a.s, a.d = map(int, input().split())
    q.append(a)

unique_id = m  # 새 원자에 부여할 고유 ID 시작

# 시뮬레이션 시작
for _ in range(k):
    tmpq = deque()
    while q:
        ca = q.popleft()
        nr = (ca.r + ca.s * dr[ca.d]) % n
        nc = (ca.c + ca.s * dc[ca.d]) % n
        ca.r = nr
        ca.c = nc
        tmpq.append(ca)

    mem, is_collapse = check(tmpq)
    tmpq_dict = {a.id: a for a in tmpq}

    if is_collapse:
        tmpq_dict, new_atoms, unique_id = Divide(tmpq_dict, mem, unique_id)
        for a in new_atoms:
            q.append(a)

    for a in tmpq_dict.values():
        q.append(a)

# 질량 합산 결과 출력
res = sum(a.m for a in q)
print(res)