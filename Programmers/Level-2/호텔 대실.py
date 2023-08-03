def solution(book_time):
    answer = 0
    endList = []
    
    # 정렬하여 for문 (대실 시작 시각 기준)
    for each in sorted(book_time):
        # 처음이라면 answer +1, 대실 종료 시각을 endList에 넣기
        # 넣을 때, 분으로 변환
        if endList == []:
            answer += 1
            endHour, endMinute = map(int, each[1].split(":"))
            endList.append(endHour * 60 + endMinute)
        else:
            # 대실 시작 시각 분으로 변환
            startHour, startMinute = map(int, each[0].split(":"))
            startTime = startHour * 60 + startMinute
            
            # 종료 시각 리스트를 돌며 10분보다 더 늦은 시간이라면 해당 종료 시각 제거
            for endTime in endList:
                if endTime + 10 <= startTime:
                    endList.remove(endTime)
                    break
            # 모두 돌아도 없다면 방 +1
            else:
                answer += 1
                
            # 종료 시각 넣기
            endHour, endMinute = map(int, each[1].split(":"))
            endList.append(endHour * 60 + endMinute)
    
    return answer