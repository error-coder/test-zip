# X, Y의 공통된 숫자 k(0 <= k <= 9)
# X, Y의 짝꿍이 존재하지 않으면 짝꿍이 -1
# X, Y의 짝꿍이 0으로만 구성되면 짝꿍은 0
# 3 <= X, Y의 길이(자릿수) <= 3000000
# X, Y는 0으로 시작X
# X, Y의 짝꿍은 문자열로 반환
# X, Y문자열을 서로 비교해 같은 값을 추출함


def solution(X, Y):
    result = ''
    countX = {}
    countY = {}
    intersection = {}


    # X를 순회하며 해당 원소 개수를 카운트해줌
    for x in X:
        if (x in countX):
            countX[x] += 1
        else:
            countX[x] = 1

    # Y를 순회하며 해당 원소 개수를 카운트해줌
    for y in Y:
        if (y in countY):
            countY[y] += 1
        else:
            countY[y] = 1

    # key -> 값, value -> 개수
    # 교집합의 개수를 구하기 위해 한쪽 딕셔너리만 조사
    for key in countX.keys():
        if (key in countX) and (key in countY):
            # 겹치는 값 개수는 둘 원소의 밸류 중 최솟값(max는 합집합)
            intersection[key] = min(countX[key], countY[key])

    # 파이썬은 저장 순서를 보장해주는데 슷자가 정렬되어 있다는 보장이 없기 
    # 때문에 정리해주는 과정이 필요함
    sortedKey = sorted(intersection.keys())
    
    # 정렬된 key를 기반으로 교집합에 들어있는 개수만큼 
    # 오름차순으로 정렬해야 하기 때문에 앞에 buffer를 더해줌
    for key in sortedKey:
        buffer = ''
        for i in range(intersection[key]):
            buffer += key
        result = buffer + result

    # 예외 처리
    if len(result) == 0:
        return "-1"
    
    # result 안에 0만 있는 경우
    if result[0] == "0":
        return "0"        


    return result

