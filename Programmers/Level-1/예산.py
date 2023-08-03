# 1. 정렬
# 2. budget에서 차례대로 빼줌
# 3. 음수가 된다면, 해당 물품을 지원하지 못하므로 result-1 리턴
# 4. for문을 다 돌았다면, 모든 물품 지원 가능 -> result 리턴
def solution(d, budget):
    d = sorted(d)
    result = 0
    
    for i in range(len(d)):
        budget -= d[i]
        result += 1
        if(budget < 0):
            return result-1
        
    return result