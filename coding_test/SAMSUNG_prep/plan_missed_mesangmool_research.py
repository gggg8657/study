
import sys
input = sys.stdin.readline

from collections import deque

N, Q = map(int, input().split())

q = deque()
id =0
for _ in range(Q):
    id+=1
    tmp = list(map(int, input().split()))
    tmp.append(id)
    q.append(tmp) # r1, c1, r2, c2, id

world=[[0 for _ in range(N)]for _ in range(N)]

dr, dc = [-1,0,1,0],[0,-1,0,1]

# def check(tq):
#     visited = [[False for _ in range(N)]*N]
#     while tq:
#         r,c = tq.popleft()
#         if world[r][c] == 0:
#             continue
#         for d in range(4):
#             nr, nc = r+dr[d], c + dc[d]
#             if 0<nr<=N and 0<nc<=N and world[nr][nc] == world[r][c] and not visited[nr][nc]:
#                 tq.append((nr,nc))
#                 visited[nr][nc] = True
def erase(r1,c1,r2,c2,it):
    for r in range(r1,r2):
        for c in range(c1,c2):
            if world[r][c] == id :
                world[r][c] = 0
    return True

def check(tq, id):
    """
    :param tq:
    :return:
    만약에 r1, c1, r2, c2, id가 있어, 그럼 맵 다 만들고 그 범위 순회해
    근데, 이게? 만약에 같은 r을 두고 보는데 (r1<r<r2) (c1<c<c2) 일때, c1 ~ c2 까지 쭉 다른id야? 그럼 그 r1,r2,c1,c2 범위에서,
    id인것들 0으로 만들어
    """
    flag_col = False
    flag_row = False
    erased= False
    for _ in range(id):
        r1,r2,c1,c2,it = tq[_]
        for r in range(r1+1,r2-1):
            for c in range(c1+1,c2-1):
                if world[r][c] != it:
                    flag_col=True
                else : flag_col=False
            if flag_col == True: #이거 날려야되는 가로줄임 즉, 잘림
                erased = erase(r1,c1,r2,c2,it)
                if erased:
                    tq.pop(_)
                    # print(tq)
                    return tq
        for c in range(c1+1,c2-1):
            for r in range(r1+1,r2-1):
                if world[r][c] != it:
                    flag_row = True  #
                else:
                    flag_row = False
            if flag_row == True: #날려야될 세로줄, 잘림
                erased = erase(r1, c1, r2, c2, it)
                if erased:
                    tq.pop(_)
                    # print(tq)
                    return tq
    return tq
def find_value_in_2d_array(array, target_value):
    for row in array:
        for element in row:
            if element == target_value:
                return False
    print(f"{target_value} is not in {world}")
    return True
def put_it_in():
    tq = []
    while q:
        r1,c1,r2,c2,id = q.popleft()
        tq.append((r1,c1,r2,c2,id))
        for r in range(r1,r2):
            for c in range(c1,c2):
                world[r][c] = id
                # print_world(world)
                # print("*** *** ***")
        # 일단 넣었고,
        if id >= 2 and len(tq)>=2:
            tq = check(tq, len(tq))
            #TODO 지워진게 아니라, 완전 덥혀진거면, 삭제가 안되는 문제가 있음 요거 문제 있음
            poplist=[]
            for _ in range(len(tq)):
                if all(tq[_][4] not in row for row in world):
                    poplist.append(_)
            for idx in poplist:
                tq.pop(idx)
            print(tq)
        """
            use BFS to find divided pieces || or check it with (r,c)
            checking and erase from the world done
        """

        #TODO 그... 배양통? 으로 옮기기
        move_it()



def print_world(arr):
    for _ in range(N):
        print(arr[_])
def move_it(arr):
    for i in range(N):
        for j in range(N):

    pass
def cal():
    pass

def main():
    print_world(world)
    print("\n*** *** ***\n")
    put_it_in()
    print_world(world)
    print("\n*** *** ***\n")
    move_it()
    cal()

main()

"""
input:
8 4
2 2 5 6
2 3 5 8
2 0 5 3
1 1 6 6

"""
