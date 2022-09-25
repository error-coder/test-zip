def solution(n):
    
    # 문자열을 담을 binary_sys 선언
    binary_sys =''

    while n > 0:
        # divmod 몫과 나머지를 알 수 있는 메소드
        n, mod = divmod(n ,3)
        # 나머지를 binary_sys에 문자열로 넣음
        binary_sys += str(mod)
    # binary_sys가 문자열이므로 바로 10진법으로 변환
    result = int(binary_sys, 3)

    return result

