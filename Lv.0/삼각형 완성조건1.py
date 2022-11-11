def solution(sides):
    result = 0
    sides.sort()

    if sides[0] + sides[1] > sides[2]:
        result = 1
    else:
        result = 2

    return result

# 직관적인 답안
# def solution(sides):
#     answer = 0
#     sides.sort()
#     a, b, c = sides[0], sides[1], sides[2]
#     if a + b > c:
#         return 1
#     return 2

# # 직관적인 답안(2)
# def solution(sides):
#     sides.sort()
#     if sides[0] + sides[1] > sides[2]:
#         answer = 1
#     else:
#         answer = 2
#     return answer