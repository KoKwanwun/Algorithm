# 2진수(0b), 8진수(0o), 16진수(0x)로 시작하기 때문에 인덱스 2부터 가져오기
dexVal = int(input(), 8)
binVal = bin(dexVal)
print(binVal[2:])