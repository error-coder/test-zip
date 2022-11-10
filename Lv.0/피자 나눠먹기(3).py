# 피자 조각수 slice, 먹는 사람 수 n

def solution(slice, n):
    answer = 0

    if n % slice != 0:
        answer = (n // slice) + 1
    else:
        answer = n // slice
        
    return answer

# 간단한 답안

# def solution(slice, n):
#     return ((n - 1) // slice) + 1

# 직관적인 답안

# def solution(slice, n):
#     answer = n//slice

#     if n % slice != 0:
#         answer +=1

#     return answer