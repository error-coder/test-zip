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
