def solution(s):
    # stack 사용
    stack = []

    # 같으면 제거, 아니면 stack에 쌓기
    for each in s:
        if(len(stack) == 0):
            stack.append(each)
            continue
        else:
            if(stack[-1] == each):
                stack.pop()
            else:
                stack.append(each)

    # 남아있는것이 없다면 1, 있다면 0 리턴
    if(len(stack) == 0):
        return 1
    else:
        return 0