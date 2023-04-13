n = int(input())
stack = []

# 0이면 pop, 그 외는 값 추가
for _ in range(n):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))