def solution(n):
    answer = 0

    # 나누어 떨어지는 수(약수)만 덧셈
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
    return answer