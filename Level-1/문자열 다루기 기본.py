# iddigit : 숫자인지 판별해주는 함수
def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()