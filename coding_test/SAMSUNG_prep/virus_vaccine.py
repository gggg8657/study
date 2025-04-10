# 시발코드
# if M == 1:
#     for i in range(len(hosq)):
#         combq.append(hosq[i])
# elif M == 2:
#     for i in range(len(hosq)):
#         for j in range(i, len(hosq)):
#             if (hosq[i], hosq[j]) not in combq:
#                 combq.append([hosq[i], hosq[j]])
#             else: continue
# elif M == 3:
#     for k in range(len(hosq)):
#         for i in range(k+1, len(hosq)):
#             for j in range(i+1, len(hosq)):
#                 if (hosq[k], hosq[i], hosq[j]) not in combq:
#                     combq.append([hosq[k], hosq[i], hosq[j]])
#                 else: continue
# elif M == 4:
#     for l in range(len(hosq)):
#         for k in range(l, len(hosq)):
#             for i in range(k, len(hosq)):
#                 for j in range(i, len(hosq)):
#                     if (hosq[l], hosq[k], hosq[i], hosq[j]) not in combq:
#                         combq.append([hosq[l], hosq[k], hosq[i], hosq[j]])
#                     else: continue
# elif M == 5:
#     for m in range(len(hosq)):
#         for l in range(m, len(hosq)):
#             for k in range(l, len(hosq)):
#                 for i in range(k, len(hosq)):
#                     for j in range(i, len(hosq)):
#                         if (hosq[m], hosq[l], hosq[k], hosq[i], hosq[j]) not in combq:
#                             combq.append([hosq[m], hosq[l], hosq[k], hosq[i], hosq[j]])
#                         else: continue
# elif M == 6:
#     for n in range(len(hosq)):
#         for m in range(n, len(hosq)):
#             for l in range(m, len(hosq)):
#                 for k in range(l, len(hosq)):
#                     for i in range(k, len(hosq)):
#                         for j in range(i, len(hosq)):
#                             if (hosq[n], hosq[m], hosq[l], hosq[k], hosq[i], hosq[j]) not in combq:
#                                 combq.append([hosq[n], hosq[m], hosq[l], hosq[k], hosq[i], hosq[j]])
#                             else: continue
# elif M == 7:
#     for o in range(len(hosq)):
#         for n in range(o, len(hosq)):
#             for m in range(n, len(hosq)):
#                 for l in range(m, len(hosq)):
#                     for k in range(l, len(hosq)):
#                         for i in range(k, len(hosq)):
#                             for j in range(i, len(hosq)):
#                                 if (hosq[o], hosq[n], hosq[m], hosq[l], hosq[k], hosq[i], hosq[j]) not in combq:
#                                     combq.append([hosq[o], hosq[n], hosq[m], hosq[l], hosq[k], hosq[i], hosq[j]])
#                                 else: continue
# elif M == 8:
#     for p in range(len(hosq)):
#         for o in range(p, len(hosq)):
#             for n in range(o, len(hosq)):
#                 for m in range(n, len(hosq)):
#                     for l in range(m, len(hosq)):
#                         for k in range(l, len(hosq)):
#                             for i in range(k, len(hosq)):
#                                 for j in range(i, len(hosq)):
#                                     if (hosq[p], hosq[o], hosq[n], hosq[m], hosq[l], hosq[k], hosq[i], hosq[j]) not in combq:
#                                         combq.append([hosq[p], hosq[o], hosq[n], hosq[m], hosq[l], hosq[k], hosq[i], hosq[j]])
#                                     else: continue
# elif M == 9:
#     for q in range(len(hosq)):
#         for p in range(q, len(hosq)):
#             for o in range(p, len(hosq)):
#                 for n in range(o, len(hosq)):
#                     for m in range(n, len(hosq)):
#                         for l in range(m, len(hosq)):
#                             for k in range(l, len(hosq)):
#                                 for i in range(k, len(hosq)):
#                                     for j in range(i, len(hosq)):
#                                         if (hosq[q], hosq[p], hosq[o], hosq[n], hosq[m], hosq[l], hosq[k], hosq[i], hosq[j]) not in combq:
#                                             combq.append([hosq[q], hosq[p], hosq[o], hosq[n], hosq[m], hosq[l], hosq[k], hosq[i], hosq[j]])
#                                         else: continue
# elif M == 10:
#     for r in range(len(hosq)):
#         for q in range(r, len(hosq)):
#             for p in range(q, len(hosq)):
#                 for o in range(p, len(hosq)):
#                     for n in range(o, len(hosq)):
#                         for m in range(n, len(hosq)):
#                             for l in range(m, len(hosq)):
#                                 for k in range(l, len(hosq)):
#                                     for i in range(k, len(hosq)):
#                                         for j in range(i, len(hosq)):
#                                             if (hosq[r], hosq[q], hosq[p], hosq[o], hosq[n], hosq[m], hosq[l], hosq[k], hosq[i], hosq[j]) not in combq:
#                                                 combq.append([hosq[r], hosq[q], hosq[p], hosq[o], hosq[n], hosq[m], hosq[l], hosq[k], hosq[i], hosq[j]])
#                                             else: continue

from collections import deque
import copy
N, M = map(int, input().split())

world = []
newworld=[]
hosq = deque() #병원들 위치 기억
for _ in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 2:hosq.append([_,j])
        
    world.append(tmp)

newworld = copy.deepcopy(world)

combq = deque() # posq_1, posq_2 와 같은 형태로 queue를 저장
from itertools import combinations
combq= deque(combinations(hosq, M))

posq = deque() # [r_1, c_1], [r_2, c_2] ... 형태로 좌표를 저장

dr, dc = [-1,0,1,0], [0,1,0,-1]

step = 1

result=[]

ans = 0
APPENDRESULT = True
while combq:
    posq = deque(combq.popleft())
    while any(0 in row for row in world):
        tmpq=deque()
        while posq:
            r,c = posq.popleft()
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0<=nr<N and 0<=nc<N and world[nr][nc] == 0:
                    world[nr][nc]=step
                    tmpq.append([nr,nc])
                elif 0<=nr<N and 0<=nc<N and world[nr][nc] == 2:
                    tmpq.append([nr,nc])
                    world[nr][nc]=-1

        for item in tmpq: posq.append(item)
        step+=1

        if len(posq) <=0 and any(0 in row for row in world): 
            ans =-1
            APPENDRESULT = False
            break
    if len(combq)==0 and len(posq) == 0 and APPENDRESULT == False and len(result)==0: 
        result.append(ans)
    elif APPENDRESULT: 
        result.append(step-1)
        step =1
        world = copy.deepcopy(newworld)


if len(result) ==0:
    print(-1)    
else : print(min(result))
'''
3 1
2 1 1
0 1 2
1 1 1
'''