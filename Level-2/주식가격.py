# 참고해서 푼 문제

# 이중 for문
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

# stack 사용
def solution(prices):
    length = len(prices)
    answer = [ i for i in range (length - 1, -1, -1)]   # answer을 max값으로 초기화
    
    stack = [0]
    for i in range (1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer