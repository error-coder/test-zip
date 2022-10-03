# 마라톤에 참여한 선수 배열 participant
# 완주한 선수들의 이름 배열 completion
# 완주하지 못한 선수의 이름을 return

def solution(participant, completion):
    result = ''
    # participant, completion을 모두 정렬해줌
    participant.sort()
    completion.sort()
    
    # zip 함수는 자료형을 묶어주는 함수를 말한다.
    for part, comp in zip(participant, completion):
        # 만약 part와 comp에 있는 선수가 같지 않으면 일단 part 반환해줌
        if part != comp:
            return part
    
    # 들어오지 못한 사람은 따로 빠져있기 때문에 배열의 맨 끝에 위치해서 역인덱스로 찾아줌 
    return participant[-1]

    # 나중에 해시로 다시 풀어보자