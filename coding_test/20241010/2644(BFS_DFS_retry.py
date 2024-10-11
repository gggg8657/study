import sys
from collections import deque
from pprint import pp as print

N = int(input())
#
src1,src2 = map(int,input().split())
#
M = int(input())

fam = [[] for i in range(N+1)]

for _ in range(M):
    x,y = map(int, input().split())
    fam[x].append(y)
    fam[y].append(x)

visit = [False for _ in range(N+1)]
result = []

def dfs(x,count):
    global flag
    visit[x] = True
    if x==src2:
        flag = True
        print(count)
    for val in fam[x]:
        if visit[val]==False:
            dfs(val, count+1)

flag = False
dfs(src1,0)
if flag==False:
    print(-1)
# fam = {}
# c=[]
# tmp =0
# for _ in range(M):
#     a, b = map(int, input().split())
#     if a not in fam : fam[a]=[]
#     fam[a].append(b)
# print(fam)
# result = -1
# def dfs(cur):
#     print("DFS")
#     print(cur)
#     route = fam[cur]
#     print(route)
#     for r in route:
#         dfs[r]
#
# plist = list(fam.keys())
# print(plist)
# dfs(plist[0])
#
#
# # input().split()
# '''
# def dfs(node,):
#     route = graph[node]
#     for r in route:
#         dfs(r)
# '''

