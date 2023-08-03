from itertools import permutations

def solution(k, dungeons):
    # 최대 횟수를 구하기 위한 초기화
    maxResult = 0

    # 모든 순열로 for문
    for dungeon in list(permutations(dungeons, len(dungeons))):
        # 각 순열의 횟수를 구하기 위해 초기화 
        result = 0
        tmpK = k
        # 던전의 최소 필요 피로도 및 소모 피로도 꺼내기
        for each in dungeon:
            # 최소 필요 피로도보다 현재 피로도가 크다면 횟수 +1, 현재 피로도에서 소모 피로도 빼주기
            if tmpK >= each[0]:
                result += 1
                tmpK -= each[1]
        # 최대 횟수 구하기
        if (maxResult < result):
            maxResult = result

    return maxResult