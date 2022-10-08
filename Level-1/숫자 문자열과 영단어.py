def solution(s):

    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, j in enumerate(num_list):
        # s에 num_list에 있는 것이 있다면 지우고 해당 인덱스 값(숫자로 바꾼 값) 넣기
        # s.split은 기준으로 자르는 거기 때문에 사라진다고도 볼 수 있음
        s = str(i).join(s.split(j))
        print(s)
    return int(s)