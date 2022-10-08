# n은 10,000이하의 수이기 때문에 리스트 크기를 10,000으로 미리 생성
def solution(n):
    mlist = ["수", "박"] * 5000
    return ''.join(mlist[0:n])