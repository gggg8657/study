def rotate(grid, start_row, start_col):
    # 3x3 부분을 90도 시계방향으로 회전
    rotated_grid = [row[:] for row in grid]
    for row in range(3):
        for col in range(3):
            rotated_grid[start_row + row][start_col + col] = grid[start_row + 3 - col - 1][start_col + row]
    return rotated_grid

def bfs(grid, visited, start_row, start_col, clear_flag):
    # BFS를 통해 연결된 칸의 개수를 계산
    queue = [(start_row, start_col)]
    connected_cells = {(start_row, start_col)}
    count = 1
    visited[start_row][start_col] = True

    while queue:
        current_row, current_col = queue.pop(0)
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row, next_col = current_row + d_row, current_col + d_col
            if (0 <= next_row < 5 and 0 <= next_col < 5 and
                not visited[next_row][next_col] and
                grid[current_row][current_col] == grid[next_row][next_col]):
                queue.append((next_row, next_col))
                visited[next_row][next_col] = True
                connected_cells.add((next_row, next_col))
                count += 1

    if count >= 3:  # 3개 이상 연결된 경우
        if clear_flag:  # 값 초기화
            for row, col in connected_cells:
                grid[row][col] = 0
        return count
    return 0

def count_clear(grid, clear_flag):
    # 전체 그리드에서 연결된 칸을 탐색
    visited = [[False] * 5 for _ in range(5)]
    total_count = 0
    for row in range(5):
        for col in range(5):
            if not visited[row][col]:
                total_count += bfs(grid, visited, row, col, clear_flag)
    return total_count

def fill_empty(grid, values):
    # 0으로 비어 있는 칸을 values로 채움
    for col in range(5):
        for row in range(4, -1, -1):
            if grid[row][col] == 0 and values:
                grid[row][col] = values.pop(0)

def main():
    K, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(5)]
    values = list(map(int, input().split()))
    results = []

    for _ in range(K):
        # 최적 회전 찾기
        max_count = 0
        best_grid = None
        for rotation in range(1, 4):  # 90도, 180도, 270도 회전
            for start_col in range(3):
                for start_row in range(3):
                    temp_grid = [row[:] for row in grid]
                    for _ in range(rotation):
                        temp_grid = rotate(temp_grid, start_row, start_col)
                    count = count_clear(temp_grid, clear_flag=0)
                    if count > max_count:
                        max_count, best_grid = count, temp_grid

        if max_count == 0:  # 더 이상 제거할 수 있는 유물이 없음
            break

        # 최적 상태로 갱신
        grid = best_grid
        removed_count = 0

        while True:
            cleared = count_clear(grid, clear_flag=1)
            if cleared == 0:
                break
            removed_count += cleared
            fill_empty(grid, values)

        results.append(removed_count)

    print(*results)

main()