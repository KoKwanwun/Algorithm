# set : 중복값 제거
# min 사용 이유 : unique한 값의 개수가 N/2를 넘어가는 값일 수 있기 때문
def solution(nums):
    tmp = len(set(nums))
    
    return min(len(nums)/2, tmp)