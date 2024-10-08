# '''
# def solution(D, T):
#     # 트럭이 담당할 쓰레기 종류를 정의합니다.
#     trash_types = ['P', 'G', 'M']
    
#     # 트럭이 각각 수거할 가장 먼 거리를 저장할 변수들
#     max_distances = {'P': -1, 'G': -1, 'M': -1}
    
#     # 각 쓰레기 종류별로 가장 먼 집을 찾습니다.
#     for i, trash in enumerate(T):
#         for t in trash_types:
#             if t in trash:
#                 max_distances[t] = i
    
#     # 각 트럭이 쓰레기를 수거하는 데 걸리는 시간을 계산합니다.
#     def calculate_time(trash_type):
#         if max_distances[trash_type] == -1:
#             return 0  # 해당 종류의 쓰레기가 없으면 시간은 0입니다.
        
#         # 해당 쓰레기를 수거하기 위해 가야 할 집의 위치
#         last_house = max_distances[trash_type]
        
#         # 출발점에서 해당 집까지 가는 총 이동 시간 계산
#         total_travel_time = sum(D[:last_house+1])
        
#         # 쓰레기 수거 시간 (해당 집에서 수거하는 봉투의 수)
#         total_pickup_time = sum([house.count(trash_type) for house in T[:last_house+1]])
        
#         # 왕복 시간을 고려합니다 (가는 시간 + 돌아오는 시간)
#         return total_travel_time * 2 + total_pickup_time
    
#     # 플라스틱, 유리, 금속을 수거하는 데 걸리는 시간 계산
#     plastic_time = calculate_time('P')
#     glass_time = calculate_time('G')
#     metal_time = calculate_time('M')
    
#     # 가장 오래 걸리는 시간을 반환
#     return max(plastic_time, glass_time, metal_time)

# # 예제 실행
# D1 = [2, 5]
# T1 = ['PGP', 'M']
# print(solution(D1, T1))  # 출력: 15

# D2 = [3, 2, 4]
# T2 = ['MPM', '', 'G']
# print(solution(D2, T2))  # 출력: 19

# D3 = [2, 1, 1, 1, 2]
# T3 = ['', 'PP', 'PP', 'GM']
# print(solution(D3, T3))  # 출력: 12

# '''

# def solution(D, T):
#     # 먼저, 트럭이 수거할 쓰레기 종류를 정의합니다.
#     trash_types = ['P', 'G', 'M']
    
#     # 각 트럭이 수거할 쓰레기 종류 중 가장 먼 집의 인덱스를 저장합니다.
#     max_indices = {'P': -1, 'G': -1, 'M': -1}
    
#     # 각 집마다 어떤 쓰레기가 있는지 확인해서, 가장 먼 집을 찾습니다.
#     for i in range(len(T)):
#         for trash in T[i]:
#             if trash in trash_types:
#                 max_indices[trash] = i
    
#     # 특정 종류의 쓰레기를 수거하는데 걸리는 시간을 계산하는 함수를 만듭니다.
#     def get_total_time(trash_type):
#         last_house = max_indices[trash_type]
#         if last_house == -1:
#             return 0  # 해당 종류의 쓰레기가 없으면 0분 걸립니다.
        
#         # 출발점에서 마지막 집까지 가는 데 걸리는 시간을 계산합니다.
#         travel_time = 0
#         for i in range(last_house):
#             travel_time += D[i]
        
#         # 마지막 집까지 도착 후, 쓰레기를 수거하는 시간도 계산합니다.
#         pickup_time = 0
#         for i in range(last_house + 1):
#             pickup_time += T[i].count(trash_type)
        
#         # 왕복 시간 = 가는 시간 + 돌아오는 시간 + 쓰레기 수거 시간
#         total_time = (travel_time * 2) + pickup_time + D[last_house] * 2
#         return total_time
    
#     # 플라스틱, 유리, 금속 수거 시간을 각각 계산합니다.
#     plastic_time = get_total_time('P')
#     glass_time = get_total_time('G')
#     metal_time = get_total_time('M')
    
#     # 모든 트럭이 작업을 끝내는 데 걸리는 최소 시간은 가장 오래 걸리는 트럭의 시간입니다.
#     return max(plastic_time, glass_time, metal_time)

# # 예제 실행
# D1 = [2, 5]
# T1 = ['PGP', 'M']
# print(solution(D1, T1))  # 출력: 15

# D2 = [3, 2, 4]
# T2 = ['MPM', '', 'G']
# print(solution(D2, T2))  # 출력: 19

# D3 = [2, 1, 1, 1, 2]
# T3 = ['', 'PP', 'PP', 'GM']
# print(solution(D3, T3))  # 출력: 12

def solution(D, T):
    N = len(T)
    cum_D = [0] * N
    if N == 0:
        print("No houses to process.")
        return 0
    cum_D[0] = D[0]
    for k in range(1, N):
        cum_D[k] = cum_D[k-1] + D[k]
    print(f"Cumulative distances: {cum_D}")

    max_total_time = 0
    for c_type in ['P', 'G', 'M']:
        total_bags = 0
        furthest_house = -1
        for k in range(N):
            count = T[k].count(c_type)
            if count > 0:
                total_bags += count
                furthest_house = k
                print(f"House {k}: Found {count} '{c_type}' bag(s).")
        if total_bags == 0:
            total_time = 0
            print(f"No '{c_type}' bags to collect.")
        else:
            total_time = 2 * cum_D[furthest_house] + total_bags
            print(f"Total '{c_type}' bags: {total_bags}, Furthest house: {furthest_house}, Total time: {total_time}")
        max_total_time = max(max_total_time, total_time)
    print(f"Maximum total time needed: {max_total_time}\n")
    return max_total_time

def test_solution():
    test_cases = [
        # Example 1
        {
            'D': [2, 5],
            'T': ["PGP", "M"],
            'expected': 15
        },
        # Example 2
        {
            'D': [3, 2, 4],
            'T': ["MPM", "", "G"],
            'expected': 19
        },
        # Example 3
        {
            'D': [2, 1, 1, 1, 2],
            'T': ["", "PP", "PP", "GM", ""],
            'expected': 12
        },
        # Edge Case: No houses
        {
            'D': [],
            'T': [],
            'expected': 0
        },
        # Edge Case: No garbage
        {
            'D': [1, 2, 3],
            'T': ["", "", ""],
            'expected': 0
        },
        # Edge Case: All garbage types at the last house
        {
            'D': [1, 1, 1],
            'T': ["", "", "PGM"],
            'expected': 7
        },
    ]

    for idx, case in enumerate(test_cases):
        D = case['D']
        T = case['T']
        expected = case['expected']
        print(f"Test Case {idx+1}: D = {D}, T = {T}")
        result = solution(D, T)
        print(f"Computed Result: {result}")
        if expected is not None:
            assert result == expected, f"Test Case {idx+1} Failed: Expected {expected}, got {result}"
            print(f"Test Case {idx+1} Passed!\n")
        else:
            print(f"Test Case {idx+1}: Result computed without expected value.\n")

# Run the test cases
test_solution()
