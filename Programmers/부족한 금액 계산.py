def solution(price, money, count):
    answer = 0
    Using_price = 0

    for i in range(1, count+1):
        Using_price += price * i

        if Using_price > money :
            answer = abs(Using_price - money)
        
    return answer
