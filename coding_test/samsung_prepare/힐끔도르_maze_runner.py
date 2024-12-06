#20241206 19:40 init

# condition :   1) 빈 칸은 이동 가능
#               2) 벽은 이동 불가 (1 ~ 9)의 내구도
#               3) 벽은 회전시, 내구도 1 깎임
#               4) 내구도가 0이 되면 빈 칸 됨
#               5) 출구에 도착하면 즉시 탈출
# TODO  [1] : move => narr[nr][nc] = arr[r][c]
#       [2] : rotate => narr[sizeof(arr[0])-1-col][row] = arr[row][col]
#       def rotate_90(b):
#           n,m = len(b),len(b[0])
#           temp_board = [[-1 for _ in range(m)] for _ in range(n)]
#           for i in range(n):
#               for j in range(n):
#                   temp_board[m-j-1][i] = b[i][j]
#           return temp_board
#       [3] : exit => arr[r][c] 없애주기
#       [4] : each iter => arr[r][c] = narr[r][c]

import sys

def show_world(world):
    for _ in range(N):
        print(world[_])
    print("* * * * * * * * *")

def copy_world(tar, src):
    for r in range(N):
        for c in range(N):
            tar[r][c] = src[r][c]

def rotate_world(arr):
    n,m = len(arr), len(arr[0])
    for r in range(n):
        for c in range(m):
            if arr[r][c] >=1 : arr[r][c]-=1
            narr[m-c-1][r] = arr[r][c]
    return narr

def init_world(arr):
    for cnt in range(len(position)):
        r,c = position[cnt]
        arr[r][c] -=1 # -1 is human location
    arr[door[0]][door[1]] = -11 # -11 is door

def asscio_square(arr):
    # 비상구 <-> 모든 사람간의 가장 짧은 가로 또는 세로 거리 구하기
    m = N
    # print(m)
    for row in range(N):
        for col in range(N):
            if -11 < arr[row][col] < 0:  # 사람임
                # print(f"row is {row}, col is {col}, arr[{row}][{col}] is {arr[row][col]}")
                # print(f"{erow}, {row} ,{ecol}, {col}, {m}")
                # show_world(arr)
                m = min(m, max(abs(erow - row),abs(ecol - col)))
                # print(f"m is updated {m}")

    # 00 부터 , 순회하면서 길이 L 인 정사각형에 비상구와 사람 하나 이상 있는지 체크
    for srow in range(N - m):
        for scol in range(N - m):
            if srow <= erow <= srow + m and scol <= ecol <= scol + m:
                for i in range(srow, srow + m + 1):
                    for j in range(scol, scol + m + 1):
                        if -11 < arr[i][j] < 0:
                            return srow, scol, m + 1

    # No valid square found

def find_exit(arr):
    for row in range(N):
        for col in range(N):
            if arr[row][col]== -11:
                return row,col

input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

narr = [[0 for _ in range(N)] for _ in range(N)]

copy_world(narr, arr)

position = [list(map(lambda x:int(x)-1, input().split())) for _ in range(M)]

door = list(map(lambda x:int(x)-1, input().split()))

init_world(arr)


ans = 0
cnt = M
erow,ecol = door
for _ in range(K):
    narr = [x[:] for x in arr]
    for row in range(N):
        for col in range(N):
            if -11<arr[row][col]<0: # human case
                dist = abs(erow-row)+abs(ecol-col)
                # 네 방향 (상 하 좌 우), in range, not wall, dist 보다 작으면
                for drow, dcol in ((-1,0),(1,0),(0,-1),(0,1)):
                    nrow, ncol = row+drow, col+dcol
                    if 0<=nrow<N and 0<=ncol<N and arr[nrow][ncol]<=0 and dist>(abs(erow-nrow)+(abs(ecol-ncol))):
                        ans+=arr[row][col]      #현재 인원수가 이동하는 것이니 이동 거리에 누적
                        narr[row][col]-=arr[row][col]       #이동 처리
                        if arr[nrow][ncol]==-11:    #exit
                            cnt+=arr[row][col]      #exit count ++
                        else:                       #just road or human
                            narr[nrow][ncol] += arr[row][col]   #이동 인원 추가
                        break
    arr = narr
    if cnt ==0:
        break
    srow, scol, L = asscio_square(arr) #비상구 포함한 사각형 찾는거

    narr = [x[:] for x in arr]
    for row in range(L):
        for col in range(L):
            narr[srow+row][scol+col] = arr[srow+L-1-col][scol+row]
            if narr[srow+row][scol+col]>0:      #벽이면 회전시 1 감소
                narr[srow+row][scol+col] -=1

    arr = narr
    # 회전으로 달라짐 -> 비상구 위치 저장
    erow, ecol = find_exit(arr)
    # show_world(arr)
print(-ans)
print(erow+1, ecol+1)