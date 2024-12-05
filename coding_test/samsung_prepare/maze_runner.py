#20241206 19:40 init

import sys

def show_world(world):
    for _ in range(N):
        print(world[_])
    print("* * * * * * * * *")

input = sys.stdin.readline

N, M, K = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(N)]

position = [list(map(int, input().split())) for _ in range(M)]

door = list(map(int, input().split()))

show_world(world)

# condition :   1) 빈 칸은 이동 가능
#               2) 벽은 이동 불가 (1 ~ 9)의 내구도
#               3) 벽은 회전시, 내구도 1 깎임
#               4) 내구도가 0이 되면 빈 칸 됨
#               5) 출구에 도착하면 즉시 탈출
# TODO [1] :