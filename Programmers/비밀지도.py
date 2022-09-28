# 논리 연산자, 진법 변환
# 매개변수랑 함수내 변수 다르게 하기
def solution(n, arr1, arr2):
    result = []
    
    # arr1과 arr2를 zip으로 묶기
    for num1, num2 in zip(arr1, arr2):
        # 2진수로 바꿔줌
        elem = str(bin(num1 | num2))[2:]
        # 앞이 0으로 시작하는 2진수가 사라지기 때문에 변의 길이에서 숫자만큼 수를 뺀후 '0'을 곱하고 더함
        elem = '0' * (n - len(elem)) + elem
        # '1'을 '#'으로 대체
        elem.replace('1', '#')
        # '0'을 ' '으로 대체
        elem.replace('0', ' ')

        result.append(elem)

    for i in range(len(result)):
        buffer = ''

        for j in range(len(result[i])):
            if result[i][j] == '1':
                buffer += '#'
            else:
                buffer += ' '

        result[i] = buffer

    return result

print(solution(5, [9,20,28,18,11], [30,1,21,17,28]))


# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer

        

