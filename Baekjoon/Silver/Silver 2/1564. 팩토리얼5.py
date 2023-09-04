n = int(input())
result = 1

# rstrip으로 정수 오른쪽의 0을 모두 지움
# 정수 최대값의 자릿수인 12개만큼 가져와서 계산 (숫자가 너무 커지면 계산 불가하기 때문)
for i in range(1, n+1):
    result *= i
    result = int(str(result).rstrip("0")[-12:])
    
print(str(result)[-5:])