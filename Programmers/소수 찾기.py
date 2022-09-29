def isPrime(num):
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False

    return True



def solution(n):
    
    result = 0
    
    # 소수는 1과 자기자신 제외하면 자연수 중 어떤 숫자로도 떨어지지 않는 숫자
    # 1은 포함 X, 에리토스테네스의 체
    # --------------------------------------------      
    # 2부터 N까지의 모든 자연수를 나열한다.
    # 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
    # 남은 수 중에서 i의 배수를 모두 제거한다.(i는 제거하지 않는다.)
    # 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.
    
    
    # 2부터 n까지(제곱근) 모든 수 나열
    for i in range(2, n + 1):
        if isPrime(i) != 0:
            result += 1

    return result

