n = int(input())
num = list(map(int, input().split()))
plus, miuns, multiply, divide = map(int, input().split())

maximum = -1e9
minimum = 1e9

# 함수 변수에 넣는 것으로 기존 num, 연산자에 영향을 주지 않음
def back(i, total, plus, miuns, multiply, divide):
    global maximum, minimum

    if i == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    
    # if문 4개로 전체 경우의 수 돌리기
    if plus:
        back(i + 1, total + num[i], plus - 1, miuns, multiply, divide)
    if miuns:
        back(i + 1, total - num[i], plus, miuns - 1, multiply, divide)
    if multiply:
        back(i + 1, total * num[i], plus, miuns, multiply - 1, divide)
    if divide:
        # int(total / num[i]) : 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고 몫을 음수로 바꾼 것
        back(i + 1, int(total / num[i]), plus, miuns, multiply, divide - 1)

back(1, num[0], plus, miuns, multiply, divide)
print(maximum)
print(minimum)