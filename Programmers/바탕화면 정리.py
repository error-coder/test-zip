def solution(wallpaper):
    x = []
    y = []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                x.append(i)
                y.append(j)

    return [min(x), min(y), max(x) + 1, max(y) + 1]


# 풀이 설명

# 1. "#" 이라는 문자있으면 파일이 있다는 뜻으로 파일의 위치를 행을 뜻하는 row 배열에 파일의 행을 담고, 열을 뜻하는 col 배열에 파일의 열을 담습니다.
# 2. 해당 row와 col 배열에서 제일 작은 값이 이 사각형의 시작 점이 되고, 제일 큰 값이 사각형의 끝나는 점이 됩니다.


# 다른 사람 풀이

# def solution(wallpaper):
#     rdx, rdy = 0, 0
#     lux, luy = 50, 50
#     for i in range(len(wallpaper)):
#         for j in range(len(wallpaper[0])):
#             if wallpaper[i][j] == '#':
#                 if j <= lux:
#                     lux = j
#                 if i <= luy:
#                     luy = i
#                 if i+1 >= rdx:
#                     rdx = i+1
#                 if j+1 >= rdy:
#                     rdy = j+1


#     answer = [luy, lux, rdx, rdy]
#     return answer

# 다른 사람 풀이 2

# def solution(wallpaper):
#     x, y = [], []
#     for i, row in enumerate(wallpaper):
#         for j, val in enumerate(row):
#             if val == '#':
#                 x.append(i)
#                 y.append(j)

#     a, b = min(x), min(y)
#     c, d = max(x), max(y)
#     return [a, b, c+1, d+1]
