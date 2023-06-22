def solution(n):
    # 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
    # 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
    # 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.

    cnt = bin(n).count("1")

    for i in range(n + 1, 1000001):
        if bin(i).count("1") == cnt:
            return i


# 풀이 방법

# bin이라는 함수로 이진수 변환
# count()으로 1의 갯수를 계산

# 다른 사람 풀이
# def nextBigNumber(n):
#     count = bin(n).count('1')

#     while 1:
#         n += 1
#         if count == bin(n).count('1'):
#             break

#     return n
