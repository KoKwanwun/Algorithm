# heap으로 푼 코드
# heap : 큰 이진트리 구조
# heapush : heap에 아이템 추가
# heappop : heap에 가장 작은 원소 제거
# heapify : heap으로 재정의
# heap.remove(max(heap)) : 가장 큰 값 제거
import heapq

def solution(operations):
    heap = []

    for operation in operations:
        command, num = operation.split(' ')
        num = int(num)

        if command == 'I':
            heapq.heappush(heap, num)
        elif heap:
            if num < 0:
                heapq.heappop(heap)
                heapq.heapify(heap)
            else:
                heap.remove(max(heap))
                heapq.heapify(heap)

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]

# deque로 풀기
from collections import deque
import copy

# deque의 원소 중에 크기에 맞게 값 넣기
def dqSort(dq, targetNum):
    copyDq = copy.deepcopy(dq)
    idx = 0
    
    while copyDq:
        num = copyDq.popleft()
        
        if targetNum < num:
            dq.insert(idx, targetNum)
            return 0
        else:
            idx += 1
    
    dq.insert(idx, targetNum)
    return 0

def solution(operations):
    dq = deque()
    
    for operation in operations:
        command, num = list(operation.split())
        num = int(num)
        if command == "I":
            if len(dq) == 0:        # 비어 있다면 그냥 넣기
                dq.append(num)
            else:                   # 그 외는 위치에 맞게 값 넣기
                dqSort(dq, num)
        elif len(dq) > 0:
            if num == 1:            # 1이면 최대값 제거
                dq.pop()
            else:                   # -1이면 최소값 제거
                dq.popleft()
    
    # []라면 [0, 0] 리턴, 그 외는 [최대값, 최소값]
    return [dq[-1], dq[0]] if len(dq) > 0 else [0, 0] 