def solution(n):
    result = 0
    a = 0
    b = 0

    for i in n:
        n = a * b
        
        if n % i == 0:
            result += i

    return result