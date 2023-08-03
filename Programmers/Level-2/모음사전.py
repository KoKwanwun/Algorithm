# 완전탐색
# 다른 사람 풀이의 예로 5중 for문을 돌리면서 리스트에 넣고 다시 찾는 과정을 했을 때는 시간이 오래 걸림
# 나는 5중 for문을 돌리면서 찾아 시간 단축
def solution(word):
    answer = 0
    
    for one in "AEIOU":
        answer += 1
        if one == word:
            return answer
        
        for two in "AEIOU":
            answer += 1
            if (one + two) == word:
                return answer
            
            for three in "AEIOU":
                answer += 1
                if (one + two + three) == word:
                    return answer
            
                for four in "AEIOU":
                    answer += 1
                    if (one + two + three + four) == word:
                        return answer
                    
                    for five in "AEIOU":
                        answer += 1
                        if (one + two + three + four + five) == word:
                            return answer