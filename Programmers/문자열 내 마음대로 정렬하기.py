# strings의 글자 중 n번째 순서 글자 오름차순 정렬

def solution(strings, n):
    
    strings.sorted()

    return sorted(strings, key=lambda string : string[n])





