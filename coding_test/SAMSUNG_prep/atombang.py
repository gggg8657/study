class atom:
    def __init__(self):
        self.r = 0
        self.c = 0
        self.m = 0
        self.s = 0
        self.d = 0

from collections import deque

def check(cq):
    clpsed = deque()
    tmp = deque()
    for i in range(len(cq)):
        src = cq[i]
        clpsed = deque()
        for j in range(len(cq)):
            tar = cq[j]
            if src.r == tar.r and src.c == tar.c:
                clpsed.append(tar)
        if clpsed not in tmp and len(clpsed) >= 2:
            tmp.append(clpsed)
    if len(tmp) <= 0:
        return _, False
    else:
        return tmp, True

def Divide(tq, mem):
    tmp = deque()
    while mem:
        tmp = mem.popleft()
        total_m = 0
        total_s = 0
        direction = []
        while tmp:
            atom_n = tmp.popleft()
            tq.remove(atom_n)
            total_m += atom_n.m
            direction.append(abs(atom_n.d % 2))
            total_s += atom_n.s

        new_m = total_m // 5
        if new_m == 0:
            continue
        else:
            a, b, c, d = atom(), atom(), atom(), atom()
            a.m = b.m = c.m = d.m = new_m

        if min(direction) != max(direction):
            a.d, b.d, c.d, d.d = 1, 3, 5, 7
        else:
            a.d, b.d, c.d, d.d = 0, 2, 4, 6

        new_s = total_s // len(direction)
        a.s = b.s = c.s = d.s = new_s
        a.r = b.r = c.r = d.r = atom_n.r
        a.c = b.c = c.c = d.c = atom_n.c

        q.append(a)
        q.append(b)
        q.append(c)
        q.append(d)

    return tq, q

n, m, k = map(int, input().split())
dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
q = deque()

for _ in range(m):
    a = atom()
    a.r, a.c, a.m, a.s, a.d = map(int, input().split())
    q.append(a)

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
    if is_collapse:
        tmpq, q = Divide(tmpq, mem)

    for item in tmpq:
        q.append(item)

res = 0
for ato in q:
    res += ato.m

print(res)