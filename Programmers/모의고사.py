def solution(answers):
    # 가장 많이 맞힌 사람 나타내는 리스트
    result = []
    # 수포자가 맞힌 수 리스트 나열
    supo_arr = [0,0,0]

    # 수포자1은 5자리 반복
    arr1 = [1,2,3,4,5]
    # 수포자2은 8자리 반복
    arr2 = [2,1,2,3,2,4,2,5]
    # 수포자3은 10자리 반복
    arr3 = [3,3,1,1,2,2,4,4,5,5]

    # 입력 답안 바탕으로 수포자가 얼마나 맞았는지 반복
    for i in range(len(answers)):
        # 수포자1은 5를 주기로 반복
        if arr1[i % 5] == answers[i]:
            supo_arr[0] += 1
        # 수포자2는 8을 주기로 반복
        if arr2[i % 8] == answers[i]:
            supo_arr[1] += 1
        # 수포자3은 10을 주기로 반복
        if arr3[i % 10] == answers[i]:
            supo_arr[2] += 1


    for i in range(len(supo_arr)):
        max_elem = max(supo_arr)
        if supo_arr[i] == max_elem:
            result.append(i + 1)


    return result
    


# 풀이 후 ----> 매개변수를 활용안하고 빈 리스트를 순회하였음
# 순회할 때 필요한 변수들을 잘 확인하자