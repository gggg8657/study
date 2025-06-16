
import sys
import math
from pprint import pp as print

input = sys.stdin.readline

H,W,N,M = map(int,input().split())

a = math.ceil(H/(N+1))
b = math.ceil(W/(M+1))

print(a*b)
