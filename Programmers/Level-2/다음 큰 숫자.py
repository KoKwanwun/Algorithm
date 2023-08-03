def solution(n):
    # n을 2진수로 바꾼 수의 1의 개수
    n_count = bin(n).count('1')
    
    # n을 1씩 증가시키면서 기존 n(2진수)과 1의 개수가 같아지면 리턴
    while True:
        n += 1
        tmp = bin(n).count('1')
        if n_count == tmp:
            return n