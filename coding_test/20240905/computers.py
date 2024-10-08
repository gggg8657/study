from collections import deque


def solution(n, computers):
    queue = deque()

    visited = [[False for _ in range(n)] for _ in range(n)]

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(3):
        print(computers[i], end='\n')
    cnt = 0
    for a in range(n):
        for b in range(n):
            if visited[a][b]: continue
            if not visited[a][b]:
                queue.append((a,b))
            while queue:
                x, y = queue.popleft()
                visited[x][y] = True
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    print("nx is ", nx)
                    print("ny is ", ny)
                    if 0 <=nx<n and 0<=ny<n  and  computers[nx][ny] == 1 and visited[nx][ny] == False:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
            cnt += 1
    print(cnt)



    # while queue:

    answer = 0
    return answer
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(3,computers))