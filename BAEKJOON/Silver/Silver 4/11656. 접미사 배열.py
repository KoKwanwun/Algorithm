word = input()
mlist = []

# 접미사 리스트에 추가
for i in range(len(word)):
    mlist.append(word[i:])

# 정렬 후 프린트
for each in sorted(mlist):
    print(each)