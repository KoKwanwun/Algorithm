# 나머지 분배 법칙
# (AxB) % C = ((A%C)*(B%C)) % C
a, b, c = map(int, input().split())

def back(a, n, c):
    if n == 1:
        return a % c
    else:
      tmp = back(a, n//2, c)
      if n % 2 == 0:
          return (tmp * tmp) % c
      else:
          return (tmp * tmp * a) % c
    
print(back(a, b, c))