def solution(k, score):
    answer = []
    rank = []
    # 명예의 전당 목록 점수 개수 k
    # 1일부터 마지막 날까지 출연한 가수들의 점수 score
    # 매일 발표된 명예의 전당 최하위 점수 return

    for i in score:
        if len(rank) < k:
            rank.append(i)
        else:
            if min(rank) < i:
                rank.remove(min(rank))
                rank.append(i)

        answer.append(min(rank))
    return answer


# 다른 사람 풀이

# def solution(k, score):

#     q = []

#     answer = []
#     for s in score:

#         q.append(s)
#         if (len(q) > k):
#             q.remove(min(q))
#         answer.append(min(q))

#     return answer
