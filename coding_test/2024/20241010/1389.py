#BFS 문제

import sys
from pprint import pp as print

input = sys.stdin.readline

N, M = map(int, input().split())

friend = [[]for _ in range(N+1)]

for _ in range(N):
    a,b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)

print(friend)
visit = [False for _ in range(N+1)]
def dfs(start, cnt):
    #종료조건
    visit[start]=True
    print(start)
    if :
        return cnt
    for idx in range(len(friend)):
        if visit[idx]==False:
            dfs(idx,cnt+1)
cnt_list=[]
cnt_list.append(dfs(0,0))
print(cnt)