# 미리 찍는 방식 리스트를 만들어 놓은 후 반복하게 코딩
# 1번, 2번, 3번 수포자의 MAX 값을 순서대로 넣기 때문에 따로 정렬할 필요 없음
def solution(answers):
    answer = []
    data1 = [ 1, 2, 3, 4, 5 ]
    data2 = [ 2, 1, 2, 3, 2, 4, 2, 5 ]
    data3 = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 ]
    
    correct1 = 0
    correct2 = 0
    correct3 = 0
    
    k1 = 0
    k2 = 0
    k3 = 0
    
    for i in range(len(answers)):
        if answers[i] == data1[k1]:
            correct1 += 1
        if answers[i] == data2[k2]:
            correct2 += 1
        if answers[i] == data3[k3]:
            correct3 += 1
            
        k1 += 1
        k2 += 1
        k3 += 1
        
        if k1 == 5:
            k1 = 0
        if k2 == 8:
            k2 = 0
        if k3 == 10:
            k3 = 0
    
    if correct1 == max(correct1,correct2,correct3):
        answer.append(1)
    if correct2 == max(correct1,correct2,correct3):
        answer.append(2)
    if correct3 == max(correct1,correct2,correct3):
        answer.append(3)
    
    return answer