def solution(n):
    answer = 0

    for i in range(1, n + 1):
        j = n % i

        if j == 0:
            answer += 1
        else:
            continue

    return answer


# 다른 사람 풀이 1

# def solution(n):
#     answer = 0
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             answer += 2

#             if i * i == n:
#                 answer -= 1

#     return answer

# 다른 사람 풀이 2

# def solution(n):
#     return len(list(filter(lambda v: n % (v+1) == 0, range(n))))

# 가장 많은 풀이

# def solution(n):
#     answer =0
#     for i in range(n):
#         if n % (i+1) ==0:
#             answer +=1
#     return answer
