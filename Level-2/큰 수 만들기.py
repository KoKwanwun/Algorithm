def solution(number, k):
    stack = []

    for num in number:
        if(len(number) == 0):
            stack.append(num)
            continue
        if(k > 0 and stack[-1] < num):
            stack.pop()
            k -= 1
            if(k <= 0):
                break
        stack.append(num)

    for _ in range(k):
        stack.pop()

    return ''.join(stack)