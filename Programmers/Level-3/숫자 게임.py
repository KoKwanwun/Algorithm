def solution(A, B):
    answer = 0

    # A, B 정렬
    A.sort()
    B.sort()
    checkIdx = 0
    
    for i in range(len(A)):
        for j in range(checkIdx, len(B)):
            # A보다 B가 더 크다면 점수 올리기
            if A[i] < B[j]:
                answer += 1
                checkIdx += 1
                break
            
            checkIdx += 1
        # j를 모두 돌아도 못찾았다면 더이상 B가 이길 수 있는 경우의 수가 없음
        else:
            break

    return answer