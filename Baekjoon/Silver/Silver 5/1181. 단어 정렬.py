import sys

input = sys.stdin.readline
mset = set()

for _ in range(int(input())):
    mset.add(input().rstrip())

# 길이 짧은 순, 같다면 사전순
for each in sorted(mset, key=lambda x : (len(x), x)):
    print(each)