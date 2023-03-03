# -2진수는 2진수와 똑같이 -2로 나눠주면 되는데, 나머지가 0 or 1이어야 함
n = int(input())
originN = n
result = ""

while n:
    # 나머지가 -1이 나오면 안되므로 따로 처리
    if(n % -2 == -1):
        result += str(1)
        n = (n // -2) + 1
    else:
        result += str(n % -2)
        n = n // -2

# 0을 입력받았을 때는 따로 처리
if(originN == 0):
    print(0)
else:
    print(result[::-1])