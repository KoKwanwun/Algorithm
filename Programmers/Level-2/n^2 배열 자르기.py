# 참고해서 푼 문제
# 인덱스의 몫과 나머지 중 큰 값이 1차원 배열 값이 됨
# 인덱스는 0부터 시작이므로 +1을 해서 넣어줘야 함

def solution(n, left, right):
    result = []

    for i in range(left, right + 1):
        quotient = i // n   # 몫
        remainder = i % n   # 나머지
        result.append(max(quotient, remainder) + 1)

    return result