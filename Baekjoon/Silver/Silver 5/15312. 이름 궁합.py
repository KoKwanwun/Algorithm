a = list(input())
b = list(input())
alpha = {'A' : 3, 'B' : 2, 'C' : 1, 'D' : 2, 'E' : 3, 'F' : 3, 'G' : 2, 'H' : 3, 'I' : 3, 'J' : 2, 'K' : 2, 'L' : 1, 'M' : 2, 'N' : 2, 'O' : 1,
         'P' : 2, 'Q' : 2, 'R' : 2, 'S' : 1, 'T' : 2, 'U' : 1, 'V' : 1, 'W' : 1, 'X' : 2, 'Y' : 2, 'Z' : 1}

# 이름 궁합에 사용할 리스트 만들기
mlist = []
for i in range(len(a)):
    mlist.append(alpha[a[i]])
    mlist.append(alpha[b[i]])

# 이름 궁합 실행
while len(mlist) > 2:
    tmpList = []
    for i in range(len(mlist)-1):
        tmpList.append((mlist[i] + mlist[i+1]) % 10)
    mlist = tmpList

# 2자리 수 출력
print(str(mlist[0]) + str(mlist[1]))