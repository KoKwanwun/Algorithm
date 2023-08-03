# 힙 큐 활용
import heapq, sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

# 최소값 2개를 꺼낸 후 더한 값을 다시 heap에 넣어 최소힙 유지
result = 0
while len(heap) > 1:
    tmp = heapq.heappop(heap) + heapq.heappop(heap)
    result += tmp
    heapq.heappush(heap, tmp)

print(result)