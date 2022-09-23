def solution(s):
    answer = []
    words = s.split(' ')
    buffer = ''

    for i in range(len(words)):
        for j in range(len(words[i])):
            if j % 2 == 0:
                buffer += words[i][j].upper();
            else:
                buffer += words[i][j].lower();
        answer.append(buffer)
        buffer = ''


    return ' '.join(answer)