def solution(a, b):
    answer = 0
    
    # 최대 최소 정하기
    if a <= b:
        x = a
        y = b + 1
    else:
        x = b
        y = a + 1

    for i in range(x, y):
        answer += i
    
    return answer