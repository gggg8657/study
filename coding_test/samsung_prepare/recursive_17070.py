import sys

def print_world(world):
    n = len(world)
    for _ in range(n):
        print(world[_])
    print("* * * * * * * * * * * * * * *")

def movePipe(state, r, c):
    global ans
    if r==N-1 and c==N-1: ans+=1
    canMovH = c+1 < N and arr[r][c+1] ==0
    canMovV = r+1 < N and arr[r+1][c] ==0

    if canMovH and state != 1:
        movePipe(0,r,c+1)
    if canMovV and state != 0:
        movePipe(1,r+1,c)
    if canMovH and canMovV and arr[r+1][c+1]==0:
        movePipe(2,r+1,c+1)

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split()))for _ in range(N)]
# print_world(arr)

ans=0
movePipe(0,0,1)
print(ans)
