# dict의 key값을 문자열로 해야하는 이유
# 01234567을 1234567로 저장하기 때문에 결과값이 다르게 출력
import sys
input = sys.stdin.readline

k, l = map(int, input().split())
mdict = dict()

# dictionary로 입력 받는 값의 순서를 갱신 (먼저 들어온 것은 자동 삭제)
for i in range(l):
    mdict[input().rstrip()] = i
    
# 중복제거된 dictionary를 들어온 순서대로 정렬 
result = sorted(mdict.items(), key = lambda x : x[1])

# 반례 : result의 개수가 k보다 작을 경우
if k > len(result):
    k = len(result)
    
for i in range(k):
    print(result[i][0])