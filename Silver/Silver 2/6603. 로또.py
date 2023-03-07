from itertools import combinations

while True:
    nums = list(map(int, input().split()))

    # 첫번째 값이 0이라면 종료
    if(nums[0] == 0):
        break
    else:
        n = nums[0]
        nums.pop(0)         # k개를 의미하는 인덱스 0의 값 제거

        # 조합 사용
        result = list(combinations(nums, 6))
        for each in result:
            print("%d %d %d %d %d %d" %(each[0], each[1], each[2], each[3], each[4], each[5]))
        print()             # 테스트 케이스 사이에는 빈 줄 하나 출력