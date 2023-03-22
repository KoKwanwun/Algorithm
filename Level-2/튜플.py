from collections import Counter

def solution(s):
    result = []
    
    # {, } 제거
    new = s.replace("{", "").replace("}", "")

    """
    # Counter(new.split(',')).most_common()
    1. ,로 구분하여 리스트 생성
    2. Counter 라이브러리로 각 원소 개수 구하기
    3. most_common() 함수로 개수가 많은 원소로 정렬하여 key, 개수의 튜플 형태로 리스트 생성
       ex) [(1, 3), (2, 2)]
    4. key값을 int로 변환하여 결과 리스트에 append
    """
    for element in Counter(new.split(',')).most_common():
        result.append(int(element[0]))
    
    return result