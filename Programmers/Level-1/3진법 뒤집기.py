# 3진법 구하는 방법으로 구한 후 뒤집지 않고 10진수로 출력
# int() 두번째 매개변수가 있을때 해당하는 진수에서 10진수로 변환
def solution(n):
    mlist = ''
    while n:
        mlist += str(n % 3)
        n = n//3
    return int(mlist, 3)