# 정수를 문자형으로 바꾼 후 각 자리수 더하기
def solution(n):
    return sum(list(map(int,str(n))))