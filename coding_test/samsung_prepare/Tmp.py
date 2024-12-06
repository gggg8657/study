from collections import deque

def solve():
    # 예제용 상수
    N = 8
    M = 3
    F = 2

    # 예시용 맵 (문제의 예시를 간단화)
    # 실제로는 입력값을 받아서 parsing 해야 함
    floor_map = [
        [4,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,0,0],
        [0,1,3,3,3,1,0,1],
        [0,1,3,3,3,1,0,1],
        [0,1,3,3,3,0,0,0],
        [0,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,1]
    ]

    # 윗면 지도 (M×M)
    top_map = [
        [1,1,1],
        [0,0,0],
        [1,0,1]
    ]

    # 시간 이상 현상 정보 (간단화)
    # 실제 문제에서는 각 F개의 시간 이상 현상에 대해 (r, c, d, v) 받아서 처리
    # 여기서는 그냥 하나의 시간 이상 현상만 가정하고 매 턴마다 동쪽으로 확산한다고 치자.
    anomalies = [
        (0,7,0,14),  # r=0,c=7,d=동,v=14 형태로 가정
        (6,3,3,2)    # r=6,c=3,d=북,v=2 형태로 가정
    ]

    # 레벨 정의: 0 -> 바닥(N×N), 1 -> 윗면(M×M)
    # 바닥 좌표: (0, r, c)
    # 윗면 좌표: (1, r, c)

    # 시작점 (윗면에서의 타임머신 위치=2)
    # 실제 문제: 윗면 지도에 2가 표시되어 있음. 여기서는 가정.
    start = (1, 1, 1)  # 예를 들어 윗면 가운데를 시작점이라 가정

    # 탈출구(4) 위치: floor_map에서 4 찾아서 기록
    exit_pos = None
    for i in range(N):
        for j in range(N):
            if floor_map[i][j] == 4:
                exit_pos = (0, i, j)
                break
        if exit_pos:
            break

    # 바닥과 윗면을 연결하는 "통로"를 찾아야 함.
    # 실제 문제에서는 시간의 벽 측면 단면도를 해석하여 단 한칸의 통로를 찾아내야 한다.
    # 여기서는 임의로 윗면 (1,2,1)이 바닥 (0,4,2)로 이어진다고 가정.
    passage_top = (1, 2, 1)
    passage_floor = (0, 4, 2)

    # 시간 이상 현상 맵(바닥 전용)
    anomaly_map = [[False]*N for _ in range(N)]
    # 장애물 표시: 바닥과 윗면에서 1이나 3 등은 장애물로 처리
    def is_obstacle(level, r, c):
        if level == 0:
            # 바닥
            return floor_map[r][c] in [1,3]
        else:
            # 윗면
            return top_map[r][c] == 1

    # 맵 범위 체크
    def in_range(level, r, c):
        if level == 0:
            return 0 <= r < N and 0 <= c < N
        else:
            return 0 <= r < M and 0 <= c < M

    # 시간 이상 현상 확산 (간단 예시)
    # 매 턴마다 anomalies를 확인, 확산 조건에 맞는 턴이면 d방향으로 확산 시도
    # d: 동(0),서(1),남(2),북(3)
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]

    def spread_anomalies(turn):
        for (ar, ac, d, v) in anomalies:
            if turn % v == 0:
                nr, nc = ar+dr[d], ac+dc[d]
                if 0 <= nr < N and 0 <= nc < N:
                    # 빈 공간이면 확산
                    if floor_map[nr][nc] == 0 and not anomaly_map[nr][nc]:
                        anomaly_map[nr][nc] = True

    # BFS를 통한 최단 경로 탐색 (turn마다 이상현상 확산 후 이동)
    from heapq import heappush, heappop

    # visited: (level, r, c, turn)
    # 하지만 turn에 따라 anomaly_map 변하므로 turn도 상태에 넣는다면 너무 커짐
    # 대신 visited는 (level, r, c)만 관리하고, turn마다 상태를 큐에서 관리
    visited = [[[False]*(max(N,M)) for _ in range(max(N,M))] for _ in range(2)]
    # 우선순위 큐에 (시간, level, r, c)
    pq = []
    heappush(pq, (0, start[0], start[1], start[2]))
    visited[start[0]][start[1]][start[2]] = True

    while pq:
        turn, lev, r, c = heappop(pq)

        # 만약 탈출구 도달
        if (lev, r, c) == exit_pos:
            print(turn)
            return

        # 다음 턴 시간 이상 현상 확산
        spread_anomalies(turn)

        # 인접 이동
        directions = [(1,0),( -1,0),(0,1),(0,-1)]
        for dr_, dc_ in directions:
            nr, nc = r+dr_, c+dc_
            if in_range(lev, nr, nc) and not is_obstacle(lev, nr, nc):
                # 윗면이면 anomaly 고려X
                # 바닥이면 anomaly_map[nr][nc] False인지 확인
                if lev == 0:
                    if anomaly_map[nr][nc]:
                        continue
                if not visited[lev][nr][nc]:
                    visited[lev][nr][nc] = True
                    heappush(pq, (turn+1, lev, nr, nc))

        # 층간 이동 (통로가 있는 경우)
        if (lev, r, c) == passage_top:
            fl_lev, fl_r, fl_c = passage_floor
            if not visited[fl_lev][fl_r][fl_c]:
                if not anomaly_map[fl_r][fl_c]:
                    visited[fl_lev][fl_r][fl_c] = True
                    heappush(pq, (turn+1, fl_lev, fl_r, fl_c))
        if (lev, r, c) == passage_floor:
            tp_lev, tp_r, tp_c = passage_top
            if not visited[tp_lev][tp_r][tp_c]:
                # 윗면 anomaly 고려X
                visited[tp_lev][tp_r][tp_c] = True
                heappush(pq, (turn+1, tp_lev, tp_r, tp_c))

    # 탈출 불가능
    print(-1)

if __name__ == "__main__":
    solve()