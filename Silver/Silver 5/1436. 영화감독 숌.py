n = int(input())
cnt = 0
# 666이 1번이므로 665부터 시작
num = 665

# 적어도 3개 이상 연속이기 때문에 666만 체크해도 됨
while cnt < n:
    num += 1
    if '666' in str(num):
        cnt += 1

print(num)