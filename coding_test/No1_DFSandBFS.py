# https://www.acmicpc.net/problem/1260
# 문제: DFS와 BFS
# DFS와 BFS를 이용하여 그래프를 탐색하는 문제
# 입력: 정점의 개수 N(1<=N<=1000), 간선의 개수 M(1<=M<=10000), 탐색을 시작할 정점의 번호 V
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어짐
# 출력: DFS로 탐색한 결과, BFS로 탐색한 결과
# 입력 예:
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 출력 예:
# 1 2 4 3
# 1 2 3 4
# -------------------------TIP------------------------------------
# 입력을 받아 그래프를 만들고, DFS와 BFS를 구현하여 출력하는 문제
# DFS는 재귀함수를 이용하여 구현하고, BFS는 큐를 이용하여 구현
# ----------------------------------------------------------------

import sys
from collections import deque


# DFS 랑 BFS 이렇게 쓰는구나를 보고 

# 노드 넷 엣지 다섯개 시작노드 1

# 1번 

# 그래프는 딕셔너리로 하는 방법 2차원 배열로 하는 방법

# 2차원으로 하면 1번부터 4번까지 있고

# dict 1 : 2, 3, 4

# array 4 by 4 -> 1,3 -> 1 에서 3으로 가는 줄

n, m, v = map(int, sys.stdin.readline().split())

arr = [[False for _ in range(n+1)] for _ in range(n+1)] # list comprehension

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = arr[b][a] = True # 1 -> 2 // 2-> 1  그래프다.


