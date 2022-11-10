def solution(money):
    result = []
    result.append(money // 5500)
    result.append(money % 5500)

    return result