# lottos - 구매한 로또 번호가 담긴 배열, win_nums - 로또 당첨 번호가 담긴 배열
# return - 당첨 가능한 최고 순위, 최저 순위를 차례대로 담은 배열


def solution(lottos, win_nums):
    result = []
    count = 0
    # 0 개수 셀때
    zero_cnt = lottos.count(0)

    # 로또 안의 i 꺼내어 확인
    for i in lottos:
        # 만약 당첨번호가 i안에 들어있으면
        if i in win_nums:
            # 알아볼 수 있는 번호
            count += 1
    # 최대 번호, 최소 번호
    result = [get_num(count+zero_cnt), get_num(count)]
    
    return result

        
    
def get_num(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6




    