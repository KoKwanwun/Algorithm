n = int(input())
# 인덱스 위치를 저장하기 위해 enumerate 사용하여 정렬
nums = sorted(enumerate(list(map(int, input().split()))), key=lambda x : x[1])
result = [0 for _ in range(n)]

rank = 0

result[nums[0][0]] = rank

# 이전 값과 같다면 rank는 그대로, 그 외에는 rank+1
for i in range(1, len(nums)):
    if nums[i-1][1] != nums[i][1]:
        rank += 1

    result[nums[i][0]] = rank

print(*result)