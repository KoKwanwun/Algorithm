def solution(a, b, n):
    answer = 0
    
    while n >= a:
        # 빈병으로 바꿔먹은 콜라 개수 더하기
        answer += n // a * b
        # 빈병 나머지와 콜라를 먹고 나온 빈병의 합으로 n 갱신
        n = (n % a) + (n // a * b)
        
    return answer