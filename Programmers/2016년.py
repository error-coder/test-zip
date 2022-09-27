def solution(a,b):

    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    LastDay = [31,29,31,30,31,30,31,31,30,31,30,31]

    return day[(sum(LastDay[:a-1]) + b - 1) % 7]

print(solution(5,24))