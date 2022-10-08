# 길이가 긴 곳을 계속 비교하기 위해 대소비교
# 긴 곳은 긴 곳끼리 비교
def solution(sizes):
    x = 0
    y = 0
    for data in sizes:
        if data[0] > data[1]:
            x = max(x, data[0])
            y = max(y, data[1])
        else:
            x = max(x, data[1])
            y = max(y, data[0])
        
    return x*y