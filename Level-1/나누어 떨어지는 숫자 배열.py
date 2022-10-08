# 나누어 떨어지는 수만 리스트 저장
def solution(arr, divisor):
    answer = [ i for i in arr if i % divisor == 0 ]
    return  [-1] if len(answer) == 0 else sorted(answer)