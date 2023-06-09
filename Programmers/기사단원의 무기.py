def solution(number, limit, power):
    # 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매
    # 공격력 1당 1kg 철이 필요함
    # 기사단원의 수 number, 공격력의 제한 수치 limit, 제한 수치를 초과한 기사가 사용할 무기의 공격력 power
    # 무기를 모두 만들기 위해 필요한 철의 무게 return

    def divisor_count(n):  # 약수 개수 세는 함수
        cnt = 0

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if i == (n // i):
                    cnt += 1
                else:
                    cnt += 2

        return cnt

    total_iron = 0

    for i in range(1, number + 1):
        weapon_power = divisor_count(i)

        if weapon_power > limit:
            total_iron += power
        else:
            total_iron += weapon_power

    return total_iron


print(solution(5, 3, 2))
print(solution(10, 3, 2))


# 힌트1. 약수의 개수를 효율적으로 구하는 방법
# for문을 n까지 다 돌리고 있지 않으신가요?
# 다 돌릴 필요 없고, int(n의 제곱근)까지만 돌리면 된답니다.
# range 구문에서 마지막 인수 +1을 해줘야 마지막까지 돌아간다는 것도 기억해주세요.

# 힌트2. 제곱근의 개수는 1번만 세기
# for문을 돌리다 보면, 카운트를 2번씩 하게 되는데요 (i, n//i)
# 제곱은은 i == n//i 이므로 1번만 카운트를 해줘야 합니다.

# 다른 사람 풀이

# def get_cds(n, limit , power):
#    cnt = 0
#    for i in range(1, int(n**(1/2))+1): # ★포인트1. 제곱근만큼만 반복
#        if n%i == 0:
#            if i == n//i: # 제곱근일 경우 -> 1개만 카운트하기
#                cnt += 1
#            else:
#                cnt += 2 # 제곱근이 아닐 경우, 2개 카운트 (i, n//i)
#        if cnt > limit:  # ★포인트2. 소수의 개수가 limit를 넘어가면
#            return power #            강제로 power만큼을 return
#    return cnt


# def solution(number, limit, power):
#    total = 1
#    for i in range(2, number+1):
#        len_cds = get_cds(i, limit, power)
#        total += len_cds

#    return total

# 다른 사람 풀이 2
# def get_divider_cnt(number):
#     d = []

#     for i in range(1, int(number**0.5)+1):
#         if number % i == 0:
#             d.append(i)
#             if i != number//i:
#                 d.append(number//i)

#     # d.append(number)

#     return len(d)


# def solution(knight_numbers, limit, power):
#     answer = 0
#     iron_weight = 0

#     for each_knight in range(1, knight_numbers+1):
#         cur_divider = get_divider_cnt (each_knight)
#         if cur_divider <= limit:
#             iron_weight = cur_divider
#         else:
#             iron_weight = power
#         answer += iron_weight

#     return answer
