# 미리 설치되어 있는 stations를 이용
# 전파가 전달되지 않는 연속된 아파트 구간을 찾아 (w * 2 + 1)를 나눈 후 올림해주면 그 구간에 설치되어야 하는 개수가 나옴
"""
예시
N : 16, stations : [9], W : 2로 현재 7~11에 전파가 전달됨
1 2 3 4 5 6 * * * * * 12 13 14 15 16
- 1~6까지의 아파트는 6개에 5(w * 2 + 1)로 나눈 후 올림하면 2개를 설치
- 12~16까지의 아파트는 5개 5로 나눈 후 올림하면 1개를 설치
- 각 구간에 설치해야하는 기지국 개수를 구할 수 있음
"""
import math

def solution(n, stations, w):
    answer = 0
    for i in range(len(stations)):
        if i == 0:
            answer += math.ceil(((stations[i] - w) - 1) / (w * 2 + 1))
        if i == len(stations) - 1:
            answer += math.ceil((n - (stations[i] + w)) / (w * 2 + 1))
            break
        answer += math.ceil(((stations[i + 1] - w) - (stations[i] + w + 1)) / (w * 2 + 1))
        
    return answer