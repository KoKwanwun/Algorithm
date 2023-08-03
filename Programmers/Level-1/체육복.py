def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    # 도난당한 학생 중 여벌 옷이 있는 학생은 양쪽 제거
    for i in lost[:]:
        if i in reserve[:]:
            lost.remove(i)
            reserve.remove(i)
    
    # 양쪽 반 중 빌려주기
    for i in reserve[:]:
        if i - 1 in lost[:]:
            lost.remove(i-1)
        elif i + 1 in lost[:]:
            lost.remove(i+1)
    
    # 체육 수업 들을 수 있는 최댓값을 출력
    answer = n - len(lost)

    return answer