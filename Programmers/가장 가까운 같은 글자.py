def solution(s):
    answer = []

    # 같은 글자가 없으면 -1
    # 칸 수 1, 두 개 이상 있으면 가까운 것 기준으로 칸 수

    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer


# 다른 사람 풀이

# def solution(s):
#    answer = []
#    alphas = {}
#    for i in range(len(s)):
#        if s[i] in alphas:
#            answer.append(i - alphas[s[i]])
#        else:
#           answer.append(-1)
#       alphas[s[i]] = i
#    return answer
