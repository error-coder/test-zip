<<<<<<< HEAD
# 학생들의 번호 배열 number
# 삼총사 만드는 방법의 수 return
# 백트래킹 알고리즘 참고

def solution(number):
    result = []
  
    def recursion(arr, idx):
        if len(arr) == 3 and arr[0] + arr[1] + arr[2] == 0:
            result.append(arr)
            return
        
        if len(arr) < 3:
            for i in range(idx + 1, len(number)):
                recursion([*arr, number[i]], i)

    # 초기 조건 설정
    for i in range(len(number)):
        recursion([number[i]], i)

    # result 리스트의 길이 반환
    return len(result)
=======
# 학생들의 번호 배열 number
# 삼총사 만드는 방법의 수 return
# 백트래킹 알고리즘 참고

def solution(number):
    result = []
  
    def recursion(arr, idx):
        if len(arr) == 3 and arr[0] + arr[1] + arr[2] == 0:
            result.append(arr)
            return

        if len(arr) < 3:
            for i in range(idx + 1, len(number)):
                recursion([*arr, number[i]], i)

    for i in range(len(number)):
        recursion([number[i]], i)


    return len(result)


print(solution([-2,3,0,2,-5]))
>>>>>>> 6c716a35aca2fe3cc8bb69776cd4724da2f4b323
