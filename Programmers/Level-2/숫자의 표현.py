# 아래 그림을 보면 1, 3, 6, 10 ,15 ... 의 숫자에 새로운 규칙이 생기며
# 각 규칙은 일정한 간격으로 계속 증가함
# ex) 12 -> 23 -> 34 -> 45 는 3에서 2씩 증가
# ex) 123 -> 234 -> 345 -> 456 는 6에서 3씩 증가
"""
1							
2							
3   12						
4							
5       23					
6   123						
7           34				
8							
9		234		45			
10	1234						
11					56		
12			345				
13						67	
14		2345					
15	12345			456			78
"""
# 위 규칙을 이용해서, (n - start) % interval == 0의 조건에 맞다면 +1을 해줌
def solution(n):
    start = 1
    interval = 1
    answer = 0

    while start <= n:
        if (n - start) % interval == 0:
            answer += 1

        interval += 1
        start += interval

    return answer