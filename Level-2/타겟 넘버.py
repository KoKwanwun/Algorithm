result = 0

def dfs(numbers, target, idx, num):
    # 전역 변수로 변환
    global result

    if (len(numbers) == idx):
        if (num == target):
            result += 1
    else:
        # 재귀로 +, -한 것을 넣어주기
        dfs(numbers, target, idx+1, num+numbers[idx])
        dfs(numbers, target, idx+1, num-numbers[idx])

def solution(numbers, target):
    # 전역 변수로 변환
    global result

    dfs(numbers, target, 0, 0)

    return result