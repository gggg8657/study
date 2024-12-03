import sys
from copy import deepcopy

def print_world(world, n):
    for _ in range(n):
        print(world[_])
    print("* * * * * * * * * * * * *")

def MinVal(arr):
    return min([sum(lst) for lst in arr])

def rot(arr,qry):
    (r,c,s) = qry
    r,c = r-1, c-1
    narr = deepcopy(arr)
    for i in range(1, s+1):
        rr, cc = r-i, c+i
        for w in range(4):
            for d in range(i*2):
                rrr, ccc = rr + dx[w], cc + dy[w]
                narr[rrr][ccc] = arr[rr][cc]
                rr,cc = rrr,ccc
    return narr

def DFS(arr, qry):
    global rst
    if sum(qry) == K:
        rst = min (rst, MinVal(arr))
        return
    for i in range(K):
        if qry[i]:
            continue
        narr = rot(arr, cal_info[i])
        qry[i] = 1
        DFS(narr, qry)
        qry[i]=0

input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = [list(map(int, input().split()))for _ in range(N)]

# print_world(arr,N)

cal_info = []
point_info = []
#한 칸씩 돌린다는 의미이다.
for k in range(K):
    r,c,s = map(int, input().split())
    lt = (r-s,c-s)
    rt = (r-s,c+s)
    lb = (r+s,c-s)
    rb = (r+s,c+s)
    cal_info.append((r,c,s))
    point_info.append([lt,rt,rb,lb])
# print(cal_info)
# print(point_info)

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

rst = 10000


DFS(arr, [0 for i in range(K)])
print(rst)




