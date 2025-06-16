import sys
from collections import deque
from pprint import pp as print

input = sys.stdin.readline
a, b = map(int, input().split())
graph_candidate = [[] for _ in range(a+1)]
#make graph
# print(graph_candidate)
for _ in range(b):
    src, tar = map(int, input().split())
    graph_candidate[src].append(tar)
    graph_candidate[tar].append(src)

visited = [False for _ in range(a+1)]

def bfs(graph, visited,x):
    queue = deque([x])
    visited[x]=True
    while queue:
        node = queue.popleft()
        for near in graph[node]:
            if visited[near] == False:
                visited[near]=True
                queue.append(near)

cnt = 0
for i in range(1, a+1):
    if visited[i]==False:
        bfs(graph_candidate,visited,i)
        cnt +=1
print(cnt)



