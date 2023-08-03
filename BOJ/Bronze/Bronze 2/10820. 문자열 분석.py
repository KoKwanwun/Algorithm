import sys

while True:
    # 줄바꿈 제거
    line = sys.stdin.readline().rstrip('\n')

    # 입력이 없다면 탈출
    if not line:
        break

    l, u, d, s = 0, 0, 0, 0

    for each in line:
        if each.islower():
            l += 1
        elif each.isupper():
            u += 1
        elif each.isdigit():
            d += 1
        elif each.isspace():
            s += 1
            
    print(l, u, d, s)