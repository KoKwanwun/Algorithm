def solution(food):
    answer = ''
    
    # food[i]의 몫만큼 한쪽을 완성한 후, return 값 형태로 만들기
    for i in range(1, len(food)):
        for _ in range(food[i] // 2):
            answer += str(i)
    
    return answer + '0' + answer[::-1]