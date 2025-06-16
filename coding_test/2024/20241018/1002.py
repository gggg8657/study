t = int(input())

for i in range(t):
    x1, y1, a, x2, y2, b = map(int, input().split())
    d = ((x1-x2)**2+(y1-y2)**2)**0.5 # 두 점 사이의 거리 구하기

    if d > a+b or d < abs(a-b): # 밖에서 안만나거나 안에서 안만나는 경우
        print(0)
    elif d == a+b or d == abs(a-b) !=0: # 외접, 내접
        print(1)
    elif abs(a-b) < d < a+b: # 서로 다른 두점에서 만나는 경우
        print(2)
    else: # 같은 원인 경우
        print(-1)