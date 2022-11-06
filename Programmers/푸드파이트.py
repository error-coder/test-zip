def solution(food):
    # 음식 양을 담을 스택을 하나 선언해줌
    food_stack = []

    for var in range(1, len(food)):
        # 더미 변수를 붙인 반복문을 실행함(더미 변수는 실제 사용되진 않음)
        # % 연산자는 나머지를 호출, //는 나머지를 버리고 몫 값만 호출
        for _ in range(food[var] // 2):
            food_stack.append(var)

    return ''.join(map(str, (food_stack + [0] + food_stack[::-1])))