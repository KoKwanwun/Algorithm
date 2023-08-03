def solution(number, k):
    stack = []

    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)   # k는 number의 자릿수 미만이기 때문에 최소 stack의 자릿수는 1

    for _ in range(k):
        stack.pop()

    return ''.join(stack)