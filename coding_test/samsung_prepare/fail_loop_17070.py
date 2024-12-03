N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# 3차원 DP 배열 초기화
dp = [[[0] * N for _ in range(N)] for _ in range(3)]

# 초기 상태 설정 (가로 방향에서 시작)
dp[0][0][1] = 1

for r in range(N):
    for c in range(N):
        # 현재 위치가 벽인 경우, 넘어감
        if arr[r][c] == 1:
            continue

        # 가로 상태에서 가능한 이동
        if c - 1 >= 0 and arr[r][c - 1] == 0:
            dp[0][r][c] += dp[0][r][c - 1] + dp[2][r][c - 1]

        # 세로 상태에서 가능한 이동
        if r - 1 >= 0 and arr[r - 1][c] == 0:
            dp[1][r][c] += dp[1][r - 1][c] + dp[2][r - 1][c]

        # 대각선 상태에서 가능한 이동
        if r - 1 >= 0 and c - 1 >= 0 and arr[r - 1][c] == 0 and arr[r][c - 1] == 0 and arr[r - 1][c - 1] == 0:
            dp[2][r][c] += dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

# 마지막 위치 (N-1, N-1)에서 가능한 모든 상태의 합 계산
print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])