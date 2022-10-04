# 시작위치 : * - 왼손, # - 오른손
# 2,5,8,0의 거리배열만 생각하면될듯
# (두 넘버패드의 거리 차이 절대값) / 3의 몫 + 나머지

def solution(numbers, hand):
    result = ''
    
    dic = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    
    left_hand = [3,0]
    right_hand = [3,2]

    for i in numbers:
        if i in [1,4,7]:
            left_hand = dic[i]
            result += 'L'
        elif i in [3,6,9]:
            right_hand = dic[i]
            result += 'R'
        elif i in [2,5,8,0]:
            # 왼손 오른손 버튼에서 중간까지 거리 구하기
            mid_left = abs(dic[i][0] - left_hand[0]) + abs(dic[i][1] - left_hand[1])
            mid_right = abs(dic[i][0] - right_hand[0]) + abs(dic[i][1] - right_hand[1])
            
            # 왼쪽에서 가운데 버튼까지 가는 값이 오른쪽에서 가는 것보다 클 때
            if mid_left > mid_right:
                result += 'R'
                right_hand = dic[i]
            # 오른쪽에서 가운데 버튼까지 가는 값이 왼쪽에서 가는 것보다 클 때
            elif mid_left < mid_right:
                result += 'L'
                left_hand = dic[i]
            # 손잡이 따질때
            else:
                if hand == 'right':
                    result += 'R'
                    right_hand = dic[i]
                else:
                    result += 'L'
                    left_hand = dic[i]
    return result
