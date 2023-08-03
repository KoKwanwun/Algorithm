n = int(input())
nums = list(map(int, input().split()))
visited = [0] * n
mlist = []

maximum = -1e9

def back():
    global maximum
    # 길이와 n이 동일하면 주어진 식에 따라 max값 갱신
    if len(mlist) == n:
        tmp = 0
        for i in range(len(mlist)-1):
            tmp += abs(mlist[i] - mlist[i+1])

        maximum = max(maximum, tmp)
        return
    
    # visited를 활용하여 순서를 바꾼 모든 경우의 수 백트래킹
    for i in range(len(nums)):
        if not visited[i]:
            mlist.append(nums[i])
            visited[i] += 1
            back()
            visited[i] -= 1
            mlist.pop()

back()
print(maximum)