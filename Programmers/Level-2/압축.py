def solution(msg):
    result = []
    dic = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}
    idx = 27

    # for문을 사용해도 되지만 i를 중간중간 변경하기 위해 while문 사용
    i = 0
    while i < len(msg):
        # i부터 문자열 끝까지 중 사전에 있는 것을 찾기 위해 j는 -1 규칙
        for j in range(len(msg), i, -1):
            if msg[i:j] in dic.keys():          # 해당 문자열이 존재한다면, 결과에 idx 넣고, 문자열 하나 추가한 것을 사전에 넣기
                result.append(dic[msg[i:j]])
                dic[msg[i:j+1]] = idx
                idx += 1
                i = j - 1                       # i값 변경
        i += 1
        
    return result