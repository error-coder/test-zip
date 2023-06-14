def solution(keymap, targets):
    answer = []

    # 문제 설명
    # 휴대폰의 자판은 컴퓨터 키보드 자판과는 다르게 하나의 키에 여러 개의 문자가 할당될 수 있습니다. 키 하나에 여러 문자가 할당된 경우, 동일한 키를 연속해서 빠르게 누르면 할당된 순서대로 문자가 바뀝니다.
    # 예를 들어, 1번 키에 "A", "B", "C" 순서대로 문자가 할당되어 있다면 1번 키를 한 번 누르면 "A", 두 번 누르면 "B", 세 번 누르면 "C"가 되는 식입니다.

    # 1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열배열 keymap
    # 입력하려는 문자열들이 담긴 문자열 배열 targets
    # 각 문자열을 작성하기 위해 키를 최소 몇 번씩 눌러야 하는지 배열에 담아 return
    # 목표 문자열을 작성할 수 없을 땐 -1

    keytable = {}

    for keys in keymap:
        for i, key in enumerate(keys):
            if key not in keytable:
                keytable[key] = i + 1
            else:
                keytable[key] = min(keytable[key], i + 1)

    for target in targets:
        click_time = 0
        for key in target:
            if key not in keytable:
                click_time = -1
                break
            click_time += keytable[key]

        answer.append(click_time)

    return answer


# 풀이 설명

# 자판의 정보 keymap이 주어진다. keymap[i]는 i + 1번 키에 대한 정보이다.

# 예를 들어 ["ABACD", "BCEFD"]로 주어지면, 1번 키는 ABACD, 2번 키는 BCEFD 키를 가지고 있는 것임.

# 그리고 targets를 완성할 수 있는 최소 횟수를 리턴하면 된다. 만약 만들 수 없다면 -1을 리턴한다.

# 접근 : 그리디 + 브루트포스
# A라는 문자를 가진 키가 여러 개 있을 수 있지만, 우리는 그 중 가장 빠른 키만 찾으면 된다.

# 예를 들어 ["ABACD", "BCEFD"] 라는 키 정보가 주어졌을 때,

# A는 1번 눌러서 입력할 수도 있고, 3번 눌러서 입력할 수도 있다. 하지만 최소횟수는 1번이다.

# 따라서 아래와 같이 입력받은 모든 키 정보에 대해서, 최소로 누를 수 있는 횟수로만 갱신한다
# 시간복잡도는 O(N^2)이다. 하지만 keymap의 길이는 최대 100, keymap원소의 길이도 최대 100이기 때문에 시간초과가 날 일은 없을 것이다.

# 그리고 이제 이 값을 이용해서 값이 들어있지 않다면 입력할 수 없는 문자고, 입력할 수 있다면 이 테이블의 value 값이 최소 횟수 이므로 매번 더해주기만 하면 된다.


# 다른 사람 풀이

# def solution(keymaps,targets):
#     data=dict()
#     keylist=[]
#     ans=[]
#     for key in keymaps:
#         for k in key:
#             if k not in keylist:
#                 data[k]=key.index(k)+1
#                 keylist.append(k)
#             else:
#                 if key.index(k)+1<data[k]:
#                     data[k]=key.index(k)+1
#     for target in targets:
#         tmp=0
#         for t in target:
#             if t not in keylist:
#                 tmp=-1
#                 break
#             else:
#                 tmp+=data[t]
#         ans.append(tmp)
#     return ans
