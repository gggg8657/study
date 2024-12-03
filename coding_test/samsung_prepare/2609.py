from collections import deque
import sys

input = sys.stdin.readline

a, b = map(int, input().split())
Max = 1
for div in range(b,1,-1):
    if a%div ==0 and b%div ==0 and Max<div:
        Max = div
    else: continue
print(Max)
print(a*b//Max)
# print(f"{Max}\n{a*b//Max}")