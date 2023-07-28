from collections import Counter
import math

n, d = map(int, input().split())
mlist = list(map(int, input().split()))
result = 0

for key, value in Counter(mlist).items():
    # 단순하게 몫만 구하면 안됨 -> 선조를 추가한 후에도 d를 초과할 수 있기 때문
    while value > d:
        # 우선 몫(추가된 선조)를 결과값에 추가
        tmp = value // d
        result += tmp
        # value = 추가된 선조 + 나머지 선조
        # 선조가 5, d가 2라면 2 2 1로 나눠지고 선조가 2명 추가됨. 이후 3명 선조를 다시 while을 거쳐야 함
        value = math.ceil(value / d)

print(result)