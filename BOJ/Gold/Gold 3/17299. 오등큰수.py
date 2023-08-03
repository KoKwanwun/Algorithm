# '오른쪽에 있으면서'라는 말을 보고 오른쪽부터 시작하는 것이 아닌
# 스택을 활용하여 할 수도 있음
from collections import Counter

n = int(input())
data = list(map(int, input().split()))
count = Counter(data)                   # 각 숫자 개수 구하기
stack = [0]                             # 시작 인덱스 넣기
result = [-1] * n                       # -1로 초기값 설정

for i in range(n):
    # stack이 존재하며, stack의 최상위 데이터의 개수가 i번째 데이터의 개수보다 작다면
    # result의 인덱스 값을 data의 인덱스 i값으로 바꾸기
    while stack and count[data[stack[-1]]] < count[data[i]]:
        result[stack.pop()] = data[i]
    stack.append(i)

for r in result:
    print(r, end=' ')