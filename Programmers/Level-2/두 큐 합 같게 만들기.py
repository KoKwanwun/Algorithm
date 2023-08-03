from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    q1s = sum(queue1)
    q2s = sum(queue2)
    
    # 합이 홀수라면 실패
    if (q1s + q2s) % 2 == 1:
        return -1
    
    # limit을 주어 일정 횟수 while을 돌면 탈출
    limit = len(queue1) + len(queue2)
    
    while q1s != q2s:
        if answer >= limit:
            return -1

        # queue1이 존재하고 합이 더 크다면 queue2에 값 넣기
        while queue1 and q1s > q2s:
            tmp = queue1.popleft()
            queue2.append(tmp)
            answer += 1
            q1s -= tmp
            q2s += tmp

        # queue2가 존재하고 합이 더 크다면 queue1에 값 넣기
        while queue2 and q2s > q1s:
            tmp = queue2.popleft()
            queue1.append(tmp)
            answer += 1
            q1s += tmp
            q2s -= tmp
    
    return answer