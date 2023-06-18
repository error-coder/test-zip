def solution(A, B):
    answer = 0

    A.sort(reverse=True)
    B.sort()

    for i in enumerate(len(A)):
        answer += A[i] * B[i]

    return answer


# 풀이 방법

# sort 함수를 이용해 A는 내림차순, B는 오름차순으로 정렬한다.
# 그 후 같은 인덱스끼리 곱한 뒤 누적해서 더하면 최솟값이 될 것이다.

# 다른 사람 풀이
# def getMinSum(A, B):
#     return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])

# 다른 사람 풀이 2

# def getMinSum(A,B):
#    if len(A) == 0 : return 0
#    s = []
#    for i in range(len(A)):
#        a = A.pop(A.index(min(A)))
#        b = B.pop(B.index(max(B)))
#        s.append(a*b)
#    return sum(s)
