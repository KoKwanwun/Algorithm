import collections

# collections 함수를 활용하여 해결
# 각 원소의 개수를 Counter 형식으로 리턴
# [0] : 문자열로 변환시키기 위해
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer)[0]