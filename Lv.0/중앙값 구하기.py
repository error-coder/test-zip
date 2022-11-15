import statistics

def solution(array):
    new_arr = sorted(array)

    return statistics.median(new_arr)