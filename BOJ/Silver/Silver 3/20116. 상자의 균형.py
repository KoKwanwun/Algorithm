# 위에부터 적층된 상자들의 무게중심이 바로 아래상자의 범위에 있는지 확인
n, l = map(int, input().split())
mlist = list(map(int, input().split()))

sum = 0

for i in range(n-1, 0, -1):
    sum += mlist[i]
    center = sum / (n-i)

    if center <= (mlist[i-1] - l) or center >= (mlist[i-1] + l):
        print("unstable")
        break
else:
    print("stable")