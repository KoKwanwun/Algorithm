dexVal = int(input(), 2)        # 2진수 -> 10진수
octVal = oct(dexVal)            # 10진수 -> 8진수
print(octVal[2:])               # 2진수(0b), 8진수(0o), 16진수(0x)로 시작하기 때문에 인덱수 2부터 가져오기