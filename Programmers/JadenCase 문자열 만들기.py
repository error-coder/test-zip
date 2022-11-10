<<<<<<< HEAD
def solution(s):
    answer = ''
    s = s.split(' ')
    
    for i in range(len(s)):
        s[i] = s[i].capitalize()

        answer = ' '.join(s)

=======
def solution(s):
    answer = ''
    s = s.split(' ')
    
    for i in range(len(s)):
        s[i] = s[i].capitalize()

        answer = ' '.join(s)

>>>>>>> 6c716a35aca2fe3cc8bb69776cd4724da2f4b323
    return answer