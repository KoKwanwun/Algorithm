# sorted 정렬 함수(reverse=True : 내림차순)
# ''.join() : 공백없이 문자 붙이기
def solution(n):
    n = sorted(list(map(int, str(n))), reverse=True)
    return int(''.join(map(str,n)))