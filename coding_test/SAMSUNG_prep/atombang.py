class atom:
    def __init__(self):
        self.r = 0
        self.c = 0
        self.m = 0
        self.s = 0
        self.d = 0



n , m , k = map(int, input().split())

from collections import deque

dr, dc = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]

q = deque()
for _ in range(m):
    a = atom()
    a.r, a.c, a.m, a.s, a.d = map(int, input().split())
    q.append(a)

<<<<<<< HEAD
for _ in range(k):
    tmpq = deque() #이동된 원자 위치 저장할 q 초기화
    while q:
        ca = q.popleft()
        nr, nc = ca.r + ca.s*dr[ca.d], ca.c + ca.s*dc[ca.d]
        ca.r = nr
        ca.c = nc
        tmpq.append(ca) #이동 후 원자의 위치 저장
        # if 0<=nr<n and 0<=nc<n:
        #     ca.r = nr
        #     ca.c = nc
        #     tmpq.append(ca)
=======
while q and k !=0:
    ca = q.popleft()
>>>>>>> parent of 6d81c8c (atom bang 중간)

'''
init -> 1sec -> if check(q) == True : # 합쳐진게 있음
                    원자분해 -> 4개로 ()

원자분해 -> 4개로 (합쳐진 원자들):
    질량 = (합쳐진 질량)//5
    if 질량 == 0 -> del 합쳐진 원자들
    else:
        속력 = 합쳐진 원자 속력 / 합쳐진 원자 개수
        if 합쳐진 원자 상 하 좌 우 || 대각 대각 대각 대각 :
            방향 = 상하좌우
        else : 방향 = 4대각
        
        q. append(원자분해된 4개의 원자) 
        
    
                        
'''

