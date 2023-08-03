# 홀수면 가운데, 짝수면 가운데 두글자
def solution(s):
    return s[len(s) // 2] if len(s) % 2 == 1 else s[len(s) // 2 - 1 : len(s) // 2 + 1]