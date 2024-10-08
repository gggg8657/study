N = int(input())

for i in range(N):
    list_ = list(map(int, input().split()))
    avg = (sum(list_)-list_[0])/list_[0]
    cnt = 0
    for j in list_[1:]:
        if j > avg:
            cnt +=1
    print("%.3f%%" % ((cnt / list_[0])*100))