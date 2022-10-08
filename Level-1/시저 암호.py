# 아스키 코드를 활용한 문제 해결
def solution(s, n):
    c = []
    for i in range(len(s)):
        if s[i] == ' ':
            c.append(s[i])
        elif ord(s[i]) >= 65 and ord(s[i]) <= 90:
            if ord(s[i]) + n > 90:
                c.append(chr(ord(s[i]) + n - 26))
            else:
                c.append(chr(ord(s[i]) + n))
        elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
            if ord(s[i]) + n > 122:
                c.append(chr(ord(s[i]) + n - 26))
            else:
                c.append(chr(ord(s[i]) + n))
    return ''.join(c)