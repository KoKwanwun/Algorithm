# 주어지는 수 5개로 고정
mlist = []

for _ in range(5):
    mlist.append(int(input()))

# 평균
print(sum(mlist) // 5)
# 중앙값
print(sorted(mlist)[2])