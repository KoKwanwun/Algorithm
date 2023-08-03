def solution(price, money, count):
    answer = 0

    for i in range(i, count+1):
        answer += i * price

    # 부족한 금액만큼 리턴, 그 외는 0
    return answer - money if answer - money > 0 else 0