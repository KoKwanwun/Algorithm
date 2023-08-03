def solution(s):
    answer = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            answer += 1
        elif s[i] == ')':
            answer -= 1
        
        # answer가 0미만이 되면 올바르지 않은 괄호
        # 마지막에 answer가 0이 아니면 올바르지 않은 괄호
        if answer < 0 or (i == len(s)-1 and answer != 0):
            return False

    return True