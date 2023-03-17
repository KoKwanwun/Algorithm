def solution(citations):
    # index 1부터 시작하도록 맞춰주기 위해 (enumerate(citations, start=1)로 해결 가능할 듯)
    citations = [0] + sorted(citations, reverse=True)
    
    # 최대값이 0이면 0리턴
    # 아래와 같이 i값이 i+1에 해당하는 값보다 크거나 같다면 i 리턴
    # 그 외는 citations의 길이 리턴 (0 인덱스를 붙였기 때문에 -1 해줌)
    """
        1 2 3 4 5
        6 5 3 3 2
    """
    if citations[1] == 0:
        return 0
    else:
        for i in range(1, len(citations) - 1):
            if (i >= citations[i+1]):
                return i
        
        return len(citations) - 1