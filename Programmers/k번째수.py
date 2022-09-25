# 배열을 자르고 정렬
# 모든 원소에 대해 연산 적용한 결과 반환

def solution(array, commands):
    result = []


    for i in range(len(commands)):
        # index가 0부터 시작이라 -1을 빼준다
        new_arr = array[commands[i][0]-1 : commands[i][1]]
        new_arr.sort()
         
        result.append(new_arr[commands[i][2] - 1])

    return result

        

