def solution(phone_book):
    # 정렬하여 다음 번호만 비교하면 되도록 함
    phone_book = sorted(phone_book)
    
    # i인덱스의 문자열을 다음 문자열과 비교(i문자열의 크기만큼만)
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
        
    return True