from itertools import permutations

# 순열로 경우의 수를 했기 때문에 완전 탐색
def isMatch(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False
        
        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    answer = []
    userList = list(permutations(user_id, len(banned_id)))
    
    for users in userList:
        if not isMatch(users, banned_id):
            continue
        else:                               # 중복을 제외하고 넣기
            users = set(users)
            if users not in answer:
                answer.append(users)
    
    return len(answer)

"""
# 처음에 해당 방법으로 풀려고 했으나 product 함수를 알지 못해 위의 방법으로 해결
# result = list(product(*result)) : 이중 리스트의 경우의 수를 알 수 있음
# [["1", "2"], ["2", "3"]] -> [("1", "2"), ("1", "3"), ("2", "2"), ("2", "3")]
from itertools import product

def check(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] == "*":
            continue
        if str1[i] != str2[i]:
            return False
    return True

def solution(user_id, banned_id):
    answer = set()
    result = [[] for i in range(len(banned_id))]

    for i in range(len(banned_id)):
        for u in user_id:
            if check(banned_id[i], u):
                result[i].append(u)

    result = list(product(*result))
    for r in result:
        if len(set(r)) == len(banned_id):
            answer.add("".join(sorted(set(r))))

    return len(answer)
"""