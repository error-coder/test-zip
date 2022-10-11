def solution(s):
    answer = ''
    arr = list(map(int, s.split(' ')))
    
    min_num = min(arr)
    max_num = max(arr)

    arr.sort()

    answer = str(min_num) + ' ' + str(max_num)

    return answer