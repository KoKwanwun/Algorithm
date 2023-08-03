n, m = map(int, input().split())

# 직접 팩토리얼을 구하려면, n과 m의 최대값인 2000000000라면 범위를 초과
# 다른 방법을 생각 -> 끝자리 0이 생기려면 10의 배수 (2, 5 배수를 포함하는 개수 중 최소값)
def num_count(n, k):
    num = 0
    while n != 0:
        n //= k
        num += n
    return num

# 분자는 +, 분모는 -로 구함
print(min(num_count(n, 2) - num_count(n-m, 2) - num_count(m, 2), num_count(n, 5) - num_count(n-m, 5) - num_count(m, 5)))