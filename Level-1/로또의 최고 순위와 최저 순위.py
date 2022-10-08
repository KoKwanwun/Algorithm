def solution(lottos, win_nums):
    cnt = lottos.count(0)
    correct_nums = 0
    answer = []
    
    for i in lottos:
        if i in win_nums:
            correct_nums += 1
    # 맞은 개수가 없으면 0의 개수대로 최고 최저 순위 리스트 추가
    if correct_nums == 0:
        if cnt == 0:
            answer.append(6)
            answer.append(6)
        else:
            answer.append(7 - cnt)
            answer.append(6)
    # 맞은 개수를 빼준 후, 0의 개수대로 최고 최저 순위 리스트 추가
    else:
        answer.append(7 - correct_nums - cnt)
        answer.append(7 - correct_nums)
  

    return answer