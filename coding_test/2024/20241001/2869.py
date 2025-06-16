import math
A, B, V = map(int, input().split())

# S = 0
# cnt = 0
# while V-S > 0:
#     # print("day ", cnt, "current snail ", S, "way to go ", V - S)
#     cnt +=1
#     S += A
#     if V-S <= 0:
#         break
#     else : S-=B
#
# print(cnt)

print(math.ceil((V - A)/(A-B))+1)