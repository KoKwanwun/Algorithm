# 입력값 받기
a, b = map(int, input().split())
n = int(input())
aList = list(map(int, input().split()))

# a진수 -> 10진수
aList = aList[::-1]
aVal = 0
for i in range(n):
    aVal += pow(a, i) * aList[i]

# 10진수 -> b진수
bList = []
while aVal:
    bList.append(str(aVal % b))
    aVal //= b

print(' '.join(bList[::-1]))