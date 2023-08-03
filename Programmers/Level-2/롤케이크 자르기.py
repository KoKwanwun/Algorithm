from collections import Counter

def solution(topping):
    answer = 0

    # 추가할 left는 Set 사용
    left = set()
    right = Counter(topping)

    for i in range(len(topping)):
        # topping 개수만큼 left에 추가하고 right에서 빼주기
        left.add(topping[i])
        right[topping[i]] -= 1
        
        # 원소를 제거한 후, value가 0이면 key 제거
        if right[topping[i]] == 0:
            right.pop(topping[i])
        if len(left) == len(right.keys()):
            answer += 1

    return answer