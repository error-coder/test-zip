<<<<<<< HEAD
def solution(s):
    answer = ''
    arr = list(map(int, s.split(' ')))
    
    min_num = min(arr)
    max_num = max(arr)

    arr.sort()

    answer = str(min_num) + ' ' + str(max_num)

=======
def solution(s):
    answer = ''
    arr = list(map(int, s.split(' ')))
    
    min_num = min(arr)
    max_num = max(arr)

    arr.sort()

    answer = str(min_num) + ' ' + str(max_num)

>>>>>>> 6c716a35aca2fe3cc8bb69776cd4724da2f4b323
    return answer