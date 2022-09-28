def solution(s):
    result = s
    arr = {'zero' : '0','one' : '1','two' : '2','three' : '3','four' : '4','five' : '5',
    'six' : '6','seven' : '7','eight' : '8','nine' : '9'}
    

    for key,value in arr.items():
        result = result.replace(key, value)

    return int(result)

print(solution('one4seveneight'))