def solution(my_string):
    vowel = 'a,e,i,o,u'
    result = ''

    for i in my_string:
        if i not in vowel:
            result += i

    return result

# 간단한 답안
# def solution(my_string):
#     vowels = ['a','e','i','o','u']
#     for vowel in vowels:
#         my_string = my_string.replace(vowel, '')
#     return my_string

# 직관적인 답안
# def solution(my_string):
#     answer = ''

#     for c in my_string:
#         if c in ['a', 'e', 'i', 'o', 'u']:
#             continue
#         answer += c

#     return answer