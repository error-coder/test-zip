def solution(s):
    answer = []
    cnt, zero_cnt = 0, 0

    # x의 모든 0을 제거
    # x의 길이를 c라 할 때, x를 "c를 2진법으로 표현한 문자열"로 바꿈
    #  s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수 return

    while True:
        if s == "1":
            break

        zero_cnt += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]

        cnt += 1
        answer = [cnt, zero_cnt]

    return answer


# 풀이 방법

# 문자열 s가 들어왔을 때 0의 갯수를 세고, 0을 제거한다.
# 제거된 문자열 s의 길이를 2진수로 변환하고 위의 작업을 "1"이 남을 때까지 반복한다.
# s.count("0")로 문자열 s의 0의 갯수를 세고 zeroCnt에 저장한다.
# s.replace("0", '')를 통해 문자열 s의 0을 공백으로 치환한다. (예시 : 1010 -> 11)
# bin( ) 함수는 이진수로 변환해주는 역할을 한다.
# bin(len(s))은 문자열의 s의 길이를 이진 문자열로 변환하게 한다.
# bin(len(s))[2:]은 이진 문자열을 알려주는 "0b"을 생략하게 해준다.

# 다른 사람 풀이

# def solution(s):
#     a, b = 0, 0
#     while s != '1':
#         a += 1
#         num = s.count('1')
#         b += len(s) - num
#         s = bin(num)[2:]
#     return [a, b]

# 풀이 방법

# a = 몇회차에 '1'로 끝났는지
# b = s의 총 길이에서 숫자 1의 갯수만큼 뺌  = 0의 갯수
