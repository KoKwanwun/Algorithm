# 이 문제는 원소를 2배를 하여 구했지만 시간이 오래 걸림
# 해결 방안 : %를 이용하여 element의 합을 구하면 시간 절약 가능 ()
"""
for i in range(ll):
    ssum = elements[i]
    res.add(ssum)
    for j in range(i+1, i+ll):
        ssum += elements[j%ll]
        res.add(ssum)
"""
def solution(elements):
    n = len(elements)
    elements = elements + elements          # 2배로 하여 원형 수열 생성
    mSet = set()

    for i in range(1, n + 1):               # 길이만큼 for문을 돌려 합 경우의 수 set에 넣기
        for j in range(n):
            mSet.add(sum(elements[j:j+i]))

    return len(mSet)

print(solution([7,9,1,1,4]))