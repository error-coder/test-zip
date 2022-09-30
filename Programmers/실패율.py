# 실패율 : 스테이지 도달했으나 아직 클리어 못한 플레이어수 / 도달한 플레이어수   
def solution(N, stages):
    
    # 실패율 - 딕셔너리
    Fail_rate = {}
    # 스테이지에 도달한 플레이어수를 늘어난 스테이지의 길이로 표현
    Total_User = len(stages)
    # 1부터 N+1까지 스테이지 반복하기
    for i in range(1, N + 1):
            # 스테이지 도달 유저가 하나도 없을때가 아닌 경우 먼저 처리
            if Total_User != 0:
                All_stages = stages.count(i)
                Fail_rate[i] = All_stages / Total_User
                Total_User -= All_stages
            # 나머지 else문이 도달유저가 하나도 없을때
            else:
                Fail_rate[i] = 0
    # 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호 배열 나열
    return sorted(Fail_rate, key=lambda N: Fail_rate[N], reverse=True)


            

        
