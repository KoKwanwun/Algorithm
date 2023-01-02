import math

def solution(n,a,b):
    # 2의 제곱수를 차례대로 remainNum에 넣어주기(N이 2^20까지 주어짐)
    # a, b에 각각 remainNum을 나눠준 후 몫을 올림해준 것이 같으면 i를 리턴하면 됨
    """
    n = 8, a = 4, b = 5일 때, 답은 3
    remainNum = 1, 수식 결과 : 4 | 5 
    remainNum = 2, 수식 결과 : 2 | 3
    remainNum = 4, 수식 결과 : 1 | 2
    remainNum = 8, 수식 결과 : 1 | 1 -> 3 리턴
    """
    for i in range(21):
        remainNum = pow(2, i)
        
        if(math.ceil(a / remainNum) == math.ceil(b / remainNum)):
            return i