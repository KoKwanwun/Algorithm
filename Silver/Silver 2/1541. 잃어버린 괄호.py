# 첫번째 원소는 무조건 양수
# -가 나오면 다음 -가 나올 때까지 뒷 원소 더해준 후 빼주기
# 즉, -를 기준으로 분리
mlist = list(input().split('-'))
result = 0

for i in range(len(mlist)):
    tmpList = list(map(int, mlist[i].split('+')))

    if i == 0:
        result += sum(tmpList)
    else:
        result -= sum(tmpList)

print(result)