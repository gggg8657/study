class CAR:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.dir = 0
        self.cnt = 0
        self.ans = 1


def Move(car):
    LEFT, car = car_left(car)
    if LEFT: # True is road, False is not road
        car = Move_forward(car)
        car.cnt = 0
        car.ans += 1
    else :
        car.dir = (car.dir - 1)%4
        car.cnt+=1
    if car.cnt >= 4: # 세번 왼쪽 봤는데, 갈 곳 없음
        car = BBAGGU(car) # 빠꾸도 불가능하면 이 함수에서 return?
        car.cnt = 0

dr, dc = [-1,0,1,0],[0,1,0,-1]

def car_left(car):
    if 0<= car.row + dr[(car.dir-1)%4] < n and  0<=car.col + dc[(car.dir-1)%4]<m and world[car.row + dr[(car.dir-1)%4]][car.col + dc[(car.dir-1)%4]] ==0:
        car.dir = (car.dir - 1)%4
        return True, car
    else: return False, car

def Move_forward(car):
    car.row, car.col = car.row + dr[car.dir],car.col + dc[car.dir]
    return car

Bdr, Bdc = [1, 0, -1, 0], [0, -1, 0, 1]

def BBAGGU(car):
    if 0<= car.row + Bdr[car.dir] < n and  0<=car.col + Bdc[car.dir]<m and world[car.row + Bdr[car.dir]][car.col + Bdc[car.dir]] == 2:
        car.row, car.col = car.row + Bdr[car.dir],car.col + Bdc[car.dir]
        return car
    else: 
        print(car.ans)
        exit()

n, m = map(int, input().split())

tsl = CAR()
r, c, d= map(int, input().split())
tsl.row, tsl.col, tsl.dir = r, c, d

world = []
for row in range(n):
    world.append(list(map(int,input().split())))

# print(world)

while True: 
    world[tsl.row][tsl.col] = 2
    Move(tsl)
    