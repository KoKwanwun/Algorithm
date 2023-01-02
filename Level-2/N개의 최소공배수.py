# 유클리드 호제법을 활용한 최소공배수 구하기
# a * b = gcd * lcm
def lcm(a, b):
    multiNum = a * b
    maxNum = max(a, b)
    minNum = min(a, b)

    while True:
        if(maxNum % minNum == 0):
            return multiNum // minNum
        else:
            remainNum = maxNum % minNum
            maxNum = minNum
            minNum = remainNum

def solution(arr):
    
    # 2개를 각각 비교하며 최소공배수 구하기
    while len(arr) >= 2:
        a = arr.pop()
        b = arr.pop()
        arr.append(lcm(a, b))
    
    return arr[0]