# 진출 지점으로 오름차순 정렬하는 것이 포인트
# for문을 돌리며 겹치지 않는 곳의 진출 지점에 계속 설치
def solution(routes):
    answer = 0
    camera = -30001
    
    # 진출 지점으로 오름차순
    for route in sorted(routes, key = lambda x : x[1]):
        if route[0] > camera:   # 진입지점이 현재 카메라 설치 지점보다 크면
            camera = route[1]   # 카메라를 진출지점에 다시 설치
            answer += 1
    
    return answer