import math

def solution(fees, records):
    answer = []
    dict = {}

    # records를 이중 리스트화 한 후, 차량 번호, 시간 순으로 정렬
    for i in range(len(records)):
        records[i] = list(records[i].split())
    records = sorted(records, key = lambda x : (x[1], x[0]))

    # 차량 번호가 같은 것끼리 dictionary 생성
    for i in range(len(records)):
        if records[i][1] not in dict:
            dict[records[i][1]] = []
        dict[records[i][1]].append(records[i][0])

    # 차량 번호별로 계산
    for each in dict:
        # 기록이 홀수라면(출차기 록이 하나 없다면, 23:59 기록 추가)
        if len(dict[each]) % 2:
            dict[each].append("23:59")

        # 시간 계산
        price = 0
        time = 0
        for i in range(0, len(dict[each]), 2):
            inHour = int(dict[each][i].split(':')[0])
            inMin = int(dict[each][i].split(':')[1])
            outHour = int(dict[each][i+1].split(':')[0])
            outMin = int(dict[each][i+1].split(':')[1])

            if outMin < inMin:
                outHour -= 1
                outMin += 60

            time += (outHour - inHour) * 60 + (outMin - inMin)

        # 금액 계산
        price += fees[1]
        time -= fees[0]

        if time > 0:
            price += math.ceil(time / fees[2]) * fees[3]
        answer.append(price)

    return answer