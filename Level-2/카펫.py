def solution(brown, yellow):
    answer = []

    # 약수 접근
    for i in range(1, int(yellow**(1/2)) + 1):
        # i가 yellow의 약수라면
        if(yellow % i == 0):
            # yellowBrownArea : 전체 카펫 넓이(전체 격자 수)
            yellowBrownArea = (i + 2) * (yellow//i + 2)
            # 전체 카펫 넓이와 brown, yellow 격자 수 합이 같다면
            if(yellowBrownArea == (brown + yellow)):
                answer.append(i + 2)
                answer.append(yellow//i + 2)
                break

    # 항상 가로가 길다.(내림차순 정렬)
    return sorted(answer, reverse=True)