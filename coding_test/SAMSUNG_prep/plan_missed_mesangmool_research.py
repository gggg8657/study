class QUERY:
    def __init__(self, r1, c1, r2, c2):
        self.r1 = r1
        self.c1 = c1
        self.r2 = r2
        self.c2 = c2


class MICRO:
    def __init__(self, id, minR, minC, maxR, maxC, count):
        self.id = id
        self.minR = minR
        self.minC = minC
        self.maxR = maxR
        self.maxC = maxC
        self.count = count


class RC:
    def __init__(self, r, c):
        self.r = r
        self.c = c


MAX = 20
MAX_Q = 55

T = 1
N, Q = 0, 0
MAP = [[0] * MAX for _ in range(MAX)]
query = [None] * MAX_Q
micro = []
mcnt = 0
dead = [False] * MAX_Q
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
queue = []


def input_data():
    global N, Q
    N, Q = map(int, input().split())
    for q in range(1, Q + 1):
        r1, c1, r2, c2 = map(int, input().split())
        query[q] = QUERY(r1, c1, r2, c2)


def print_map(map):
    for r in range(N):
        for c in range(N):
            print(map[r][c], end=' ')
        print()
    print()


def insert(id, r1, c1, r2, c2):
    for r in range(r1, r2):
        for c in range(c1, c2):
            MAP[r][c] = id

visited=[[False for _ in range(N)]for _ in range(N)]

def bfs(r, c):
    rp, wp = 0, 0
    minR, maxR = r, r
    minC, maxC = c, c
    queue.append(RC(r, c))
    visited[r][c] = True

    while rp < len(queue):
        out = queue[rp]
        rp += 1
        for i in range(4):
            nr = out.r + dr[i]
            nc = out.c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if MAP[out.r][out.c] != MAP[nr][nc] or visited[nr][nc]:
                continue
            queue.append(RC(nr, nc))
            visited[nr][nc] = True
            if nr < minR: minR = nr
            if nc < minC: minC = nc
            if nr > maxR: maxR = nr
            if nc > maxC: maxC = nc

    ret = MICRO(MAP[r][c], minR, minC, maxR, maxC, len(queue))
    return ret


def find_live_micro():
    global mcnt
    mcnt = 0
    visited = [[False] * N for _ in range(N)]
    check = [False] * MAX_Q

    for r in range(N):
        for c in range(N):
            id = MAP[r][c]
            if id == 0 or dead[id] or visited[r][c]:
                continue
            m = bfs(r, c)
            if check[id]:
                dead[id] = True
                continue
            check[id] = True
            micro.append(m)

    micro_alive = [m for m in micro if not dead[m.id]]
    micro.clear()
    micro.extend(micro_alive)


def is_priority(a, b):
    if a.count != b.count:
        return a.count > b.count
    return a.id < b.id


def sort_micro():
    micro.sort(key=lambda m: (-m.count, m.id))


def check_move(newMAP, m, fr, fc):
    sr, sc, er, ec = m.minR, m.minC, m.maxR, m.maxC
    for r in range(sr, er + 1):
        for c in range(sc, ec + 1):
            if MAP[r][c] != m.id or MAP[r][c] == 0:
                continue
            newR = fr - sr + r
            newC = fc - sc + c
            if newR >= N or newC >= N or newMAP[newR][newC] != 0:
                return False
    return True


def move(newMAP, m, fr, fc):
    sr, sc, er, ec = m.minR, m.minC, m.maxR, m.maxC
    for r in range(sr, er + 1):
        for c in range(sc, ec + 1):
            if MAP[r][c] != m.id or MAP[r][c] == 0:
                continue
            newMAP[fr - sr + r][fc - sc + c] = m.id


def move_micro(newMAP, m):
    for r in range(N):
        for c in range(N):
            if check_move(newMAP, m, r, c):
                move(newMAP, m, r, c)
                return


def move_all():
    newMAP = [[0] * MAX for _ in range(MAX)]
    for m in micro:
        move_micro(newMAP, m)
    for r in range(N):
        for c in range(N):
            MAP[r][c] = newMAP[r][c]


def get_count(id):
    for m in micro:
        if m.id == id:
            return m.count
    return -1


def get_score(maxID):
    company = [[0] * MAX_Q for _ in range(MAX_Q)]
    for r in range(N):
        for c in range(N):
            if MAP[r][c] == 0:
                continue
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                id1 = MAP[r][c]
                id2 = MAP[nr][nc]
                if id1 == id2 or id2 == 0:
                    continue
                company[id1][id2] = True
                company[id2][id1] = True

    score = 0
    for i in range(1, maxID):
        for k in range(i + 1, maxID + 1):
            if not company[i][k]:
                continue
            count1 = get_count(i)
            count2 = get_count(k)
            score += (count1 * count2)
    return score


def simulate():
    for id in range(1, Q + 1):
        r1, c1, r2, c2 = query[id].r1, query[id].c1, query[id].r2, query[id].c2
        insert(id, r1, c1, r2, c2)
        find_live_micro()
        sort_micro()
        move_all()
        print(get_score(id))


def main():
    for tc in range(1, T + 1):
        input_data()
        simulate()


if __name__ == "__main__":
    main()