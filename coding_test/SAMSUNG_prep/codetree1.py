# VIRUS CHECK
### 2015 하반기 1번
'''
input :
첫째 줄에는 식당의 수 n
둘째 줄에는 각 식당에 있는 고객의 수가 공백을 사이에 두고 주어짐
셋째 줄에는 검사팀장이 검사할 수 있는 최대 고객 수와 검사팀원이 검사할 수 있는 최대 고객 수가 공백을 사이에 두고 주어짐

# CONDITION
- 1<= n <= 1,000,000
- 1<= 각 식당에 있는 고객의 수 <= 1,000,000
- 1<= 팀장 혹은 팀원 한 명이 검사 가능한 최대 고객의수 <= 1,000,000

n개의 식당의 고객들을 모두 검사하기 위한 검사자의 최소의 수 출력
'''


N = int(input())

array = list(map(int, input().split()))

C, m = map(int, input().split())

result = 0
for i in range(N):
    res = array[i] - C
    result += 1
    if res>0:
        if res - (m * (res//m)) > 0:
            result+=1
        else : result+=0
        result += res // m
# VIRUS CHECK
### 2015 하반기 1번
'''
input :
첫째 줄에는 식당의 수 n
둘째 줄에는 각 식당에 있는 고객의 수가 공백을 사이에 두고 주어짐
셋째 줄에는 검사팀장이 검사할 수 있는 최대 고객 수와 검사팀원이 검사할 수 있는 최대 고객 수가 공백을 사이에 두고 주어짐

# CONDITION
- 1<= n <= 1,000,000
- 1<= 각 식당에 있는 고객의 수 <= 1,000,000
- 1<= 팀장 혹은 팀원 한 명이 검사 가능한 최대 고객의수 <= 1,000,000

n개의 식당의 고객들을 모두 검사하기 위한 검사자의 최소의 수 출력
'''


N = int(input())

array = list(map(int, input().split()))

C, m = map(int, input().split())

result = 0
for i in range(N):
    res = array[i] - C
    result += 1
    if res>0:
        if res - (m * (res//m)) > 0:
            result+=1
        else : result+=0
        result += res // m

print(result)
# print(array)


# cap = []
# mem = []



print(result)
# print(array)


# cap = []
# mem = []


