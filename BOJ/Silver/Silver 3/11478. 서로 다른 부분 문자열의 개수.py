s = list(input())

mset = set()

# 이중 for문으로 부분 문자열 만든 후, set에 넣기
for i in range(len(s)):
    for j in range(i, len(s)):
        mset.add(''.join(s[i:j+1]))

print(len(mset))