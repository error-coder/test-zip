def solution(k, m, score):
    answer = 0

    # k 최상품 사과, 1점이 최하품, 사과 점수 score, 한 상자에 들어가는 사과 수 m
    # 사과 한 상자의 가격 : 낮은 점수가 p일 경우 p * m(사과 개수)
    # 사과는 상자 단위로 계산하며, 남는 사과는 버림

    score = sorted(score, reverse=True)

    for i in range(0, len(score), m):
        # m개씩 구성해야 하니까 m개 단위로 잘라가면서 길이가 m이면 현재 m개씩 잘린 사과들 중에 (가장 작은 값 * m)을 answer에 계속 더해 준다.
        tmp = score[i : i + m]

        if len(tmp) == m:
            answer += min(tmp) * m

    return answer


# 다른 사람 풀이

# def solution(k, m, score):
#     answer = 0

#     score.sort()

#     length = len(score)

#     start_point = length % m

#     while start_point < length:
#         answer += score[start_point] * m
#         start_point += m

#     return answer

# def solution(k, m, score):
#     '''
#     result = 0
#     score.sort(reverse = True)
#     while len(score) >= m:
#         result += score[:m][-1] * m
#         score = score[m:]

#     return result
#     '''

#     result = 0
#     score.sort(reverse = True)
#     for i in range(m - 1, len(score), m):
#         result += score[i] * m

#     return result
