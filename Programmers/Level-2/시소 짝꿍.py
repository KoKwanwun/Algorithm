# 1:1, 1:2, 1:3, 1:4, 2:1, 2:2, 2:3, 2:4, 3:1, 3:2, 3:3, 3:4, 4:1, 4:2, 4:3, 4:4
# 중복 방지를 위해, 같은 수는 공식으로, 나머지는 2:3, 2:4, 3:4만 체크
from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    for i in range(100, 1001):
        if counter[i] > 0:
            answer += (counter[i] * (counter[i] - 1)) // 2          # 같은 수 (n개 중에 2개를 뽑는 경우의 수 공식)
            answer += counter[i] * counter[i * 3 / 2]
            answer += counter[i] * counter[i * 2]
            answer += counter[i] * counter[i * 4 / 3]
    
    return answer