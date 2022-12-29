import collections

def solution(n, words):
    answer = []

    # words의 개수, words를 set 처리한 후 개수를 빼주면, 중복된 값들만 구할 수 있음
    """
    예시
    Counter({'tank': 2, 'know': 1, 'wheel': 1, 'land': 1, 'dream': 1, 'mother': 1, 'robot': 1, 'kick': 1})
    Counter({'tank': 1, 'know': 1, 'wheel': 1, 'land': 1, 'dream': 1, 'mother': 1, 'robot': 1, 'kick': 1})
    dict_keys(['tank'])
    """
    mdict_list = collections.Counter(words)
    mdict_set = collections.Counter(set(words))
    duplicated_key = (mdict_list - mdict_set).keys()

    # 중첩 단어를 0으로 초기화하여 dictionary 만들기
    mdict = {word:0 for word in list(duplicated_key)}

    # for문을 1부터 시작하므로 만약 words의 첫번째 값이 keys에 있다면 해당 값을 +1 해주기
    if(words[0] in list(mdict.keys())):
        mdict[words[0]] += 1

    for i in range(1, len(words)):
        # words의 i번째 값이 중첩 단어에 있다면 +1 해주기
        if(words[i] in list(mdict.keys())):
            mdict[words[i]] += 1

            # 만약 값이 2라면 이전에 한번 나왔으므로 리턴
            if(mdict[words[i]] == 2):
                answer.append((i % n) + 1)
                answer.append((i // n) + 1)
                break

        # 끝말잇기가 되었다면 다음 차례로 넘어가고, 안되었다면 리턴
        if(words[i - 1][-1] == words[i][0]):
            continue
        else:
            answer.append((i % n) + 1)
            answer.append((i // n) + 1)
            break

    # answer이 []라면 탈락한 사람이 없으므로 [0, 0] 으로 리턴
    if(answer == []):
        answer = [0, 0]

    return answer