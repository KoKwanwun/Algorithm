def solution(s):
    # 결과값 초기화
    tryCnt = 0
    zeroCnt = 0

    while True:
        # len(s)가 1, 즉 s가 1이 되면 탈출
        if(len(s) == 1):
            break

        # 0을 공백으로 바꾸고 zeroCnt에 0을 제거하기 전 후 차이를 더해줌
        removes = s.replace('0','')
        tmp = len(removes)
        zeroCnt += (len(s) - tmp)

        # 시도횟수 +1 및 1의 개수를 2진수로 변환
        tryCnt += 1
        mlist = ''
        while tmp:
            mlist += str(tmp % 2)
            tmp = tmp // 2
        s = mlist[::-1]

    return [tryCnt, zeroCnt]