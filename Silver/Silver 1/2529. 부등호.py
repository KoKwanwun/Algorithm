n = int(input())
sign = list(input().split())
mlist = []

# 최대, 최소 범위 잘 정하기
maximum = -9999999999
minimum = 9999999999

def back():
    global maximum, minimum
    # 길이가 2일 때 부터, 부등호가 맞지 않다면 return
    if len(mlist) > 1:
        if (sign[len(mlist)-2] == '<' and mlist[-2] > mlist[-1]) or (sign[len(mlist)-2] == '>' and mlist[-2] < mlist[-1]):
            return

    # 길이가 부등호 길이 + 1이 되면 최대, 최소 갱신
    if len(mlist) == (n + 1):
        maximum = max(maximum, int("".join(map(str, mlist))))
        minimum = min(minimum, int("".join(map(str, mlist))))
        return

    for i in range(10):
        if i not in mlist:
            mlist.append(i)
            back()
            mlist.pop()

back()

"""
예시
9
< < < < < < < < <
최대 최소 : 0123456789 로 앞에 0이 붙게 됨
"""
if len(str(maximum)) == (n+1):
    print(maximum)
else:
    print('0' + str(maximum))

if len(str(minimum)) == (n+1):
    print(minimum)
else:
    print('0' + str(minimum))