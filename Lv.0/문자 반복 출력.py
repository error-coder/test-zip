def solution(my_string, n):
    result = []
    for i in range(len(my_string)):
        for _ in range(n):
            result.append(my_string[i])

    return ''.join(result)

# 간단한 답안
# def solution(my_string, n):
#     return ''.join(i*n for i in my_string)

# 직관적인 답안
# def solution(my_string, n):
#     answer = ''
#     for s in my_string:
#         answer += s * n
#     return answer