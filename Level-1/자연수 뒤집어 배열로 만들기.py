# [::-1] 리스트 뒤집기
def solution(n):
    answer = list(map(int, str(n)))
    return answer[::-1]