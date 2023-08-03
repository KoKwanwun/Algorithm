n, b = input().split()
n = n[::-1]     # 뒤집기
b = int(b)      # pow 사용을 위한 int화
result = 0

for i in range(len(n)):
    tmp = n[i]

    # 알파벳인 경우, 정해진 숫자로 변환
    # 그 외의 경우는 int화
    if(tmp.isalpha()):
        tmp = ord(tmp) - 55
    else:
        tmp = int(tmp)

    # 10진수로 변환하기 위한 식
    result += pow(b, i) * tmp

print(result)