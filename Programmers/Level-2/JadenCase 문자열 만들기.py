# 첫글자는 무조건 대문자
# 전 문자가 공백이면 대문자로, 나머지는 소문자로
def solution(s):
    s = list(s)
    if ord(s[0]) >= 97 and ord(s[0]) <=122:
        s[0] = chr(ord(s[0]) - 32)
    for i in range(1,len(s)):
        if s[i-1] == ' ' and ord(s[i]) >= 97 and ord(s[i]) <= 122:
            s[i] = chr(ord(s[i]) - 32)
        elif s[i-1] != ' ' and ord(s[i]) >= 65 and ord(s[i]) <= 90:
            s[i] = chr(ord(s[i]) + 32)
    return ''.join(s)