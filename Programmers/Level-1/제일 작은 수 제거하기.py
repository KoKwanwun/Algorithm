# min 최소값
# remove 리스트에서 값 제거
# 리스트 원소가 없으면 [-1] 리턴
def solution(arr):
    arr.remove(min(arr))
    return [-1] if arr == [] else arr