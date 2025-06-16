import sys
# from pprint import pp as print

input = sys.stdin.readline

N, M = map(int, input().split())

visit = [False for _ in range(N+1)]

def dfs(graph,sex,start):
    #종료조건
    if sex == M:
        print(*graph)
        return

    for idx in range(1,N+1):
        if visit[idx]==False:
            graph.append(idx)
            visit[idx] =True
            dfs(graph,sex+1,idx)
            graph.pop()
            visit[idx]= False

dfs([],0,visit)