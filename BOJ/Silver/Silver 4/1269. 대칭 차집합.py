n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

# 교집합 개수 구하기
inter = a & b

print(len(a) + len(b) - (len(inter) * 2))