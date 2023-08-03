# 주어진 n부터 계산하기
def solution(n):
    result = 0
    
    while n > 0:
        if n % 2 == 0:      # 짝수라면, 2로 나누기
            n //= 2
        else:               # 홀수라면, n에 -1 해주고 건전지 사용량 +1
            result += 1
            n -= 1
            
    return result