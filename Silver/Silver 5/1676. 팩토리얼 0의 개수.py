import math

# 뒤에서부터 찾아야하므로 반전시켜주기
fac = str(math.factorial(int(input())))[::-1]
result = 0

# 0일 경우 result + 1, 그 외는 탈출
for i in range(len(fac)):
    if(fac[i] == '0'):
        result += 1
    else:
        break
    
print(result)