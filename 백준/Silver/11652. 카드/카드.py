import collections

n = int(input())
mlist = []

for _ in range(n):
    num = int(input())
    mlist.append(num)
    
# 정렬을 해야 최빈값이 여러개 일 때 작은값을 리턴
mlist = sorted(mlist)

# collections 라이브러리의 most_common() : 리스트 중 최빈값 리턴
print(collections.Counter(mlist).most_common()[0][0])