def solution(order):
    answer = 0
    
    # pop을 사용하기 위해 내림차순
    boxs = list(range(max(order), 0, -1))
    stack = []
    
    for each in order:
        # stack의 최상위 원소와 같다면
        # 이 if문이 while문 아래에 있다면 오류가 발생할 수 있음
        if stack != [] and stack[-1] == each:
            answer += 1
            stack.pop()
            continue
        
        # order의 현재 원소가 boxs의 원소보다 크다면 stack에 계속 쌓기
        while boxs != [] and boxs[-1] < each:
            stack.append(boxs.pop())
            
        # boxs의 원소와 같다면
        if boxs != [] and boxs[-1] == each:
            answer += 1
            boxs.pop()
            continue
            
        # 그 외는 break
        break
                
    return answer