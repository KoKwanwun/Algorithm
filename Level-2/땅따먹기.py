# DP 이용
# 이전 행의 자신의 인덱스를 제외한 3개 중 max값을 현재 인덱스에 누적해감
"""
예시
1   2   3   5
10  11  12  11
16  15  13  13
"""
def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])  # j(자신의 인덱스)를 제외한 나머지 중 max값을 현재 값에 누적

    return max(land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))