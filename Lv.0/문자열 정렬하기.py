import re

def solution(my_string):
    answer = 0
    
    answer = re.findall(r'\d', my_string)

    return sorted(answer)