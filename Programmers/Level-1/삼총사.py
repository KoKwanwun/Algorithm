from itertools import combinations

def solution(number):
    answer = 0

    # combinations로 합이 0이면 경우의 수 추가
    for each in combinations(number, 3):
        if sum(each) == 0:
            answer += 1

    return answer