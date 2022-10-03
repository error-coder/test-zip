# N마리 폰켓몬의 종류 번호가 담긴 배열 num
# N/2마리 선택 방법 중 가장 많은 종류의 폰켓몬 선택 방법을 찾아 폰켓몬 종류 번호의 개수 return
# nums - 1차원 배열, nums의 길이(N)는 자연수이며 짝수
# 폰켓몬 종류 번호는 자연수
# 많은 종류의 폰켓몬 선택 방법이 여러가지라도, 선택 가능한 폰캣몬 종류 개수의 최댓값 하나만 반환하면됨
# 최대한 다양한 종류의 폰켓몬을 가지길 원함

def solution(nums):
    result =  0
    num = len(set(nums))
    
    if len(nums) / 2 > num:
        return num
    else:
        return len(nums) / 2


    # set 함수를 사용해 nums를 새로운 배열에 담음
    # 배열의 길이가 n/2보다 길다면 n/2를 result에 담고, 짧다면 배열의 길이를 result에 담음

