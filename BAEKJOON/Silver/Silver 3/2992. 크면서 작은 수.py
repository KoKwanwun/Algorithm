from itertools import permutations

x = int(input())
nums = list(permutations(list(str(x))))

# 구성이 같은 경우의 수 중 가장 작은 수 찾기
result = 999999
for each in nums:
    num = int(''.join(each))
    
    if num > x:
        result = min(result, num)

# 999999라면 그러한 숫자가 없는 경우 -> 0 출력
if result == 999999:
    print(0)
else:
    print(result)