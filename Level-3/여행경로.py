from collections import deque

results = []

def dfs(ticket, tickets, ticketCheck, result):
    for i in range(len(tickets)):
        # 첫번째 방문이고 출발지가 ticket과 같다면
        if(ticketCheck[i] == 0 and tickets[i][0] == ticket):
            # 여러 경로를 찾기 위해 ticketCheck과 result를 복사
            ticketCheckCopy = ticketCheck[:]
            resultCopy = result[:]

            # 방문 처리 및 도착치 result에 넣기
            ticketCheckCopy[i] = 1
            resultCopy.append(tickets[i][1])

            # 최종 경로가 만들어졌다면 모든 경로를 담을 수 있는 results 리스트에 넣기, 아니라면 dfs에 다시 넣기
            if(len(tickets) == sum(ticketCheckCopy)):
                results.append(resultCopy)
            else:
                dfs(tickets[i][1], tickets, ticketCheckCopy, resultCopy)


def solution(tickets):
    # 각 ticket마다 방문처리하는 리스트 생성
    ticketCheck = [0] * len(tickets)

    # tickets를 정렬하여 경로가 여러개일 경우, 알파벳 순서가 되도록
    tickets.sort(key=lambda x: (x[0], x[1]))
    result = ["ICN"]

    # dfs 활용
    dfs("ICN", tickets, ticketCheck, result)

    return results[0]