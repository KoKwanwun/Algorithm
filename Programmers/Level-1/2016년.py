# 미리 리스트를 만들어놓은 것이 포인트
def solution(a, b):
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    date = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    tmp = (sum(month[1:a]) + b) % 7
    return date[tmp]