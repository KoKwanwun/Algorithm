def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        # -1해준 것은 위치를 인덱스로 바꿔주기 위해
        tmp = array[commands[i][0]-1:commands[i][1]]
        tmp.sort()
        answer.append(tmp[commands[i][2]-1])
    
    return answer