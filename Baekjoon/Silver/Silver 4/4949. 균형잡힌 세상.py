import sys

while True:
    strs = sys.stdin.readline().rstrip()
    if strs == ".":
        break

    stack = []

    for str in strs:
        if str == "(" or str == "[":
            stack.append(str)
        elif str == ")":
            if stack != [] and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
        elif str == "]":
            if stack != [] and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break
    else:
        if stack == []:
            print("yes")
        else:
            print("no")