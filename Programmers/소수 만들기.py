from itertools import combinations

def isPrime(num):
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False

    return True


def solution(nums):
    result = 0
    nums = list(combinations(nums,3))

    for i in nums:
        if isPrime(i[0]+i[1]+i[2]):
            result += 1

    return result