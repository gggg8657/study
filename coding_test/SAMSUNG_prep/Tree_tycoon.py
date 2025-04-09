# 신비한 나무 리브로수 씹련을 키우기

#N X N 격자에 키움

# 영양제 이동

# 리브로수 성장

from collections import deque

q = deque()

n, m = map(int, input().split())

world = []
for _ in range(n):
    world.append(list(map(int, input().split())))

for _ in range(m):
    q.append(list(map(int,input().split())))

while q:
    d,p = q.popleft()
    d -=1
    for _ in range(4):
        if d == 0:
            
        elif d==1:

        elif d == 2:
        
        elif d== 3:

        elif d == 4:
        
        elif d == 5:
        
        elif d == 6:
        
        elif d == 7:
