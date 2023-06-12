from functools import reduce


def multiply(arr):
    return reduce(lambda x, y: x * y, arr)


def solution(num_list):
    if sum(num_list) ** 2 >= multiply(num_list):
        return 1
    else:
        return 0
