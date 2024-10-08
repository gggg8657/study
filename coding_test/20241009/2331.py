import sys

input = sys.stdin.readline

def jaegob(n,p):
    n = list(map(int, n))
    v = 0
    for i in range(len(n)):
        result = 1
        src = n[i]
        for _ in range(int(p)):
            result *= src
        v += result
        # print(v)
    return str(v)

n,p = input().split()

visited = {}


#TODO
# 수열 만들기
# 만들면서, visit 처리하기?

arr = [[0 for _ in range(9999)]
i = 1
arr [0] = n
visited[int(n)] = i
result = []
erase = 9999
while True:
    arr.append(jaegob(arr[i-1],p))
    i += 1
    if int(arr[i-1]) in visited:
        break
    else:
        visited[int(arr[i - 1])] = i
erase = arr.index(arr[-1])
del arr[erase:]

'''
        if int(arr[i-1]) in result :
            break
        else:
            result.append(arr[i-1])
            continue
'''
print(len(arr))
# print(visited)
# print(arr)