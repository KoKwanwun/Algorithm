import sys

# 처음 무지개 댄스를 추는 ChongChong을 set에 넣기
mset = set()
mset.add("ChongChong")

for _ in range(int(sys.stdin.readline())):
    a, b = sys.stdin.readline().split()

    if a in mset or b in mset:
        mset.add(a)
        mset.add(b)

print(len(mset))