import sys
from collections import deque

# input = sys.stdin.readline
cnt = 0
rest_list = []
for i in range(10):
    a = input()
    rest = int(a) % 42
    if rest not in rest_list:
        rest_list.append(rest)
rest_list.sort(reverse=True)


if rest_list[0] == 0:
    print(1)
else : print(len(rest_list))