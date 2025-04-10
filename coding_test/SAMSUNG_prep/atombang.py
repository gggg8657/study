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

while q and k !=0:
    ca = q.popleft()

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

