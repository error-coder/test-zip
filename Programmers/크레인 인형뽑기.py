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
    # 크레인 움직임 출력
    for turn in moves:
        now = turn - 1
        # 해당 칸에서 뽑기가 끝나면(while 루프 끝나면) 알아서 x가 메모리 해제 -> 다시 for 루프에 들어와서 x=0으로 초기화
        x = 0
        # while 문이 x가 보드의 길이를 다 돌때까지 반복
        while (x != len(board)):
            # 칸에 구슬이 있을 때
            if board[x][now] != 0:
                # 스택 길이가 0이 아니고 마지막 원소가 칸에 있는 인형의 숫자와 같을 경우
                if len(stack) != 0 and stack[-1] == board[x][now]:
                    board[x][now] = 0
                    # 구슬이 겹치기 때문에 삭제됨
                    stack.pop()
                    # 인형의 개수가 2개가 삭제되어 2개를 더해줌
                    count += 2
                else:
                    stack.append(board[x][now])
                    board[x][now] = 0
                break
            # 인형을 찾지 못했으므로 다음 열로 이동
            x += 1
        

    return count
