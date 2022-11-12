def solution(n):
    num = n ** 0.5

    if int(num) == num:
        return 1
    else:
        return 2

# 직관적인 답안
# def solution(n):
#     import math
#     if int(math.sqrt(n))==math.sqrt(n):
#         return 1
#     else:
#         return 2