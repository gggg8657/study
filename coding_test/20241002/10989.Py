import sys

N = int(input())

count = [0] * 10001
for i in range(N):
    input_num = int(sys.stdin.readline())
    count[input_num] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)

# size = int(input())
# # nums = list(map(int,input().split()))
# nums=[]
# for i in range(size):
#     nums.append(int(input()))
#     nums = sorted(nums)
# for i in range(size):
#     print(nums[i])