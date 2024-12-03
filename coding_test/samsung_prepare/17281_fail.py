import sys

input = sys.stdin.readline

a = int(input())


line = []
homerun = []
third = []
two = []
single = []
out = []
result = 0
for _ in range(a):
    line=[]
    num = input().split()
    line.append(num)
    print(line)
    print(line[0].index('4'))
    lineup= line[0]
    if 4 in lineup:
        homerun.append(lineup.index(4))
    elif 3 in lineup:
        third.append(lineup.index(3))
    elif 2 in lineup:
        two.append(lineup.index(2))
    elif 1 in lineup:
        single.append(lineup.index(1))
    elif '0' in lineup:
        out.append(lineup.index('0'))
    print(f"homerun index : {homerun}\n third index : {third}\n two index : {two}\n single index : {single}\n out index : {out}")
    # lineup[4] = line[0]

