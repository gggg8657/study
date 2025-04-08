# 2023 하반기 오전 1번 문제

'''
input : L, N, Q

cond of L
    0 means blank
    1 means trap
    2 means wall

for N lines get information about knights : r, c, h, w, k
    r : row
    c : column
    h : height
    w : width
    k : HP at begin
처음의 기사들의 위치는 겹쳐져 있지 않음
기사와 벽은 겹쳐서 주어지지 않음

for next Q lines get information about order : i, d
    i : i_th knights
    d : direction
i번째 기사에게 d 방향으로 한칸 이동하도록 명령
d : 0 1 2 3 :: 북 동 남 서

3 <= L <= 40
1 <= N <= 30
1 <= Q <= 100
1 <= k <= 100
'''

# 입력 받고

# 세팅하고

# 기사 이동 (이동하려는 칸에 기사가 있으면 한칸 밀려남)
#   이동 -> 근데 기사 있으면 그거 먼저 밀어냄 -> 근데 그 뒤에 벽이 있으면 안움직여짐 (못 움직임)

# 대결 대미지 (밀려나면서 밟은 함정마다 체력 손실) : 기사가 모두 밀린 이후에 피를 깎음
#   이동 -> 이동한 이후 함정 밟았나 확인 -> 체력 깎기

# 출력 : Q번의 명령 수행 이후 : 생존한 기사들이 총 받은 대미지의 합을 출력하는 프로그램

from collections import deque

class kisa:
    r = 0
    c = 0
    h = 0
    w = 0
    HP = 0



L, N, Q = map(int, input().split())

world = []

for _ in range(L):
    world.append(list(map(int, input().split())))

print("\n\n * * * init world * * *\n")
print(world)

q = deque()
for _ in range(N):
    k = kisa()
    k.r, k.c, k.h, k.w, k.HP = list(map(int, input().split()))
    q.append(k)

print("\n\n * * * init knights * * *\n")
print(q)

order = deque()
for _ in range(Q):
    order.append(list(map(int, input().split())))

print("\n\n * * * init orders * * *\n")
print(order)

while order:
    n, d = order.popleft()
    ck = q[n] # n 번째 기사 출격 대기중
