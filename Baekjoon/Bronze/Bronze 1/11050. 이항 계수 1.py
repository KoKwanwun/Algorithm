# 팩토리얼
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
    
n, k = map(int, input().split())

# 이항계수 공식
print(factorial(n) // (factorial(k) * factorial(n-k)))