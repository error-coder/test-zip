def solution(n):
    result = []

    for i in range(1, n + 1):
        if i % 2 == 1:
            result.append(i)

    return result