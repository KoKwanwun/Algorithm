# 홀수 짝수를 이용하여 대소문자 설정
def solution(s):
    s = list(s.split(' '))
    c = []
    for data in s:
        data = list(data)
        for i in range(len(data)):
            if i % 2 == 0:
                data[i] = data[i].upper()
            else:
                data[i] = data[i].lower()
        c.append(''.join(data))
    return ' '.join(c)