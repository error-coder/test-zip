def solution(name, yearning, photo):
    answer = []

    # 그리워하는 사람의 이름 name
    # 각 사람별 그리움 점수 yearning
    # 각 사진에 찍힌 인물의 이름을 담은 photo

    for i in photo:
        result = 0

        for j in i:
            if j in name:
                result += yearning[name.index(j)]
        answer.append(result)

    return answer


# 다른 사람 풀이

# def solution(name, yearning, photo):
#     answer = []

#     for i in photo:
#         score=0
#         for j in range(len(name)):
#             if name[j] in i:
#                 score+=yearning[j]
#         answer.append(score)
#     return answer
