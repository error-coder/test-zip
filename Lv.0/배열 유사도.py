def solution(s1, s2):
    a = list(set(s1).intersection(s2))

    return len(a)