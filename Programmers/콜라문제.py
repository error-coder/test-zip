# 마트에 줘야 하는 병 a, 마트가 주는 병 b, 갖고 있는 병 개수 n
# 받을 수 있는 콜라 수 return(나눌 수 없을 때까지 나눈 다음 나머지를 더한 값)
# 2병에 1병으로 교환 가능

def solution(a, b, n):
    result = 0
    emptycoke = n

    while emptycoke >= a:
        havecoke = (emptycoke // a) * b
        result += havecoke
        emptycoke = (emptycoke % a) + havecoke
        

    return result

# 정수부만 얻어서 교환해주는 개수만큼 곱해서 +=하고
# 잔여 개수 = 잔여 개수에서 나눈 나머지 + 새로 얻은 콜라 개수
# 와일 루프 조건은 잔여 콜라가 최소 교환 개수랑 같거나 그보다 클때로 제한하고