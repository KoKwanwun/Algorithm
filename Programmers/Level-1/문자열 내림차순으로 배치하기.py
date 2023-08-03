# 대문자는 소문자보다 작은것으로 간주
# ord : 문자를 아스키코드(정수)로 리턴
# chr : 정수를 해당 문자로 리턴
def solution(s):
    mlist = []
    for i in s:
        mlist.append(ord(i))
    mlist = sorted(mlist, reverse=True)
    answer = []
    for i in mlist:
        answer.append(chr(i))
    return ''.join(answer)