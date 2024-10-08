T = int(input())

for _ in range(T):
    R, S = list(map(str, input().split()))

    R = int(R)

    for i in S:
        print(R*i, end='')
    print()