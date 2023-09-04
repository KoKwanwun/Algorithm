x = int(input())
result = 0

# 64이하의 2의 제곱수들을 빼며 개수 구하기
for num in [64, 32, 16, 8, 4, 2, 1]:
    while x >= num:
        x -= num
        result += 1
        
print(result)