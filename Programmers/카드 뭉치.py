def solution(cards1, cards2, goal):
    # 문자열로 이루어진 배얄 cards, 원하는 단어 배열 goal
    # goal 배열도 cards 배열에 있는 순서대로 집어넣어야 함

    # 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용합니다.
    # 한 번 사용한 카드는 다시 사용할 수 없습니다.
    # 카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다.
    # 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없습니다.

    i = 0
    j = 0

    while i + j < len(goal):
        if i < len(cards1) and cards1[i] == goal[i + j]:
            i += 1
        elif j < len(cards2) and cards2[j] == goal[i + j]:
            j += 1
        else:
            return "No"

    return "Yes"


# 다른 풀이 1
# def solution(cards1, cards2, goal):
#     for i in goal:
#         if cards1 and i == cards1[0]:
#             cards1.pop(0)
#         elif cards2 and i == cards2[0]:
#             cards2.pop(0)
#         else:
#             return 'No'
#     return 'Yes'

# goal의 모든 요소들을 순차적으로 돌며 해당 요소가 cards1 또는 cards2의 0번째 요소와 같은 지 비교하는 것이다.

# 다른 풀이 2

# def solution(cards1, cards2, goal):
#     answer = 'Yes'
#     # answer에 기본값을 'Yes'로 설정해줍니다.
#     first = 0
#     second = 0
#     # 첫번째 카드 뭉치의 확인할 위치를 담을 first와 두번째 카드 뭉치의 위치를
#     # 담을 second를 설정해줍니다.
#     for i in range(len(goal)):
#         if len(cards1) > first and cards1[first] == goal[i]:
#             first += 1
#             # cards1의 크기가 first보다 크고 cards1에서 확인할 위치가 goal에
#             # 오는 값과 같다면 first의 값을 1 더해줍니다.
#         elif len(cards2) > second and cards2[second] == goal[i]:
#             second += 1
#             # cards2의 크기가 second보다 크고 cards2에서 확인할 위치가 goal에
#             # 오는 값과 같다면 second의 값을 1 더해줍니다.
#         else:
#             answer = 'No'
#             break
#         # card1과 card2에서 goal에 와야하는 단어가 올 수 없다면 answer를 'No'로
#         # 바꾸고 출력해줍니다.
#     return answer

# 다른 풀이 3
# from collections import deque

# def solution2(cards1, cards2, goal):
#     cards1 = deque(cards1)
#     cards2 = deque(cards2)

#     for word in goal:
#         if card1 and word == cards1[0]: cards1.popleft()
#         if card2 and word == cards2[0]: cards2.popleft()
#         else: return 'No'

#     return 'Yes'

# 문제를 해결 할 수 있는 방법을 두가지 정도 생각해봄

# 두 개의 인덱스 변수를 사용해 순차적으로 비교하는 방법
# 큐를 사용해 앞에서 부터 pop 하는 방법
# 👉 큐나 스택을 이용해 pop을 수행할 때 반드시 비어있는지 확인하자
