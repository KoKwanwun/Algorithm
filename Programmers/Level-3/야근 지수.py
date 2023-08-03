# heapq : heappop을 하면 최소값을 리턴 (때문에 최대힙을 하려면 -를 한 후 작업해야 함)
# heapq.heapify(h) : 재정렬
import heapq

def solution(n, works):
    # 아래 경우는 무조건 0이 나옴
    if n >= sum(works):
        return 0
    
    # 최대힙으로 만들기
    h = []
    for works in works:
        heapq.heappush(h, -works)
        
    # 최소값에 +1 해준 후 다시 넣기 (즉, 최대값에 -1 해준 것과 동일)
    while n:
        heapq.heappush(h, heapq.heappop(h) + 1)
        n -= 1
    
    return sum([each * each for each in h])