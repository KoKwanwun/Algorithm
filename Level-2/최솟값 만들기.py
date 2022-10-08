# 한쪽은 오름차순, 다른쪽은 내림차순으로 곱하여 더하면 최소가 됨
def solution(A,B):
    A = sorted(A)
    B = sorted(B, reverse = True)
    answer = 0
    
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer