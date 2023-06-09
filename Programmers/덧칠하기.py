def solution(n, m, section):
    answer = 1  # 칠하는 횟수

    # 페인트가 칠해진 길이 n, 페인트를 칠하는 롤러의 길이 m
    # 페인트를 칠하기로 정한 구역들의 번호가 담긴 정수 배열 section
    # 롤러로 페인트칠해야 하는 최소 횟수 return

    paint = section[0]
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]

    return answer


# 다른 사람 풀이 1

# def solution(n, m, section):
#     answer = 1
#     prev = section[0]
#     for sec in section:
#         if sec - prev >= m:
#             prev = sec
#             answer += 1

#     return answer

# 다른 사람 풀이 2

# def solution(n, m, section):
#     n = 0
#     k = 0
#     for s in section:
#         if s > k:
#             n += 1
#             k = s+m-1
#     return n
