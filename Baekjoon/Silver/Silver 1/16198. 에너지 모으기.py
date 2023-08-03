n = int(input())
nums = list(map(int, input().split()))

maxVal = -1

def back(energy):
    global maxVal

    # 첫번째, 마지막은 제거하지 못하므로 정지 조건
    if len(nums) == 2:
        maxVal = max(maxVal, energy)
        return
    
    for i in range(1, len(nums)-1):
        target = nums[i-1] * nums[i+1]

        # pop, insert를 하며 백트래킹
        tmp = nums.pop(i)
        back(energy + target)
        nums.insert(i, tmp)
    
back(0)
print(maxVal)