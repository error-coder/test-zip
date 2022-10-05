# 신규 유저가 입력한 아이디 new_id
# 추천 아이디 return


def solution(new_id):
    result = ""
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for elem in new_id:
        # 숫자와 소문자는 메서드를 써서 판단한 다음 나머지 글자 빼줌
        if elem.islower() or elem.isdigit() or elem in ["-", "_", "."]:
            result += elem
    # 3단계
    while ".." in result:
        result = result.replace("..", ".")

    # 4단계
    if result[0] == ".":
        # .이 처음에 오면 삭제되기 때문에 최소 2글자 이상부터 크기를 재야함
        # 밑 부분의 조건을 안달았을 시 인덱스 에러 발생
        if len(result) >= 2:
            result = result[1:]

    if result[-1] == ".":
        result = result[:-1]

    # 5단계
    if result == "":
        result += "a"

    # 6단계
    if len(result) >= 16:
        result = result[:15]
        # 마침표 마지막에 있을 때 제거
        if result[-1] == ".":
            result = result[:-1]

    # 7단계
    while len(result) <= 2 :
        result += result[-1]

    return result
