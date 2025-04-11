class atom:
    def __init__(self):
        self.r = 0
        self.c = 0
        self.m = 0
        self.s = 0
        self.d = 0

import copy
import sys
input = sys.stdin.readline
def check(cq):
    clpsed = []
    tmp = deque()
    for i in range(len(cq)):
        src = cq[i]
        clpsed = deque()
        for j in range(len(cq)):
            tar = cq[j]
            if src.r == tar.r and src.c == tar.c: # 겹쳤으면, 
                clpsed.append(tar)
        if clpsed not in tmp and len(clpsed)>=2: 
            tmp.append(clpsed)
    if len(tmp)<=0: 
        return _, False
    else : 
        return tmp, True

def Divide(tq,mem):
    # del_list = []
    tmp = deque()
    while mem:
        tmp=mem.popleft()
        total_m = 0
        total_s = 0
        direction = []
        while tmp:
            atom_n = tmp.popleft()
            tq.remove(atom_n)
            total_m += atom_n.m
            
            direction.append(abs(atom_n.d %2))
            total_s += atom_n.s

        #summation done
        # new m
        new_m = total_m//5 
        if new_m == 0: 
            continue    #질량 나눴더니 0 됨 원자 소멸
                        # 원래 있던 q 에서도 날려줘야 되는데 어쩌노 이미 popleft 하면서 뺴고, 분리 하고 다시 넣으므로 무관
        else : 
            a, b, c ,d = atom(), atom(), atom(), atom()
            a.m = b.m = c.m = d.m = new_m

        # new direction
        if min(direction) != max(direction): # 배열 안에 0 과 1 이 모두 있음
            a.d, b.d, c.d, d.d = 1, 3, 5, 7
        else : 
            a.d, b.d, c.d, d.d = 0, 2, 4, 6 #한가지 종류로 됨

        # new speed
        new_s = total_s // len(direction) # 합쳐진 원자의 개수
        a.s = b.s = c.s = d.s = new_s

        # new r, c
        a.r = b.r = c.r = d.r = atom_n.r
        a.c = b.c = c.c = d.c = atom_n.c
        q.append(a)
        q.append(b)
        q.append(c)
        q.append(d)
        
    return tq,q
        

        
n , m , k = map(int, input().split())

from collections import deque

dr, dc = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]

q = deque()
for _ in range(m):
    a = atom()
    a.r, a.c, a.m, a.s, a.d = map(int, input().split())
    q.append(a)

for _ in range(k):
    tmpq = [] #이동된 원자 위치 저장할 q 초기화
    while q:
        ca = q.popleft()
        nr = (ca.r + ca.s * dr[ca.d]) % n
        nc = (ca.c + ca.s * dc[ca.d]) % n
        ca.r = nr
        ca.c = nc
        tmpq.append(ca) #이동 후 원자의 위치 저장
        # if 0<=nr<n and 0<=nc<n:
        #     ca.r = nr
        #     ca.c = nc
        #     tmpq.append(ca)

    mem, is_collapse = check(tmpq) # 합쳐진거 있는지 확인 mem은 deque로 구성 : 합쳐진 것들의 집합을 mem 에 포함 즉 mem.popleft() -> 합쳐진거 집합 1 mem.popleft().popleft() -> 합쳐진거 집합 1의 원자 하나
    if is_collapse:  # 합쳐진게 있음
        tmpq,q = Divide(tmpq, mem)  # update q and does not return tmpq 안에 있는거도 날려줘야됨

    for item in tmpq: q.append(item) #이동된 원자의 위치 q에 추가
    # tmpq 에 사라진 원소도 남아있음...



res = 0
for ato in q:
    res += ato.m

print(res)
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

