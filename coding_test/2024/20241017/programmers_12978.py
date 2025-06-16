def solution(N, road, K):
    print(f"{N}, {road}, {K}")



def __main__():
    N = 5
    road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
    K = 3
    solution(N, road, K)
    N, road, K = 6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4
    solution(N, road, K)

__main__()