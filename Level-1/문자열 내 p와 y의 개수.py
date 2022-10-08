# lower 소문자로 변환
# count 해당 문자의 개수 리턴
def solution(s):
    s = s.lower()
    p = s.count('p')
    y = s.count('y')
    
    if p == y:
        return True
    else:
        return False