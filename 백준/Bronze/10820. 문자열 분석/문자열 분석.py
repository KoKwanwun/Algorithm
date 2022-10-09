import sys

while(True):
    s = sys.stdin.readline().rstrip('\n')

    if not s:
        break

    cntList = [0,0,0,0]

    for i in range(len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            cntList[0] += 1
        elif ord(s[i]) >= 65 and ord(s[i]) <= 90:
            cntList[1] += 1
        elif ord(s[i]) >= 48 and ord(s[i]) <= 57:
            cntList[2] += 1
        elif s[i] == " ":
            cntList[3] += 1

    for i in range(4):
        print(cntList[i], end=" ")

    print()