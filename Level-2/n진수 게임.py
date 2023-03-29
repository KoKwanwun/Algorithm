# 10진수 -> n진수
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    # t * m + p개 이상의 숫자가 되도록 n진수 리스트 구하기
    nums = '0'
    num = 1
    while True:
        nums += convert(num, n)
        num += 1
        
        if len(nums) > (t * m + p):
            break
            
    # p - 1 : 인덱스로 인해 -1
    # m 간격으로 t개 숫자만큼 구하기
    idx = p - 1
    answer = ''
    while True:
        answer += nums[idx]
        idx += m
        
        if len(answer) == t:
            break
    
    return answer