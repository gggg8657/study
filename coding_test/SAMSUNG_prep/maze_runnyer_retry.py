import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())

world = [list(map(int, input().split()))for _ in range(N)]

human_list=[]
for _ in range(M):
    tmp,tmp2 = list(map(int, input().split()))
    human_list.append((tmp-1,tmp2-1))
    world[tmp-1][tmp2-1] = -1 #human marking
print(human_list)
exit = list(map(int, input().split()))
exit[0]-=1
exit[1]-=1
world[exit[0]][exit[1]] = -99 #exit marking

def print_world(arr):
    for _ in range(N):
        print(arr[_])
def print_set():
    print_world(world)
    print(human_list)
    print("*** *** ***")

def check_box(r,c,i,j):
    init_r ,init_c,end_r, end_c = min(r,r+i), abs(min(c, c+j)), max(r,r+i), max(c,c+j)
    box_size = max(abs(i),abs(j))
    boxed = False
    # print(init_r,init_c,end_r,end_c)
    init_r, end_r, init_c, end_c = min(init_r, end_r), max(init_r, end_r), min(init_c,end_c), max(init_c,end_c)

    for row in range(init_r, end_r+1):
        for col in range(init_c, end_c+1):
            if world[row][col] == -1 and box_size!=0:
                boxed = True
                return init_r, init_c, end_r, end_c, boxed, box_size
    if boxed is False:
        return -1,-1,-1,-1, boxed, -1

# def rotate(arr, size):
#     new_arr = [[0 for _ in range(size)]for _ in range(size)]
#     for tmp_r in range(size):
#         for tmp_c in range(size):
#             new_arr[tmp_c][size-1-tmp_r] = arr[tmp_r][tmp_c] #0,0 <- 0,1 / 0,1 <- 1,1 / 1,0 <- 0,0 /
#             # 0,0 <- 1,0/ 0,1 <- 0,0 / 1,0 <- 1,1/ 1,1 <- 0,1 <= row <- col / col <-
#
#     for tp in range(size):
#         for tp2 in range(size):
#             if arr[tp][tp2] == -1: #human
#                 human_list.remove((tp,tp2))
#                 #update hum list
#             arr[tp][tp2] = new_arr[tp][tp2]
#             if arr[tp][tp2] >= 1:
#                 arr[tp][tp2] -=1 #rotated wall racking
#             if arr[tp][tp2] == -1: #update human pos
#                 human_list.append((tp,tp2))
#
#     return arr

dr, dc = [-1,0,1,0],[0,-1,0,1]


# print_world(world)
# print("*** *** *** \n")
# world = rotate(world,2)
# print_world(world)

#

def rotate(arr,size,cbir,cbic,cber,cbec):
    new_arr = [[0 for _ in range(size+1)]for _ in range(size+1)]
    for tmp_r in range(size):
        for tmp_c in range(size):
            new_arr[tmp_c][size-1-tmp_r] = arr[cbir+tmp_r][cbic+tmp_c] #0,0 <- 0,1 / 0,1 <- 1,1 / 1,0 <- 0,0 /
            # 0,0 <- 1,0/ 0,1 <- 0,0 / 1,0 <- 1,1/ 1,1 <- 0,1 <= row <- col / col <-
    for tmp_i in range(size):
        for tmp_j in range(size):
            if arr[cbir+tmp_i][cbic+tmp_j] == -1:
                human_list.remove((cbir+tmp_i,cbic+tmp_j)) #update hum list
            arr[cbir+tmp_i][cbic+tmp_j] = new_arr[tmp_i][tmp_j]
            if arr[cbir+tmp_i][cbic+tmp_j] >= 1:
                arr[cbir + tmp_i][cbic + tmp_j] -=1 #rotated wall racked
            if arr[cbir+tmp_i][cbic+tmp_j] == -1:
                human_list.append((cbir+tmp_i, cbic+tmp_j))
            if arr[cbir+tmp_i][cbic+tmp_j] == -99:
                exit[0], exit[1] = cbir+tmp_i, cbic+tmp_j

    return arr

def check_dist(r,c):
    return abs(exit[0]-r) + abs(exit[1]-c)
for times in range(K):
    tmp_list=[]

    for human_pos in human_list:
        #find move directions
        cr,cc = human_pos[0], human_pos[1]
        cd = check_dist(cr,cc)
        for d in range(4):
            nr, nc = dr[d]+cr, dc[d]+cc
            tmpd = check_dist(nr,nc)
            if 0<=nr<N and 0<=nc<N and world[nr][nc] <1 and tmpd<cd:
                if world[nr][nc] == -99:
                    human_list.remove((cr,cc))#exit success
                    world[cr][cc] = 0
                    break
                else:
                    if (cr,cc) ==(2,4):
                        print("SHIT")
                    human_list.remove((cr,cc))

                    tmp_list.append((nr,nc))
                    world[cr][cc], world[nr][nc]  = 0, -1 #이거 반복 다 돌면? 이동 끝임
    for _ in range(len(tmp_list)):
        if tmp_list[_] not in human_list: human_list.append(tmp_list[_])
    print_set()
    print("MOVED")
    # continue
    # 그럼 여기가 이동은 끝난거. 이제 박스 찾고 회전.
    cbir, cbic, cber, cbec, cbs = 0,0,0,0,90
    # max_size = exit[0], exit[1] (위로 올라갈 수 있는 길이 exit[0], 좌로 갈 수 있는 길이 exit[1] <- 중 min )
    # 오른쪽으로 갈 수 있는 길이 N-exit[1], 아래로 갈 수 있는 길이 N- exit[0] 중 min
    # - min(exit[0], exit[1]) , min(N-exit[1], N-exit[0]), 1
    a = -min(N-exit[0], N-exit[1])
    b = min(N-exit[1], N-exit[0])
    for i in range(-b+1, b-1, 1):
        # ?print(cbs,cbir,cbic,cber,cbec)
        print(f"from {-b} to {b} now lookin at {i}")
        nbir, nbic, nber, nbec, boxed, nbs= check_box(exit[0],exit[1],i,i)
        print("BEFORE",cbs, cbir, cbic, cber, cbec)
        if nbs < cbs and boxed:
            cbir, cbic, cber, cbec, cbs =nbir, nbic, nber, nbec, nbs
            print("AFTER", cbs, cbir, cbic, cber, cbec)
            #new box from row to row and from col to col done
    world = rotate(world,cbs+1,cbir,cbic,cber,cbec)
    print(exit)
    print_set()
    print("ROTATED")


