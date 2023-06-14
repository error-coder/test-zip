def time_convert(time):
    year, month, day = map(int, time.split("."))
    return year * 12 * 28 + month * 28 + day


def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    today = time_convert(today)

    # 모든 달은 28일까지 있다고 가정합니다.
    # 오늘 날짜를 의미하는 문자열 today, 약관의 유효기간을 담은 1차원 문자열 배열 terms와 수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies가 매개변수로 주어집니다. 이때 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return

    for term in terms:
        code, period = term.split(" ")
        terms_dict[code] = int(period) * 28

    for idx, privacy in enumerate(privacies):
        start_date, code_name = privacy.split(" ")
        end_date = time_convert(start_date) + terms_dict[code_name]
        if end_date <= today:
            answer.append(idx + 1)

    return answer


# 풀이 설명

#  연도및 월을 일자로 환산하고(한 달은 28일까지밖에 없다고 가정했으므로 더 간단하다), 각 이용약관에 명시된 기간을 더해준 값이 현재 일자를 지났는지 여부를 판단해주면 된다.
