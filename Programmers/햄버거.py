<<<<<<< HEAD
# 무조건 순서대로 포장해야함
# 1 -> 빵, 2 -> 야채, 3 -> 고기
# 1,2,3,1(아래부터 빵-야채-고기-빵), 포장 중 추가되거나 높이 쌓이는 일은 없음
# 2,1,1,2,3,1,2,3,1 -> 3번째부터 6번째까지 1,2,3,1을 사용후 남은 재료 중 1,2,3,1이 되는 것을 또 사용가능함
# 스택 활용

def solution(ingredient):
    result = 0
    stack = []

    for burger in ingredient:
        stack.append(burger)

        if len(stack) >= 4:
            bread2 = stack[len(stack) - 4]
            veg = stack[len(stack) - 3]
            meat = stack[len(stack) - 2]
            bread1 = stack[len(stack) - 1]

            if (bread1 == 1 and meat == 3 and veg == 2 and bread2 == 1):
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()

                result += 1
            
=======
# 무조건 순서대로 포장해야함
# 1 -> 빵, 2 -> 야채, 3 -> 고기
# 1,2,3,1(아래부터 빵-야채-고기-빵), 포장 중 추가되거나 높이 쌓이는 일은 없음
# 2,1,1,2,3,1,2,3,1 -> 3번째부터 6번째까지 1,2,3,1을 사용후 남은 재료 중 1,2,3,1이 되는 것을 또 사용가능함
# 스택 활용

def solution(ingredient):
    result = 0
    stack = []

    for burger in ingredient:
        stack.append(burger)

        if len(stack) >= 4:
            bread2 = stack[len(stack) - 4]
            veg = stack[len(stack) - 3]
            meat = stack[len(stack) - 2]
            bread1 = stack[len(stack) - 1]

            if (bread1 == 1 and meat == 3 and veg == 2 and bread2 == 1):
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()

                result += 1
            
>>>>>>> 6c716a35aca2fe3cc8bb69776cd4724da2f4b323
    return result