# 스택 문제
# 게임 화면 격자 상태가 담긴 2차원 배열 - board, 크레인을 작동시킨 위치가 담긴 배열 - moves
# 모두 작동시킨 후 사라진 인형의 개수 return
# 같은 숫자가 겹칠 경우 겹친 숫자 제거

# 0,0,0,0,0
# 0,0,1,0,3
# 0,2,5,0,1
# 4,2,4,4,2
# 3,5,1,3,1


def solution(board, moves):
    stack = []
    count = 0

    for turn in moves:
        now = turn - 1
        x = 0

        while (x != len(board)):
            if board[x][now] != 0:
                if len(stack) != 0 and stack[-1] == board[x][now]:
                    board[x][now] = 0
                    stack.pop()
                    count += 2
                else:
                    stack.append(board[x][now])
                    board[x][now] = 0
                break

            x += 1
        

    return count



print(
    solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 3],
            [0, 2, 5, 0, 1],
            [4, 2, 4, 4, 2],
            [3, 5, 1, 3, 1],
        ],
        [1, 5, 3, 5, 1, 2, 1, 4],
    )
)
