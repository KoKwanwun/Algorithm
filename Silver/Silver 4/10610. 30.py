# 30의 배수 = 3 * 10의 배수
# 10으로 나눈 후 3의 배수 찾는다고 생각하기 -> 적어도 0이 하나 존재해야함
mlist = list(map(int, list(input())))

cnt0 = 0
sum = 0

# 0의 개수 및 각자리수 합 구하기
for num in mlist:
    if(num == 0):
        cnt0 += 1
    sum += num

# 0의 개수가 0이거나, 합이 3의 배수가 아니면 존재X
if((cnt0 == 0) or (sum % 3 != 0)):
    print(-1)
# mlist를 내림차순으로 정렬한 후, 각 자리수 붙여주기
else:
    mlist.sort(reverse=True)
    print(''.join(map(str, mlist)))