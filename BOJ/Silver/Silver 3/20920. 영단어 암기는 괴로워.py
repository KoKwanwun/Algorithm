import sys

n, m = map(int, sys.stdin.readline().split())
# 딕셔너리
words = {}

for _ in range(n):
    word = sys.stdin.readline().rstrip()

    # 길이가 m 미만이면 continue
    # 단어가 없다면 생성, 있다면 갱신
    if len(word) < m:
        continue
    else:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

# items : key, value를 쌍으로
# -x[1], -len(x[0]), x[0] : 최빈값, 길이가 긴, 알파벳 순
result = sorted(words.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for each in result:
    print(each[0])