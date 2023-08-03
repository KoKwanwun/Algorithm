import sys
from collections import Counter

mlist = []

for _ in range(int(sys.stdin.readline())):
    mlist.append(int(sys.stdin.readline()))

mlist.sort()
# 2개를 출력
cnt = Counter(mlist).most_common(2)

print(round(sum(mlist) / len(mlist)))
print(mlist[len(mlist)//2])
# 길이가 1이라면 그 값을 출력
# 최빈값이 여러개라면 두번째로 작은 값을 출력
if len(mlist) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(mlist[0])
print(max(mlist) - min(mlist))