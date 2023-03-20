# 다른 사람 풀이 참고
# [(i,p) for i,p in enumerate(priorities)] : 초기 위치 쌍 설정
# any(cur[1] < q[1] for q in queue) : 하나라도 참이면 True
# 나의 풀이는 계산하면서 location 변경
def solution(priorities, location):
    result = 0
    stack = []

    while priorities:
        stack.append(priorities.pop(0))
        location -= 1                               # 위치 변경

        for priority in priorities:                 # 하나라도 작은 값이 있다면
            if(stack[0] < priority):
                priorities.append(stack.pop(0))
                if location < 0:                    # 위치 변경
                    location = len(priorities) - 1
                break
        else:                                       # 모두 통과할 때
            stack.pop(0)
            result += 1

            if location < 0:                        # 위치 변경
                return result