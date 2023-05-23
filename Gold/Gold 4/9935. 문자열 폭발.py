mStr = input()
bustStr = input()
bustLen = len(bustStr)
stack = []

# 차례대로 문자열을 stack에 넣기
# stack이 비어있지 않고, stack의 최상위 폭발문자열 개수만큼 꺼낸 문자열이 폭발문자열과 같다면
# 폭발문자열 개수만큼 pop
# while로 위의 두단계 반복
for s in mStr:
    stack.append(s)
    while stack and ''.join(stack[-bustLen:]) == bustStr:
        for _ in range(bustLen):
            stack.pop()

if stack == []:
    print("FRULA")
else:
    print(''.join(stack))