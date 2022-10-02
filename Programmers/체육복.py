# 전체 학생들의 수 : n, 도난당한 학생들의 번호 배열 lost
# 여벌의 체육복을 가져온 학생들의 번호 배열 reserve
# 한 벌만 빌려줄 수 있는 학생(한 벌)과 둘 다 빌려줄 수 있는 겹치는 경우를 빼줘야됨
# 이중 배열

def solution(n, lost, reserve):
    result = []
    # 빌려줄 수 있는 사람(여벌이 있으나 여벌옷도 도난 가능성이 있음)
    set_person = set(reserve) - set(lost)
    # 잃어버린 사람
    lost_person = set(lost) - set(reserve)

    # 여벌의 체육복 있는 사람 기준
    for i in set_person:
        # 왼쪽부터 잃어버린 사람이 있으면
        if i - 1 in lost_person:
            # reserve가 하나 주고 -1 계산
            lost_person.remove(i - 1)
        # 왼쪽에 잃어버린 사람이 없으면
        elif i + 1 in lost_person:
            # 오른쪽에 하나 주니까 +1 추가
            lost_person.remove(i + 1)

    return n - len(lost_person)


   




            