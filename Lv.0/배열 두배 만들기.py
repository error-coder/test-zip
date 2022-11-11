def solution(numbers):
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i] * 2)

    return result

# # 직관적인 답안
# def solution(numbers):
#     return list(map(lambda x: x * 2, numbers))