def solution(players, callings):
    # 등수 순서대로 담긴 players
    # 해설진이 부른 이름을 담은 callings
    # 경주가 끝났을 때 선수들의 이름을 1등부터 순서대로 return

    answer = {}
    players_idx = {}

    for i in range(len(players)):
        answer[players[i]] = i
        players_idx[i] = players[i]

    for i in callings:
        j = answer[i]
        answer[i] = j - 1  # 부를 때마다 순서가 한칸씩 바뀜
        change_pos = players_idx[j - 1]

        answer[change_pos] = j
        players_idx[j - 1] = i
        players_idx[j] = change_pos

    return list(players_idx.values())


# 풀이 방법

# answer와 idx를 딕셔너리로 선언해주고
# players에 담겨있는 player이름과 순서를 각각 answer와 idx에 담아준다.
# answer는 player의 이름을 키값으로 순위를 저장하고
# idx는 순위를 키값으로 player의 이름을 담아준다.
# 그리고 calling반복문을 돌면서
# answer 딕셔너리 값과 idx 딕셔너리 값을 수정해 주면 된다.
# 결과값은 idx의 value값들을 뽑으면 끝 !

# 다른 사람 풀이

# def solution(players, callings):
#     pla_dic = {key: i for i, key in enumerate(players)}

#     for p in callings:
#         c = pla_dic[p]
#         pla_dic[p] -= 1
#         pla_dic[players[c-1]] += 1
#         players[c-1], players[c] = players[c], players[c-1]

#     return players

# def solution(players, callings):
#     rankDic = {}
#     playerDic = {}

#     for idx, player in enumerate(players):
#         rankDic[idx + 1] = player
#         playerDic[player] = idx + 1

#     for cur_player in callings:
#         cur_rank = playerDic[cur_player]
#         prev_rank = cur_rank - 1
#         prev_player = rankDic[prev_rank]

#         rankDic[cur_rank - 1], rankDic[cur_rank] = rankDic[cur_rank], rankDic[cur_rank - 1]
#         playerDic[prev_player], playerDic[cur_player] = playerDic[cur_player], playerDic[prev_player]


#     return list(rankDic.values())
