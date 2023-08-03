# 내적 : 각 인덱스 값을 곱하여 모든 원소의 합(a[0]*b[0] + a[1]*b[1])
def solution(a, b):
    return sum(list(map(lambda x,y: x * y, a, b)))