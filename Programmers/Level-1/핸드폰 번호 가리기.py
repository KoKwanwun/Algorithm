# 뒷자리 4개를 제외하고 *로 변환
def solution(phone_number):
    phone_number = list(phone_number)
    for i in range(len(phone_number) - 4):
        phone_number[i] = "*"
    return ''.join(phone_number)