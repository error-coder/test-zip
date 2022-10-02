# - 배열에 직접 접근 가능한 방법
# - **arr[-1] = arr[-1] * point** → 이런 식으로 접근 가능
# - **Isnumeric**이라는 문자열 내장함수를 이용해 숫자인 경우 s에 저장하고 S나, D, T, *, #가 오는 경우 저장된 점수 처리해줌

def solution(dartResult):
    result = 0
    score = []
    n = ''

    for dart_num in dartResult:
        # '*', '#'이 아닌 문자라면
        if dart_num.isnumeric():
            n += dart_num
        elif dart_num == 'S':
            score.append(int(n)**1)
            n = ''
        elif dart_num == 'D':
            score.append(int(n)**2)
            n = ''
        elif dart_num == 'T':
            score.append(int(n)**3)
            n = ''
        else:
            # 스타상인 경우
            if dart_num == '*':
                point = 2
                if len(score) < 2:
                    score[-1] = score[-1] * point
                else:
                    score[-2] = score[-2] * point
                    score[-1] = score[-1] * point
            # 아차상인 경우
            elif dart_num == '#':
                score[-1] = -score[-1]

    return sum(score)
