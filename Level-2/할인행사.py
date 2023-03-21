# 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수 구하기
def solution(want, number, discount):
    result = 0 

    for i in range(len(discount) - 9):                      # 10일동안 계산하기 위해
        # 10일 할인 개수가 want 품목의 number보다 작다면 break, 모두 통과했다면 +1
        for j in range(len(want)):
            if discount[i:i+10].count(want[j]) < number[j]:
                break
        else:
            result += 1
    
    return result