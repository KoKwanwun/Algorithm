# 스택 활용
def solution(s):
    answer = 0

    for _ in range(len(s)):
        s = s[1:] + s[0]        # 한칸 회전
        stack = []

        for each in s:
            if len(stack) == 0:     # stack 비어있다면 넣기
                stack.append(each)
            else:                   # 짝이 맞다면 pop, 그 외는 append
                if each == ")" and stack[-1] == "(": stack.pop()
                elif each == "]" and stack[-1] == "[": stack.pop()
                elif each == "}" and stack[-1] == "{": stack.pop()
                else:   stack.append(each)

        if len(stack) == 0:         # 올바른 괄호 문자라면 answer + 1
            answer += 1

    return answer