def solution(n):
    answer = 0

    # 숫자 15는 4가지의 방법으로 구할 수 있음
    # 연속된 자연수들로 n을 표현하는 방법의 수 return

    for i in range(1, n + 1):
        sum_n = 0
        for j in range(i, n + 1):
            sum_n += j

            if sum_n == n:
                answer += 1
                break
            elif sum_n > n:
                break

    return answer


# 풀이 방법

# 완전탐색으로 풀었다.
# 2중 for문을 사용해서 1~n의 숫자부터 시작해 연속된 숫자를 sum에 더해준다.
# sum이 n이 되면 answer를 하나 올려 주고 두 번째 for문을 나가 다시 다음 숫자부터 시작한다.
# 이 때, 시간을 줄이기 위해서 sum이 n보다 커질 경우 더 이상 연속된 숫자를 더해줄 필요가 없기 때문에 두 번째 for문을 나가도록 함

# 다른 사람 풀이

# def expressions(num):
#     answer = 0
#     for i in range(1, num+1):
#         summ = 0
#         while (summ < num):
#             summ += i
#             i += 1
#         if summ == num:
#             answer += 1
#     return answer
