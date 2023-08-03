# 힙
# heapq.heapify(리스트) : 리스트를 리스트힙으로
# heapq.heappop(리스트) : 가장 작은 원소 뽑기
# heapq.heappush(리스트, 값) : 리스트에 값 넣기
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    # scoville의 첫 값이 K보다 작거나 길이가 1이 아닐 경우(1이면 v를 구할 수 없음)
    while scoville[0] < K and len(scoville) != 1:
        v = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, v)
        cnt += 1

    # 최소 횟수는 cnt, 해결하지 못했다면 -1
    return -1 if scoville[0] < K else cnt