def solution(n, s):
    answer = []
    if s < n:               # 존재하지 않음
        return [-1]
    
    num = s // n            # 값 개수만큼 나누어 중심이 되는 값
    for _ in range(n):
        answer.append(num)
        
    for i in range(s % n):  # 나머지만큼 원소에 1을 더하여 곱했을 때 최대값 만들기
        answer[i] += 1
            
    return sorted(answer)   # 오름차순