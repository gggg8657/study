import sys

input = sys.stdin.readline

a = input().split(' ')
result = len(a)
for i in range(2):
    if a[-1] == "\n":
        result = result-1
        a[-1]="replaced"
    elif a[0]=="":
        result=result-1
        a[0]="replaced"

print(result)
