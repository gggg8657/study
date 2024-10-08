A, P = map(int, input().split())
arr = []
idx = 1
is_used = {}
is_used[A] = 0
arr.append(A)
while True:
    temp = 0
    num = arr[-1]
    while num > 0:
        temp += (num % 10) ** P
        num //= 10
    if temp not in is_used:
        is_used[temp] = idx
        idx += 1
        arr.append(temp)
    else:
        arr = arr[:is_used[temp]]
        break

print(len(arr))