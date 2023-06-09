# 이중 for문으로 풀면 시간 초과
# 원의 방정식 활용 : x^2 + y^2 = d^2
# y의 최대값을 구한 후, 내부에 찍을 수 있는 점의 개수를 소수점을 제거한 y/k+1 값과 같다
# (k의 배수이기 때문에 k로 나누고, 0을 포함하기 위해 +1)

def solution(k, d):
    answer = 0
    
    for x in range(0, d+1, k):
        res = int((d**2 - x**2)**0.5)
        answer += (res // k) + 1        
        
    return answer