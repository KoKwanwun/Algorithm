import sys

n = int(sys.stdin.readline())
stack = []
result = []
tmp = 1

for i in range(n):
    num = int(sys.stdin.readline())
    # tmp부터 입력받은 수까지 stack에 넣기
    while tmp <= num:
        stack.append(tmp)
        result.append('+')
        tmp += 1

    # stack 맨 위의 숫자와 입력받은 숫자와 같다면 pop
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        break
# 모두 진행됐다면 result 출력
else:
    for i in result:
        print(i)