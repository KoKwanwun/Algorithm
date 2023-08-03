# G3 : 17299번과 같은 유형
# stack 활용
n = int(input())
mlist = list(map(int, input().split()))

stack = [0]
result = [-1] * n

for i in range(n):
    # stack의 최상위 인덱스에 해당하는 값이 현재값보다 작다면
    # result 값 갱신
    while stack and mlist[stack[-1]] < mlist[i]:
        result[stack.pop()] = mlist[i]
    stack.append(i)

for r in result:
    print(r, end = " ")