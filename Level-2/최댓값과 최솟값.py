# min max로 최대 최소 구하여 문자열로 리턴
def solution(s):
    mlist = list(map(int,s.split(' ')))
    return str(min(mlist)) + ' ' + str(max(mlist))