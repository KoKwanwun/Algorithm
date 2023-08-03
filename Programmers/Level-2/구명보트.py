from collections import deque

def solution(people, limit):
    answer = 0

    # 오름차순 정렬
    people.sort()
    dq = deque(people)

    # dq 안의 원소가 없어질때까지
    while dq:
        # dq의 크기가 1이라면 구명보트 개수를 +1 해주고 탈출
        if(len(dq) == 1):
            answer += 1
            break
        
        # 가장 큰 값, 가장 작은 값을 빼서 비교 후
        # 합이 limit보다 크다면, 작은 값을 다시 넣기
        maxNum = dq.pop()
        minNum = dq.popleft()

        if(maxNum + minNum > limit):
            dq.appendleft(minNum)

        answer += 1

    return answer