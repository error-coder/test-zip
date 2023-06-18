def solution(park, routes):
    # "E 5" -> 현재 위치에서 동쪽으로 5칸 이동했단 의미
    # 두 가지를 먼저 확인
    # 1. 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
    # 2. 주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
    # 두 가지 중 하나라도 해당됨면 해당 명령을 무시 후 다음 명령 수행
    # 가로 길이 W, 세로 길이 H
    # 공원의 좌측 상단의 좌표는 (0, 0), 우측 하단의 좌표는 (H - 1, W - 1) 입니다.

    # 공원을 나타내는 문자열 배열 park, 수행할 명령이 담긴 배열 routes
    # 모든 명령 수행 후 놓인 위치 -> [세로 방향, 가로 방향 좌표] 순으로 return

    # park[i]는 S,O,X 로 이루어져 있음, 직사각형 모양
    # routes의 각 원소는 수행할 명령어, 첫 번째 부터 순서대로 명령 수행
    # "op n"과 같은 구조 -> op는 이동할 방향, n은 이동할 칸의 수
    # op -> N, S, W, E

    for x in range(len(park)):
        for y in range(len(park[0])):
            if park[x][y] == "S":
                dir_x, dir_y = x, y
                break

    directions = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

    for route in routes:
        direction, count = route.split()
        dx, dy = directions[direction][0], directions[direction][1]

        flag = True

        for i in range(1, int(count) + 1):
            tx, ty = dir_x + dx * i, dir_y + dy * i

            if 0 <= tx < len(park) and 0 <= ty < len(park[0]):
                pass
            else:
                flag = False
                break

            if park[tx][ty] == "X":
                flag = False
                break
            else:
                pass

        if flag:
            dir_x, dir_y = tx, ty

    return [dir_x, dir_y]


# 풀이
# 단순한 구현 유형

# 1. 시작점 찾기
# park 리스트에 S를 찾아 그 행과 열 위치 기록
# for row in range(len(park)):
#     for col in range(len(park)[0]):
#         if park[row][col] == "S": # 시작점 찾기
#             cur_x, cur_y = row, col
#             break


# 2. 방향, 횟수 세팅
# 동서남북 방향에 따라 행,열을 움직여야 하기 때문에 이를 딕셔너리에서 받아옴
# 몇 번을 움직여야 하는지도 정수로 받으면 좋음
# directions = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
# for route in routes:
#     direction, count = route.split()
#     dx, dy = directions[direction][0], directions[direction][1]

# 3. 조건을 만족했는지 확인하는 지표 - flag

# 조건이 만족되지 않은 경우를 False로 바꿈
# 위 코드에서 첫 번째 조건은 '범위' -> 이동을 하더라도 격자판 위에 존재하는지 확인하는 것
# 두 번째 조건은 '장애물' -> 이동할 위치에 장애물이 없어야 함

# 두 조건 중 하나라도 만족이 되지 않은 경우 flag는 False로 바뀌어 for문은 종료됨
# for문으로 모든 요소를 따질 때도 flag가 True로 유지된 경우에만 현재 위치를 업데이트함

# 즉, 범위를 벗어나게 되거나 중간에 장애물을 만난 경우는 cur_x, cur_y 위치를 그대로 유지함
# 그렇지 않은 경우 tx, ty로 업데이트 함

# 다른 사람 풀이

# def solution(park, routes):
#     H, W = len(park), len(park[0])
#     directions = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

#     # 시작 위치 찾기
#     start = None
#     for i in range(H):
#         for j in range(W):
#             if park[i][j] == "S":
#                 start = (i, j)
#                 break
#         if start is not None:
#             break

#     # 현재 위치를 시작 위치로 설정
#     curr_pos = start

#     # 명령어 순회
#     for route in routes:
#         direction, distance = route[0], int(route[2])
#         dx, dy = directions[direction]

#         # 명령어에 따른 예상 위치 계산
#         new_pos = (curr_pos[0] + dx * distance, curr_pos[1] + dy * distance)

#         # 예상 위치가 공원 내에 있는지 확인
#         if 0 <= new_pos[0] < H and 0 <= new_pos[1] < W:
#             # 장애물이 있는지 확인
#             obstacle = False
#             for i in range(distance):
#                 check_pos = (curr_pos[0] + dx * (i+1), curr_pos[1] + dy * (i+1))
#                 if park[check_pos[0]][check_pos[1]] == "X":
#                     obstacle = True
#                     break

#             # 장애물이 없다면 위치를 업데이트
#             if not obstacle:
#                 curr_pos = new_pos

#     return [curr_pos[0], curr_pos[1]]
