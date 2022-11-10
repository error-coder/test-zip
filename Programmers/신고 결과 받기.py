<<<<<<< HEAD
# 이용자 ID가 담긴 배열 id_list, 이용자가 신고한 ID정보가 담긴 배열 report
# 정지 기준이 되는 신고 횟수 k가 매개변수
# 유저별로 처리 결과 메일 받은 횟수 return
# 한 유저가 여러번 신고해도 한건으로 치기 때문에 2번 이상 신고해도 정지X
# id_list의 원소는 소문자만, 중복X
# report의 원소는 이용자 id, 신고한 id -> "muzi frodo"의 경우 muzi가 frodo를 신고함
# id는 알파벳 소문자로만 이루어짐, id는 공백 하나로 이루어짐, 자기 자신 신고X

from collections import defaultdict

def solution(id_list, report, k):
    result = []
    # 중복 신고 제거
    report = list(set(report))
    # 신고당한 횟수 저장
    num_reported = defaultdict(int)
    # 유저별 신고당한 id 저장
    ban_user = defaultdict(set)

    for name in report:
        # 공백을 기준으로 id가 신고한 유저 id, reported_id가 신고당한 유저 id
        id, reported_id = name.split(' ')
        # 신고하면 신고당한 id 더해줌
        ban_user[id].add(reported_id)
        # 신고한 id 수 추가해줌
        num_reported[reported_id] += 1

    for id in id_list:
        cnt = 0
        
        for reported_id in ban_user[id]:
            # 신고당한 횟수가 k 이상이면 1 추가해줌
            if num_reported[reported_id] >= k:
                cnt += 1

        result.append(cnt)

    return result

print(solution(["con","ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))

# 신고된 유저 아이디를 해시(또는 연관 배열) 자료구조를 이용해 관리하면 효율적으로 목록을 완성할 수 있습니다. 
# 이때, 신고한 유저 목록에는 같은 아이디가 중복되어 들어가지 않도록 주의해야 합니다.

# 위와 같이 목록을 만들었다면 신고된 유저 아이디를 순회하면서 정지 기준을 만족하는 유저가 있다면(신고한 유저 수가 k 이상이면) 
=======
# 이용자 ID가 담긴 배열 id_list, 이용자가 신고한 ID정보가 담긴 배열 report
# 정지 기준이 되는 신고 횟수 k가 매개변수
# 유저별로 처리 결과 메일 받은 횟수 return
# 한 유저가 여러번 신고해도 한건으로 치기 때문에 2번 이상 신고해도 정지X
# id_list의 원소는 소문자만, 중복X
# report의 원소는 이용자 id, 신고한 id -> "muzi frodo"의 경우 muzi가 frodo를 신고함
# id는 알파벳 소문자로만 이루어짐, id는 공백 하나로 이루어짐, 자기 자신 신고X

from collections import defaultdict

def solution(id_list, report, k):
    result = []
    # 중복 신고 제거
    report = list(set(report))
    # 신고당한 횟수 저장
    num_reported = defaultdict(int)
    # 유저별 신고당한 id 저장
    ban_user = defaultdict(set)

    for name in report:
        # 공백을 기준으로 id가 신고한 유저 id, reported_id가 신고당한 유저 id
        id, reported_id = name.split(' ')
        # 신고하면 신고당한 id 더해줌
        ban_user[id].add(reported_id)
        # 신고한 id 수 추가해줌
        num_reported[reported_id] += 1

    for id in id_list:
        cnt = 0
        
        for reported_id in ban_user[id]:
            # 신고당한 횟수가 k 이상이면 1 추가해줌
            if num_reported[reported_id] >= k:
                cnt += 1

        result.append(cnt)

    return result

print(solution(["con","ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))

# 신고된 유저 아이디를 해시(또는 연관 배열) 자료구조를 이용해 관리하면 효율적으로 목록을 완성할 수 있습니다. 
# 이때, 신고한 유저 목록에는 같은 아이디가 중복되어 들어가지 않도록 주의해야 합니다.

# 위와 같이 목록을 만들었다면 신고된 유저 아이디를 순회하면서 정지 기준을 만족하는 유저가 있다면(신고한 유저 수가 k 이상이면) 
>>>>>>> 6c716a35aca2fe3cc8bb69776cd4724da2f4b323
# 신고한 유저 목록을 순회하면서 메일을 보냈다는 표시(카운트를 1 증가) 해주면 됩니다.