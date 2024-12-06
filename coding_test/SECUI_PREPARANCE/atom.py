# #TODO [1] : mov per sec
# #TODO [2] : if in block more than two 합성 in each block
# # 같은 칸에 있는 원자들은, 각각의 질량과 속력을 모두 합한 하나의 원자로 합쳐짐.
# # if 합쳐짐 -> 네개로 나누고 (if 속력 질량 방향 나누는 기준)
# # 나누어진 원자들은 모두 해당 칸에 위치하고
# #TODO [3] : 속력 질량 방향 나누는 기준 1. 질량 = 합쳐진거 / 5,
# # 속력 = 합쳐진거 / 합쳐진 원자의 개수,
# # 방향 = 상하좌우||대각로 합쳐짐 -> 상하좌우 || 잡탕 -> 대각
# # 소수점 아래 수 날림 == (// or int 처리)
# # 질량이 0 이면 소멸
# # 이동 과정 중에 원자가 만나는 경우는 합성으로 고려하지 않음. -> 1턴 이후 합성해야됨
#
import sys

def synthesis(arr, info):
    new_list=[]
    flag = len(arr)
    i=0
    while arr:
        if i == flag: break
        syntar = []
        new_atom = [0]*6 # in new atom there is flag in address 4 if flag is 0 상하좌우, else 대각선 in new atom
        try: x, y = arr[i][0], arr[i][1]  # src x,y
        except:
            break
        tmp = arr[i][4]%2
        syntar.append(arr[i])
        for tar in range(i+1, len(arr)):
            if x == arr[tar][0] and y == arr[tar][1]:
                # print("synthesis target occur")
                syntar.append(arr[tar])
                new_atom[0] = arr[i][0] #syn pos
                new_atom[1] = arr[i][1]
        for srcs in syntar:
            new_atom[2] += srcs[2]  # syn mass
            new_atom[3] += srcs[3]  # syn spedd
            if srcs[4] % 2 != tmp: new_atom[4] = 1  # syn direction flag if different from before
            new_atom[5] += 1
                # syntar.popleft()
        if len(syntar)==1:
            i += 1
            pass
        else:
            new_list.append(new_atom)
            for a in syntar:
                #arr.pop(arr.index(a))
                info.pop(info.index(a))

    return new_list
                    #srcs[4]

                    #나눠지는 원자 방향 정해줘야겠네
import copy
def divide(newt, arr):
    while newt:
        new = newt[0]
        tmp =[0]*5
        size = new[2] // 5
        speed = new[3] // new[5]
        if size<=0:
            newt.pop(newt.index(new))
        else :
            for _ in range(4):
                tmp[0] = new[0]
                tmp[1] = new[1]
                tmp[2] = size
                tmp[3] = speed
                if new[4] ==1 : tmp[4] = _*2+1
                else : tmp[4] = _*2
                x = copy.deepcopy(tmp)
                arr.append(x)
            newt.pop(newt.index(new))
    return arr

def move(arr, N):
    # for atom in arr:
    #     offset = atom[3] % N
    #     if atom[4] == 0:
    #         atom[0] -= offset
    #     elif atom[4] == 1:
    #         atom[0] -= offset
    #         atom[1] += offset
    #     elif atom[4] == 2:
    #         atom[1] += offset
    #     elif atom[4] == 3:
    #         atom[0] += offset
    #         atom[1] += offset
    #     elif atom[4] == 4:
    #         atom[0] += offset
    #     elif atom[4] == 5:
    #         atom[0] += offset
    #         atom[1] -= offset
    #     elif atom[4] == 6:
    #         atom[1] -= offset
    #     elif atom[4] == 7:
    #         atom[0] -= offset
    #         atom[1] -= offset
    #     # 좌표를 그리드 내로 조정
    #     atom[0] %= N
    #     atom[1] %= N
    direction_vectors = [
        (-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1), (-1, -1)
    ]
    for atom in arr:
        dx, dy = direction_vectors[atom[4]]
        atom[0] = (atom[0] + dx * atom[3]) % N
        atom[1] = (atom[1] + dy * atom[3]) % N
    return arr

input = sys.stdin.readline

N, M, K = map(int, input().split())
# n : arr_size, m : atom_cnt, k : ex_time

arr = [[0]*N for _ in range(N)]

info = []
for _ in range(M):
    info.append(list(map(int, input().split())))
    info[_][0] -= 1
    info[_][1] -= 1
    # arr[info[_][0]][info[_][1]]

    # x , y : pos, m : 질량, s : 속력, d : 방향  0부터 7까지 순서대로 ↑, ↗, →, ↘, ↓, ↙, ←, ↖
#좌표로만 이동

# print(info)

for _ in range(K):
    if M == 1 or len(info)==0: break
    info = move(info, N)
    # print(info)
    arr = info
    #arr = copy.deepcopy(info)
    # for i in range(len(info)):
    #     for j in range(i+1, len(info)):
    #         if info[i][0]==
    new_atom = synthesis(arr, info)
    # print(info)
    info = divide(new_atom, info)
    # print(info)


ans = 0
for _ in info:
    ans += _[2]
print(ans)

'''
9 5 10
3 7 7 4 7
7 6 5 5 5
9 2 6 5 5
4 6 4 1 6
6 9 6 3 7
26

4 4 1
1 2 2 2 4
2 4 5 3 6
4 2 1 1 0
4 3 3 2 5
4

5 2 8
5 3 3 3 5
3 3 10 8 6
0
'''

from collections import defaultdict, deque


def move(atoms, N):
    # 방향 벡터 (0부터 7까지 순서대로 ↑, ↗, →, ↘, ↓, ↙, ←, ↖)
    direction_vectors = [
        (-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1), (-1, -1)
    ]

    for atom in atoms:
        dx, dy = direction_vectors[atom[4]]
        offset = atom[3] % N  # 속도만큼 이동
        atom[0] = (atom[0] + dx * offset) % N
        atom[1] = (atom[1] + dy * offset) % N


def synthesis(atoms):
    new_atoms = []
    grid = defaultdict(list)

    # 각 위치별 원자 그룹화
    for atom in atoms:
        grid[(atom[0], atom[1])].append(atom)

    # 그룹화된 원자 처리
    for (x, y), atom_list in grid.items():
        if len(atom_list) == 1:
            new_atoms.append(atom_list[0])  # 합성 불필요
        else:
            total_mass = sum(a[2] for a in atom_list)
            total_speed = sum(a[3] for a in atom_list)
            direction_flag = all(a[4] % 2 == atom_list[0][4] % 2 for a in atom_list)
            count = len(atom_list)

            new_mass = total_mass // 5
            new_speed = total_speed // count

            if new_mass > 0:  # 질량이 0이면 소멸
                for i in range(4):
                    new_direction = i * 2 if direction_flag else i * 2 + 1
                    new_atoms.append([x, y, new_mass, new_speed, new_direction])

    return new_atoms


# 입력 처리
N, M, K = map(int, input().split())
atoms = deque()
for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    atoms.append([x - 1, y - 1, m, s, d])

# 시뮬레이션 실행
for _ in range(K):
    move(atoms, N)
    atoms = deque(synthesis(list(atoms)))

# 결과 계산
print(sum(atom[2] for atom in atoms))
