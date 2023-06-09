# 이중 for문으로 풀면 시간 초과
# 원의 방정식 활용 : x^2 + y^2 = d^2

def solution(k, d):
    answer = 0
    
    for x in range(0, d+1, k):
        res = int((d**2 - x**2)**0.5)
        answer += (res // k) + 1        
        
    return answer