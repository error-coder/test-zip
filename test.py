def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in range(1,9):
            if (s.isdigit()==True):
                return True

            else:
                return False

    return False