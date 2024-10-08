import sys
from collections import deque

queue = deque()
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    n = int(input())
    graph = list(map(int, input().split()))

    visited = [False for _ in range(n)]
    queue.append(graph[0])
    visited[0] = True

    cnt = 0

    for i in range(n):
        if visited[i] == False:
            queue.append(graph[i])

        while queue:
            v = queue.popleft()
            if visited[v - 1]:
                cnt +=1
            else :
                queue.append(graph[v-1])
                visited[v-1] = True

    print(cnt)

