x, y = map(int, input().split())

while(x % y != 0):
    x, y = y, x % y

# 최대공약수만큼 1의 개수 생성
print('1' * y)