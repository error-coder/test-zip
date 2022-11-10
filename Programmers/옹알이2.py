<<<<<<< HEAD
def solution(babbling):
    result = 0

    for word in babbling:
        stack = ''
        prev = ''

        for char in word:
            stack += char

            if prev != stack and (stack == 'aya' or stack == 'ye' or stack == 'woo' or stack == 'ma'):
                prev = stack
                stack = ''
                
        if len(stack) == 0:
            result += 1

    return result


# 문자열 배열 발음할 수 있는 단어의 개수 return
# 배열 안의 발음이 아니면 무조건 발음 못함
# 같은 단어만 반복되도 발음할 수 있는걸로 됨
=======
def solution(babbling):
    result = 0

    for word in babbling:
        stack = ''
        prev = ''

        for char in word:
            stack += char

            if prev != stack and (stack == 'aya' or stack == 'ye' or stack == 'woo' or stack == 'ma'):
                prev = stack
                stack = ''
                
        if len(stack) == 0:
            result += 1

    return result


# 문자열 배열 발음할 수 있는 단어의 개수 return
# 배열 안의 발음이 아니면 무조건 발음 못함
# 같은 단어만 반복되도 발음할 수 있는걸로 됨
>>>>>>> 6c716a35aca2fe3cc8bb69776cd4724da2f4b323
