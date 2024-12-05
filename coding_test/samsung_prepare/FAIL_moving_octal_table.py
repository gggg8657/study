from collections import deque

MAX=4

a=[None]
for _ in range(MAX):
    data=list(str(input()))
    q=deque()
    for ele in data:
        q.append(int(ele))
    a.append(q)

def process(n,dir):

    # n번째로부터 왼쪽, 오른쪽으로 회전 대상 탐색
    d=[None]+[0]*MAX # 의자마다 회전할 방향 저장
    d[n]=dir
    # 왼쪽 순서대로 탐색
    for i in range(n,1,-1):
        if a[i][6]!=a[i-1][2]:
            d[i-1]=-d[i]
    # 오른쪽 순서대로 탐색
    for i in range(n,MAX):
        if a[i][2]!=a[i+1][6]:
            d[i+1]=-d[i]

    for i in range(1,MAX+1):
        dir=d[i]
        if dir==0:
            continue
        a[i].rotate(dir)

K=int(input())
for _ in range(K):
    n,d=map(int,input().split())
    process(n,d)

ans=a[1][0]*1+a[2][0]*2+a[3][0]*4+a[4][0]*8
print(ans)