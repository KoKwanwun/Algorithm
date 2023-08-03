# 정수를 각 자리수로 나누고 정렬
mlist = sorted(list(map(int, input())), reverse=True)

for each in mlist:
    print(each, end="")