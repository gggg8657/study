
def Jo_mo_check(jo_mo_checklist, item):
    for i in range(len(item)):
        jo_mo_checklist[item[i]-1] = 1 # 1 means jo 0 means mo
    return jo_mo_checklist
N = int(input())

work = []
worklist = []
for _ in range(N):
    work.append(list(map(int, input().split())))
    worklist.append(_+1)
from itertools import combinations
work_comb = combinations(worklist, N//2)

result = 9999
for item in work_comb:
    jo_result = 0
    mo_result = 0
    sub_result =0
    jo_mo_checklist= [0 for _ in range(N)]
    jo_mo_checklist = Jo_mo_check(jo_mo_checklist,item)

    for row in range(N):
        for col in range(N):
            if jo_mo_checklist[row] == 1 and jo_mo_checklist[col] == 1: #낮에 하는 일 세트
                jo_result += work[row][col]
            elif jo_mo_checklist[row] == 0 and jo_mo_checklist[col]==0:
                mo_result += work[row][col]

    sub_result = abs(jo_result-mo_result)
    if result>sub_result: 
        result = sub_result
        sub_result =0
print(result)