import sys
import math

a, p = map(int, sys.stdin.readline().split())
nums = [a]

while True:
    # 수열 계산
    tmp = 0
    for i in list(map(int, str(nums[-1]))):
        tmp += pow(i, p)

    # 반복수가 나오면 개수 리턴, 그 외는 수열 추가
    if(tmp in nums):
        print(len(nums[:nums.index(tmp)]))
        break
    else:
        nums.append(tmp)