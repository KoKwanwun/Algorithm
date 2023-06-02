# input, list를 사용했을 때 시간초과
# -> sys.stdin.readline, set으로 해결
import sys

mset = set()
result = 0

for _ in range(int(sys.stdin.readline())):
    tmp = sys.stdin.readline().rstrip()

    if tmp == "ENTER":
        mset = set()
        continue

    if tmp not in mset:
        mset.add(tmp)
        result += 1

print(result)