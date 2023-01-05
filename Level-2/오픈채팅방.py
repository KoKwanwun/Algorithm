def solution(record):
    mdict = dict()
    
    # dictionary를 활용하여 아이디의 닉네임을 최신화
    for i in range(len(record)):
        if(record[i].split(" ")[0] != "Leave"):
            mdict[record[i].split(" ")[1]] = record[i].split(" ")[2]
                    
    # 최신화된 아이디에 해당하는 닉네임으로 Enter, Leave 출력하기
    result = []
    
    for i in range(len(record)):
        if(record[i].split(" ")[0] == "Enter"):
            result.append(mdict[record[i].split(" ")[1]] + "님이 들어왔습니다.")
        elif(record[i].split(" ")[0] == "Leave"):
            result.append(mdict[record[i].split(" ")[1]] + "님이 나갔습니다.")
    
    return result