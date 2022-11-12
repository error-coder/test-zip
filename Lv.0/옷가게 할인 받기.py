def solution(price):
    result = 0
    if price >= 500000:
        result = price * 0.8
    elif price >= 300000:
        result = price * 0.9
    elif price >= 100000:
        result = price * 0.95
    elif price < 100000:
        result = price

    return int(result)