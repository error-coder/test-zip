def solution(n):
    answer = [0, 1]  # F(0) = 0, F(1) = 1

    # F(0) = 0, F(1) = 1, 1이상의 n에 대해 F(n) = F(n-1) + F(n-2)
    # 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴

    for i in range(2, n + 1):
        answer.append((answer[i - 1] + answer[i - 2]) % 1234567)

    return answer[-1]


# 다른 사람 풀이

# def fibonacci(num):
#     a, b = 0, 1
#     for i in range(num):
#         a, b = b, a+b
#     return a

# 다른 사람 풀이 2

# def fibonacci(num):
#     answer=[0,1]
#     for i in range(2,num+1):
#         answer.append(answer[i-1]+answer[i-2])
#     return answer[-1]
