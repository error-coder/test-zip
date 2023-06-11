def solution(s, skip, index):
    answer = ""
    # 문자열 s와 skip, 자연수 index

    # 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔줍니다.
    # index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아갑니다.
    # skip에 있는 알파벳은 제외하고 건너뜁니다.
    # skip에 포함되는 알파벳은 s에 포함되지 않습니다.

    alpha = "abcdefghijklmnopqrstuvwxyz"  # 알파벳

    for elem in skip:
        if elem in alpha:
            alpha = alpha.replace(elem, "")  # 알파벳 안에 skip 문자들 제거

    for new_elem in s:
        change_elem = alpha[
            (alpha.index(new_elem) + index) % len(alpha)
        ]  # s의 문자 인덱스 + index를 alpha의 길이로 나눈 나머지를 알파벳으로 변환
        answer += change_elem

    return answer


# 대다수가 아스키 코드 변환 내장 함수를 이용해 풀이함

# a -> b,c,d,e,f(b,d 제외) -> c,e,f,g,h ->h
# u -> v,w,x,y,z(w 제외) -> v,x,y,z,a -> a


# 다른 사람 풀이 1

# from string import ascii_lowercase

# def solution(s, skip, index):
#     result = ''

#     a_to_z = set(ascii_lowercase)
#     a_to_z -= set(skip)
#     a_to_z = sorted(a_to_z)
#     l = len(a_to_z)

#     dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

#     for i in s:
#         result += a_to_z[(dic_alpha[i] + index) % l]

#     return result

# 다른 사람 풀이 2

# def solution(s, skip, index):
#     answer = ''
#     skip = set(ord(w) for w in skip)
#     for word in s:
#         cnt = index
#         word = ord(word)
#         while cnt != 0:
#             word += 1
#             if word > ord('z'):
#                 word = word - ord('z') + ord('a') - 1
#             if word in skip:
#                 continue
#             cnt -= 1
#         answer += chr(word)
#     return answer
