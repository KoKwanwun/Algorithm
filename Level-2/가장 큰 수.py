def solution(numbers):
    numbers = list(map(str, numbers))               # 문자열로 변환
    numbers.sort(key=lambda x: x*3, reverse=True)   # 리스트를 3배하여 내림차순(범위가 0 ~ 1000이기 때문에 3배)
    return str(int(''.join(numbers)))               # 이어 붙이기