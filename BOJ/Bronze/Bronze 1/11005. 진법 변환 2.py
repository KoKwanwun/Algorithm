n, b = map(int, input().split())
result = ""

while n:
    tmp = n % b
    n = n // b

    # 숫자로 표시할 수 없는 자리 알파벳 대문자를 사용
    if(tmp >= 10):
        result += chr(55 + tmp)
    else:
        result += str(tmp)

# 진법 변환시 뒤집어야 함
print(result[::-1])