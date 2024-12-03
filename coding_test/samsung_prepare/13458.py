import sys

input = sys.stdin.readline

n = int(input()) #시험장 몇개인지

A = []

A = list(map(int,input().split()))#각 시험장에 몇명 있는지

b, c = map(int, input().split()) #한 시험장에서 감시할 수 있는 B명, 부감독이 하는 C명

# 총감은 시험장마다 무조건 1 명, 부감은 X명 있어도됨

cnt = 0
for _ in range(len(A)):
    A[_] -= b
    cnt+=1
    if A[_] >0:
        if A[_]%c != 0:
            cnt+=1
        cnt+=A[_]//c

print(cnt)

