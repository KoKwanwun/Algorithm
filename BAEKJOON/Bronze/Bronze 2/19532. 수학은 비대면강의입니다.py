a, b, c, d, e, f = map(int, input().split())

# 공식 계산
y = ((a * f) - (c * d)) // ((-b * d) - (a * -e))
x = (f - (e * y)) // d

print(x, y)