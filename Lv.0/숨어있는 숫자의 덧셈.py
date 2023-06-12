def solution(my_string):
    numbers = []  # 자연수들을 저장할 리스트 생성
    for char in my_string:
        if char.isdigit():  # 문자열이 숫자인 경우
            numbers.append(int(char))  # 숫자를 자연수로 변환하여 리스트에 추가
    return sum(numbers)  # 자연수들의 합 반환
