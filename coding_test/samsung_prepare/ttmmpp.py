# 2차원 배열 생성 예제
rows = 3  # 행의 수
cols = 4  # 열의 수

# 2차원 배열 초기화
array_2d = [[0 for _ in range(cols)] for _ in range(rows)]

# 배열에 값 할당
for i in range(rows):
    for j in range(cols):
        array_2d[i][j] = i * j  # 예시로 행과 열의 곱을 할당

# 결과 출력
for row in array_2d:
    print(row)

# BFS 구현
from collections import deque

def bfs(start_row, start_col):
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True

    while queue:
        current_row, current_col = queue.popleft()
        print(f"방문한 노드: ({current_row}, {current_col})")  # 방문한 노드 출력

        # 상하좌우 탐색
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = current_row + dr, current_col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                visited[new_row][new_col] = True
                queue.append((new_row, new_col))

# BFS 시작
bfs(0, 0)  # (0, 0)에서 BFS 시작

