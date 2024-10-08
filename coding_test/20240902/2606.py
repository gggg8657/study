import sys
from collections import deque

input = sys.stdin.readline
vertex = int(input())
edge = int(input())
graph= [[False for _ in range(vertex+1)] for _ in range(vertex+1)]
for _ in range(edge):
    start, end = map(int ,input().split())
    graph[start][end] = True
    graph[end][start] = True

visited=[]

queue=deque([1])
visited.append(1)
while queue:
    n = queue.popleft()
    for m in range(vertex+1):
        if graph[n][m] == True and not m in visited:
            visited.append(m)
            queue.append(m)

print(len(visited)-1)


