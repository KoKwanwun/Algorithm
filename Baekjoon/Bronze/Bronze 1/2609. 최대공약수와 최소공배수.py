x, y = map(int, input().split())

# 유클리드 호제법 사용
if (x > y):
    maxVal = x
    minVal = y
else:
    maxVal = y
    minVal = x

while(True):
    tmp = maxVal % minVal
    maxVal = minVal
    minVal = tmp

    if(minVal == 0):
        break

# GCD 최대공약수, LCM 최소공배수
GCD = maxVal
LCM = maxVal * (x // maxVal) * (y // maxVal)

print(GCD, LCM)