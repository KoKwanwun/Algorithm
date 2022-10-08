from itertools import combinations

# 조합 함수를 통해 2개씩 뽑은 후 더하여 리스트에 추가
# 겹치는 것은 set을 통해 제거 후 정렬
def solution(numbers):
    answer = []
    for i in list(combinations(numbers, 2)):
        answer.append(sum(i))
    
    return sorted(list(set(answer)))