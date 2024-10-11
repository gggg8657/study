import sys
# from pprint import pp as print
from collections import deque

input = sys.stdin.readline

# TODO

'''
3 4 5 4 5 6 
'''
#
#
# def arr_sum(arr, x1, y1, x2, y2):
#     result = 0
#
#     # x1 == x2일 때: 같은 행에서 y1부터 y2까지 합산
#     if x1 == x2 and y1 == y2:
#         return arr[x1 - 1][y1 - 1]
#     else:
#         if x1 == x2:  # 한 행에서 y1부터 y2까지의 합을 구하는 경우
#             for j in range(y1, y2 + 1):  # y1부터 y2까지 포함하므로 y2 + 1
#                 result += arr[x1 - 1][j - 1]
#         elif y1 == y2:  # 한 열에서 x1부터 x2까지의 합을 구하는 경우
#             for i in range(x1, x2 + 1):  # x1부터 x2까지 포함하므로 x2 + 1
#                 result += arr[i - 1][y1 - 1]
#         else:  # 여러 행과 열을 포함하는 경우 (사각형 영역)
#             for i in range(x1, x2 + 1):
#                 for j in range(y1, y2 + 1):
#                     result += arr[i - 1][j - 1]
#
#     return result
def prefix_sum(arr,N):
    prefix = [[0]*(N+1)for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,N+1):
            prefix[i][j] = arr[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

    return prefix

def arr_sum (prefix, x1,y1,x2,y2):
    return prefix[x2][y2] -prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
# 입력 처리
N, M = map(int, input().split())

arr = [(list(map(int, input().split()))) for _ in range(N)]

x1_list, y1_list, x2_list, y2_list = [], [], [], []
prefix = prefix_sum(arr,N)
# 쿼리 입력
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = arr_sum(prefix,x1,y1,x2,y2)
    print(result)
