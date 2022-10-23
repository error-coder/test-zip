# 마트에 줘야 하는 병 a, 마트가 주는 병 b, 갖고 있는 병 개수 n
# 받을 수 있는 콜라 수 return(나눌 수 없을 때까지 나눈 다음 나머지를 더한 값)
# 2병에 1병으로 교환 가능

def solution(a, b, n):
    result = 0

    while n >= a :
        receivecoke = (n / a) * b
        n = (n % a) + b

        result += receivecoke
        

    return result

print(solution(2,1,20))