def solution(s, n):
    buffer = []

    for i in range(len(s)):
        buffer.append(ord(s[i]))

    for i in range(len(buffer)):
        # 대문자 케이스
        if buffer[i] >= 65 and buffer[i] <= 90:
            # n을 더했을때 Z를 넘어버리는 경우
            if buffer[i] + n > 90:
                buffer[i] = chr(buffer[i] + n - 26)
            else:
                buffer[i] = chr(buffer[i] + n)
        # 소문자 케이스
        elif buffer[i] >= 97 and buffer[i] <= 122:
            #  n을 더했을때 z를 넘어버리는 경우
            if buffer[i] + n > 122:
                buffer[i] = chr(buffer[i] + n - 26)
            else:
                buffer[i] = chr(buffer[i] + n)
        # 이외의 케이스(공백, 특수문자 등)
        else:
            buffer[i] = chr(buffer[i])


    return ''.join(buffer)
