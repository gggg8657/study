import sys

input = sys.stdin.readline

n = int(input())

store_list = list(map(int, input().split()))

C, M = map(int, input().split())

# print(n, store_list, C, M)
ans = 0
for _ in range(n):
    store_list[_] -= C
    # print(store_list[_])
    if store_list[_]>0:
        if store_list[_]%M!=0:
            # print("a")
            store_list[_] = store_list[_]//M + 1
            # print(store_list[_])
        else:
            # print("b")
            store_list[_] = store_list[_] // M
            # print(store_list[_])
        store_list[_]+=1
    else :
        # print("c")
        store_list[_] = 1
        # print(store_list[_])
    ans += store_list[_]
print(ans)