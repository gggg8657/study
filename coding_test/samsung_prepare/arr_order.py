import sys

def move(arr,flag):
    narr=[]
    for _ in range(20):
        narr.append(arr[_])
    for _ in range(len(arr)):
        if _+flag == 20 or _+flag<0:
            break
        else :
            narr[_ + flag] = arr[_]

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[' ' for _ in range(20)]for _ in range(n)]
print(len(arr))
order = [list(map(int, input().split())) for _ in range(m)]
for _ in range(m):
    if order[_][0] ==1:
        arr[order[_][1]][order[_][2]] = 1
    elif order[_][0] ==2:
        arr[order[_][1]][order[_][2]] = 0
    elif order[_][0]==3:
        move(arr[order[_][1]],1)
    elif order[_][0]==4:
        move(arr[order[_][1]],-1)
result = []
result.append(arr[0])
for _ in range(n):
    if arr[_] in result:
        continue
    else: result.append(arr[_])

print(len(result)-1)