import sys
from math import sqrt
from collections import defaultdict
input = sys.stdin.readline

N = int(input())

point_list = defaultdict(list)

for i in range(N):
    a,b = list(map(int, input().split()))
    point_list[i] = [a,b]

def weight_cal(a,b,c,d):
    # print(a, b, c ,d, sqrt((a-c)**2 + (b-d)**2))
    return sqrt((a-c)**2 + (b-d)**2)
print(point_list)

weight_list = defaultdict(list)
for i in range(N):
    for j in range(N):
        weight_list[i].append((j,weight_cal(point_list[i][0], point_list[i][1], point_list[j][0], point_list[j][1])))
print(weight_list)
is_visited = [False for _ in range(N)]

answer = []

def dfs(n, road, city, weights, start):
    if city == n:  # 도시를 다 돌았을때
        # 다시 돌아갈 수 있는지 확인
        for i, weight in weight_list[road]:
            if i == start:
                answer.append(weights + weight)
        return

    is_visited[road] = True

    for i, weight in weight_list[road]:
        # print(i)
        # print(weight)
        if is_visited[i] == False:
            # 다음 도시 이동
            dfs(n, i, city + 1, weights + weight, start)

    # 백트래킹
    is_visited[road] = False


dfs(N, 0, 1, 0, 0)
print(min(answer))